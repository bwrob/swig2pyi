import shutil
import subprocess
import sys
from pathlib import Path


def validate_stub(file_path: Path) -> bool:
    """Run ruff and pyright to validate the generated stubs in tests."""
    ruff_path = shutil.which("ruff")
    pyright_path = shutil.which("pyright") or shutil.which("basedpyright")

    if not ruff_path:
        msg = "Ruff not found"
        raise FileNotFoundError(msg)

    use_shell = sys.platform == "win32"

    # Format
    subprocess.run([ruff_path, "format", str(file_path)], check=True, shell=use_shell)
    # Check & fix
    subprocess.run(
        [
            ruff_path,
            "check",
            "--fix",
            "--select=E,F,W",
            "--ignore=E501",
            str(file_path),
        ],
        check=True,
        shell=use_shell,
    )

    if pyright_path:
        # Run pyright/basedpyright
        res = subprocess.run(
            [pyright_path, str(file_path)],
            capture_output=True,
            text=True,
            check=False,
            shell=use_shell,
        )
        if res.returncode != 0:
            return False

    return True
