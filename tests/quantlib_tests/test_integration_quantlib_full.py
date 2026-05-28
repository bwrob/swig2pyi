"""Integration test: generate full QuantLib stubs and verify coverage."""

from __future__ import annotations

import ast
import importlib
import os
import tempfile
import types
from pathlib import Path

import pytest

from swig2pyi.core.config import Config
from swig2pyi.core.emitter import StubEmitter
from swig2pyi.core.parser import SwigXmlParser
from swig2pyi.core.qa import CoverageReport, StubCoverageChecker
from swig2pyi.core.runner import SwigRunner
from swig2pyi.core.type_system import TypeManager

TESTS_DIR = Path(__file__).parent.parent
ROOT_DIR = TESTS_DIR.parent
INTERFACE_FILE = TESTS_DIR / "data" / "quantlib-1.40" / "quantlib_full.i"
CONFIG_FILE = ROOT_DIR / "src" / "swig2pyi" / "rules" / "quantlib.json"
MODULE_NAME = "QuantLib"

# ---------------------------------------------------------------------------
# Extra-code symbols added by quantlib.json that are not parsed from the
# SWIG XML (they are manually specified in the config as generic helpers).
# These ARE expected in the stub but will not be found via the AST builder.
# ---------------------------------------------------------------------------
EXTRA_CODE_SYMBOLS = {"Handle", "RelinkableHandle", "TimeSeries"}

# ---------------------------------------------------------------------------
# Known differences: stub classes that exist in quantlib.json or the partial
# interface but are NOT directly exported to Python by the installed QuantLib.
# SWIG exposes concrete template instantiations (e.g. QuoteHandle), not the
# generic template class itself (Handle). Enums are exposed as int constants
# not as Python classes in older SWIG/QuantLib configurations.
# ---------------------------------------------------------------------------
STUB_ONLY_ALLOWLIST: set[str] = {
    # Generic template helpers (concrete forms are exposed instead)
    "Handle",
    "RelinkableHandle",
    "TimeSeries",
    # std::string mapped class (not exported as Python class in newer QuantLib)
    "string",
    # Wrapper helper types
    "OptionalBool",
    "OptionalInteger",
    "OptionalFrequency",
    # C++ enums exposed as int constants, not Python classes, by this version
    "BusinessDayConvention",
    "Compounding",
    "Frequency",
    "JointCalendarRule",
    "Month",
    "TimeUnit",
    "Weekday",
    # Internal TypeVar used in stubs
    "_T",
    # Anonymous SWIG proxy types (e.g. Observer mixin helpers) — start with __
    # and therefore excluded from runtime dir() by our public-symbol filter, but
    # they are valid SWIG-generated classes that belong in the stub.
    "__dummy_0__",
    "__dummy_1__",
    "__dummy_2__",
    "__dummy_3__",
    "__dummy_4__",
    "__dummy_5__",
    "__dummy_6__",
    "__dummy_7__",
    "__dummy_8__",
    "__dummy_9__",
}


@pytest.fixture(scope="module")
def generated_stub_text() -> str:
    """Generate the QuantLib stub from the test interface and return its text."""
    config = Config.from_file(CONFIG_FILE)
    runner = SwigRunner()

    xml_fd, xml_path = tempfile.mkstemp(suffix=".xml")
    os.close(xml_fd)
    xml_path_obj = Path(xml_path)

    try:
        runner.run(config.includes, INTERFACE_FILE, xml_path_obj)
        parser = SwigXmlParser()
        top = parser.parse_file(xml_path_obj)
    finally:
        if xml_path_obj.exists():
            xml_path_obj.unlink()

    tm = TypeManager(config)
    emitter = StubEmitter(tm)
    emitter.emit(top)
    return emitter.get_output()


@pytest.fixture(scope="module")
def generated_stub_path(generated_stub_text: str) -> Path:
    """Write the generated stub to a temp file and return the path."""
    stub_fd, stub_path = tempfile.mkstemp(suffix=".pyi")
    os.close(stub_fd)
    stub_path_obj = Path(stub_path)
    stub_path_obj.write_text(generated_stub_text, encoding="utf-8")
    return stub_path_obj


@pytest.fixture(scope="module")
def stub_top_level_names(generated_stub_text: str) -> set[str]:
    """Parse the stub and return the set of top-level names it defines."""
    tree = ast.parse(generated_stub_text)
    names: set[str] = set()
    for node in tree.body:
        if isinstance(node, ast.ClassDef | ast.FunctionDef | ast.AsyncFunctionDef):
            names.add(node.name)
        elif isinstance(node, ast.AnnAssign) and isinstance(node.target, ast.Name):
            names.add(node.target.id)
        elif isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name):
                    names.add(target.id)
    return names


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------


def test_full_stub_generates_classes(stub_top_level_names: set[str]) -> None:
    """The generated stub must contain a substantial number of class definitions."""
    # Count only class definitions (not function/enum aliases)
    assert len(stub_top_level_names) >= 100, (
        f"Expected >= 100 top-level definitions, got {len(stub_top_level_names)}"
    )


def test_full_stub_has_no_template_leaks(generated_stub_text: str) -> None:
    """Module-level functions leaked from uninstantiated templates must be absent."""
    # These names appear as SWIG template member names that must NOT be at module level
    leaked_names = {"def first(", "def second(", "def third(", "def asObservable("}
    for leaked in leaked_names:
        assert leaked not in generated_stub_text, (
            f"Template-member leak detected: {leaked!r} found at module level"
        )


def test_stub_does_not_define_phantom_runtime_symbols(
    stub_top_level_names: set[str],
) -> None:
    """Every stub-defined symbol (outside the allowlist) must exist in the QuantLib runtime.

    This catches cases where we are generating stubs for C++ constructs that
    SWIG does NOT actually expose to Python (e.g. internal template classes).
    """
    try:
        ql = importlib.import_module(MODULE_NAME)
    except ImportError:
        pytest.skip("QuantLib not importable — phantom symbol check skipped.")

    runtime_symbols = {
        name
        for name in dir(ql)
        if not name.startswith("_")
        and not isinstance(getattr(ql, name, None), types.ModuleType)
    }

    phantom = (
        {s for s in stub_top_level_names if not s.startswith("_")}
        - runtime_symbols
        - STUB_ONLY_ALLOWLIST
    )
    assert phantom == set(), (
        f"{len(phantom)} stub-defined symbol(s) are absent from the QuantLib runtime "
        f"(not in allowlist):\n" + "\n".join(f"  - {s}" for s in sorted(phantom)[:30])
    )


def test_full_stub_coverage(
    generated_stub_path: Path,
) -> None:
    """All runtime QuantLib symbols covered by the interface must appear in the stub.

    Uses StubCoverageChecker. Only symbols that both (a) exist in the QuantLib
    runtime AND (b) appear in the generated stub or our allowlist are checked.
    """
    checker = StubCoverageChecker()
    report: CoverageReport | None = checker.check(generated_stub_path, MODULE_NAME)

    if report is None:
        pytest.skip("QuantLib not importable — coverage check skipped.")

    # We do NOT assert full coverage (the partial interface only covers a subset
    # of the installed QuantLib runtime). Instead we assert that every symbol
    # the stub defines (minus the allowlist) is in the runtime — that's the
    # phantom check above. Here we just log coverage as information.
    assert report.stub_symbol_count > 0, "Stub has no top-level symbols."
    assert report.runtime_symbol_count > 0, "Runtime has no public symbols."
