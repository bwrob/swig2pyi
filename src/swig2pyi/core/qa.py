"""Validates generated .pyi files using ruff and pyright."""

from __future__ import annotations

import ast
import importlib
import logging
import shutil
import subprocess
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

    # ------------------------------------------------------------------
    # Public interface
    # ------------------------------------------------------------------

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

    # ------------------------------------------------------------------
    # Helpers
    # ------------------------------------------------------------------

    @staticmethod
    def _try_import(module_name: str) -> types.ModuleType | None:
        try:
            return importlib.import_module(module_name)
        except ImportError:
            return None

    @staticmethod
    def _public_runtime_symbols(module: types.ModuleType) -> set[str]:
        return {
            name
            for name in dir(module)
            if not name.startswith("_")
            and not isinstance(getattr(module, name, None), types.ModuleType)
        }

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


class QAValidator:
    """Validates generated .pyi files using ruff and pyright."""

    def __init__(self) -> None:
        """Initialize validator and check for executables."""
        self.ruff_path = shutil.which("ruff")
        self.pyright_path = shutil.which("pyright") or shutil.which("basedpyright")

    def run_formatting(self, file_path: Path) -> tuple[bool, str]:
        """Run ruff format and check --fix on the file."""
        if not self.ruff_path:
            return False, "Ruff executable not found."

        try:
            # Format
            subprocess.run(  # noqa: S603
                [self.ruff_path, "format", str(file_path)],
                check=True,
            )
            # Lint and fix
            subprocess.run(  # noqa: S603
                [self.ruff_path, "check", "--fix", str(file_path)],
                check=True,
                capture_output=True,
            )
        except subprocess.CalledProcessError as e:
            return False, f"Ruff failed:\n{e.stderr.decode()}"
        else:
            return True, "Formatting and linting successful."

    def run_type_check(self, file_path: Path) -> tuple[bool, str]:
        """Run pyright on the file."""
        if not self.pyright_path:
            return False, "Pyright executable not found."

        try:
            # Capture output to report errors if any
            result = subprocess.run(  # noqa: S603
                [self.pyright_path, str(file_path)],
                check=False,
                capture_output=True,
                text=True,
            )
            output = result.stdout
        except OSError as e:
            return False, f"Pyright execution failed: {e}"
        else:
            if result.returncode == 0:
                return True, "Type checking passed."
            return False, f"Type checking failed:\n{output}"

    def validate(self, file_path: Path) -> bool:
        """Run the full QA suite on the file.

        Returns True if all checks pass (or strictly if formatting succeeds,
        type checking might be warnings).
        """
        # Step 1: Format & Lint
        fmt_ok, _fmt_msg = self.run_formatting(file_path)
        if not fmt_ok:
            return False

        # Step 2: Type check (informational)
        _py_ok, _py_msg = self.run_type_check(file_path)
        return True
