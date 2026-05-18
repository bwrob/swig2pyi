import shutil
import subprocess
from pathlib import Path


class QAValidator:
    """Validates generated .pyi files using ruff (formatting/linting) and pyright (type checking)."""

    def __init__(self) -> None:
        self.ruff_path = shutil.which("ruff")
        self.pyright_path = shutil.which("pyright") or shutil.which("basedpyright")

    def run_formatting(self, file_path: Path) -> tuple[bool, str]:
        """Runs ruff format and check --fix on the file."""
        if not self.ruff_path:
            return False, "Ruff executable not found."

        try:
            # Format
            subprocess.run(
                [self.ruff_path, "format", str(file_path)],
                check=True,
                capture_output=True,
            )
            # Lint and fix
            subprocess.run(
                [self.ruff_path, "check", "--fix", str(file_path)],
                check=True,
                capture_output=True,
            )
            return True, "Formatting and linting successful."
        except subprocess.CalledProcessError as e:
            return False, f"Ruff failed:\n{e.stderr.decode()}"

    def run_type_check(self, file_path: Path) -> tuple[bool, str]:
        """Runs pyright on the file."""
        if not self.pyright_path:
            return False, "Pyright executable not found."

        try:
            # Capture output to report errors if any
            result = subprocess.run(
                [self.pyright_path, str(file_path)],
                check=False,
                capture_output=True,
            )
            output = result.stdout.decode()
            if result.returncode == 0:
                return True, "Type checking passed."
            return False, f"Type checking failed:\n{output}"
        except Exception as e:
            return False, f"Pyright execution failed: {e}"

    def validate(self, file_path: Path) -> bool:
        """Runs the full QA suite on the file.
        Returns True if all checks pass (or strictly if formatting succeeds, type checking might be warnings).
        """
        # Step 1: Format & Lint
        fmt_ok, _fmt_msg = self.run_formatting(file_path)
        if not fmt_ok:
            return False

        # Step 2: Type Check
        tc_ok, _tc_msg = self.run_type_check(file_path)
        # Print a summarized message or full output if failed
        if tc_ok:
            pass
        else:
            pass

        return fmt_ok and tc_ok
