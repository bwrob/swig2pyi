import subprocess
import sys
from pathlib import Path


def validate_stub(file_path: Path) -> bool:
    """Run ruff and pyright to validate the generated stubs in tests."""
    python = sys.executable

    # Format
    subprocess.run([python, "-m", "ruff", "format", str(file_path)], check=True)
    # Check & fix
    subprocess.run(
        [
            python,
            "-m",
            "ruff",
            "check",
            "--fix",
            "--select=E,F,W",
            "--ignore=E501",
            str(file_path),
        ],
        check=True,
    )

    # Run basedpyright if available
    try:
        res = subprocess.run(
            [python, "-m", "basedpyright", str(file_path)],
            capture_output=True,
            text=True,
            check=False,
        )
        if res.returncode != 0:
            return False
    except FileNotFoundError:
        pass  # basedpyright not installed, skip

    return True
