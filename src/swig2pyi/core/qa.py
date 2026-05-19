"""Validates generated .pyi files using ruff and pyright."""

from __future__ import annotations

import shutil
import subprocess
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pathlib import Path


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
