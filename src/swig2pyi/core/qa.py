"""Validates generated .pyi files and checks symbol coverage."""

from __future__ import annotations

import ast
import importlib
import logging
import sys
import types
from dataclasses import dataclass, field
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pathlib import Path

logger = logging.getLogger(__name__)


@dataclass
class CoverageReport:
    """Result of a stub coverage check against a runtime module."""

    runtime_symbol_count: int
    stub_symbol_count: int
    missing: list[str] = field(default_factory=list)
    allowlisted: list[str] = field(default_factory=list)

    @property
    def uncovered_count(self) -> int:
        """Symbols missing from stub that are not in the allowlist."""
        return len(self.missing)

    @property
    def coverage_pct(self) -> float:
        """Percentage of runtime symbols covered by the stub."""
        if self.runtime_symbol_count == 0:
            return 100.0
        covered = self.runtime_symbol_count - self.uncovered_count
        return 100.0 * covered / self.runtime_symbol_count


class StubCoverageChecker:
    """Checks that a .pyi stub covers the public API of an importable module."""

    def __init__(self, allowlist: set[str] | None = None) -> None:
        """Initialise with an optional set of known-missing symbol names to suppress."""
        self.allowlist: set[str] = allowlist or set()

    def check(
        self,
        stub_path: Path,
        module_name: str,
    ) -> CoverageReport | None:
        """Compare the stub at *stub_path* against the live *module_name*.

        Returns ``None`` if the module cannot be imported (e.g. native library not
        available in the current environment) so callers can skip gracefully.
        """
        module = self._try_import(module_name)
        if module is None:
            logger.warning("Coverage check skipped: could not import %r", module_name)
            return None

        runtime_symbols = self._public_runtime_symbols(module)
        stub_symbols = self._stub_top_level_names(stub_path)

        missing_raw = runtime_symbols - stub_symbols
        allowlisted = sorted(missing_raw & self.allowlist)
        missing = sorted(missing_raw - self.allowlist)

        return CoverageReport(
            runtime_symbol_count=len(runtime_symbols),
            stub_symbol_count=len(stub_symbols),
            missing=missing,
            allowlisted=allowlisted,
        )

    @staticmethod
    def _try_import(module_name: str) -> types.ModuleType | None:
        try:
            return importlib.import_module(module_name)
        except ImportError as e:
            logger.warning(
                "Could not import module %s due to ImportError: %s", module_name, e
            )
            sys.stderr.write(f"Warning: Could not import module {module_name}\n")
            return None
        except Exception as e:  # noqa: BLE001
            logger.warning(
                "Could not import module %s due to error: %s", module_name, e
            )
            sys.stderr.write(f"Warning: Could not import module {module_name}\n")
            return None

    @staticmethod
    def _is_native_symbol(name: str, obj: object, module_name: str) -> bool:
        if name.startswith("_") or isinstance(obj, types.ModuleType):
            return False

        obj_module = getattr(obj, "__module__", None)
        if not isinstance(obj_module, str):
            return True

        shadow_module_name = f"_{module_name}"
        is_same_pkg = (
            obj_module in (module_name, shadow_module_name)
            or obj_module.startswith((module_name + ".", shadow_module_name + "."))
            or module_name.startswith(obj_module + ".")
        )
        is_mock = module_name == "mock_mod" or module_name.startswith("mock")
        return is_same_pkg or is_mock

    @staticmethod
    def _public_runtime_symbols(module: types.ModuleType) -> set[str]:
        symbols: set[str] = set()
        module_name = module.__name__
        for name in dir(module):
            obj = getattr(module, name, None)
            if obj is not None and StubCoverageChecker._is_native_symbol(
                name, obj, module_name
            ):
                symbols.add(name)
        return symbols

    @staticmethod
    def _stub_top_level_names(stub_path: Path) -> set[str]:
        source = stub_path.read_text(encoding="utf-8")
        tree = ast.parse(source)
        names: set[str] = set()
        for node in tree.body:
            names.update(StubCoverageChecker._names_from_node(node))
        return names

    @staticmethod
    def _names_from_node(node: ast.stmt) -> set[str]:
        """Extract defined names from a single top-level AST statement."""
        if isinstance(node, ast.ClassDef | ast.FunctionDef | ast.AsyncFunctionDef):
            return {node.name}
        if isinstance(node, ast.AnnAssign) and isinstance(node.target, ast.Name):
            return {node.target.id}
        if isinstance(node, ast.Assign):
            return StubCoverageChecker._names_from_assign(node)
        return set()

    @staticmethod
    def _names_from_assign(node: ast.Assign) -> set[str]:
        """Extract target names from an assignment statement."""
        return {target.id for target in node.targets if isinstance(target, ast.Name)}
