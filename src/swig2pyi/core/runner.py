"""SWIG execution runner."""

import logging
import os
import shutil
import subprocess
import tempfile
from pathlib import Path

try:
    import swig  # pyright: ignore [reportMissingImports, reportMissingTypeStubs]
except ImportError:
    swig = None  # pyright: ignore [reportMissingImports]

_SWIG_MODULE_AVAILABLE: bool = swig is not None
_logger = logging.getLogger(__name__)


class SwigRunner:
    """Handles execution of the SWIG binary to generate XML output directly."""

    def __init__(self, swig_path: str = "swig") -> None:
        """Initialize the runner."""
        self.swig_path = swig_path
        self.use_module = _SWIG_MODULE_AVAILABLE and swig_path == "swig"

    def _get_swig_exe(self) -> Path:
        """Resolve SWIG executable path."""
        if self.use_module and swig:
            exe = Path(swig.BIN_DIR) / "swig"
            if not exe.exists() and os.name == "nt":
                exe = exe.with_suffix(".exe")
            return exe
        return Path(self.swig_path)

    def _get_swig_version(self, env: dict[str, str]) -> str:
        """Get SWIG version string."""
        try:
            res = subprocess.run(  # noqa: S603
                [str(self._get_swig_exe()), "-version"],
                capture_output=True,
                text=True,
                check=True,
                env=env,
            )
        except (OSError, subprocess.CalledProcessError):
            return ""
        else:
            return res.stdout

    def run(
        self,
        includes: list[str],
        interface_file: Path,
        output_xml: Path,
        module_name: str = "swig2pyi_wrapper",
    ) -> Path:
        """Execute SWIG to generate XML directly."""
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_dir_path = Path(temp_dir)
            dummy_cpp = temp_dir_path / "dummy_wrap.cpp"

            cmd, env = self._build_command(
                includes, output_xml, dummy_cpp, temp_dir_path
            )
            tmp_path = self._create_wrapper(interface_file, module_name)
            cmd.append(str(tmp_path))

            try:
                return self._execute(cmd, env, output_xml)
            finally:
                if tmp_path.exists():
                    tmp_path.unlink()

    def _build_command(
        self, includes: list[str], output_xml: Path, dummy_cpp: Path, outdir: Path
    ) -> tuple[list[str], dict[str, str]]:
        """Build the SWIG command and environment."""
        env = os.environ.copy()
        exe = self._get_swig_exe()
        if self.use_module and swig:
            env.update(swig.SWIG_LIB_ENV)
        elif not shutil.which(self.swig_path):
            msg = f"SWIG not found at '{self.swig_path}'"
            raise FileNotFoundError(msg)
        cmd = [str(exe)]

        mocks_dir = Path(__file__).parent.parent / "mocks"
        if mocks_dir.exists():
            cmd.append(f"-I{mocks_dir}")

        cmd.extend(
            [
                "-python",
                "-c++",
                "-xmlout",
                str(output_xml),
                "-o",
                str(dummy_cpp),
                "-outdir",
                str(outdir),
            ]
        )
        cmd.extend([f"-I{inc}" for inc in includes])
        return cmd, env

    def _create_wrapper(
        self, interface_file: Path, module_name: str = "swig2pyi_wrapper"
    ) -> Path:
        """Create a temporary SWIG interface file that includes the target."""
        preamble = f"""
%module {module_name}
%define apply_cpptypes(x...)
%enddef
%define pythoncode(x...)
%enddef
"""
        preamble += f'%include "{interface_file.resolve().as_posix()}"\n'
        with tempfile.NamedTemporaryFile(mode="w", suffix=".i", delete=False) as tmp:
            tmp.write(preamble)
            return Path(tmp.name)

    def _execute(self, cmd: list[str], env: dict[str, str], output_xml: Path) -> Path:
        """Execute the SWIG command."""
        try:
            subprocess.run(  # noqa: S603
                cmd, capture_output=True, text=True, check=True, env=env
            )
        except subprocess.CalledProcessError as e:
            msg = f"SWIG failed:\n{e.stderr}"
            raise RuntimeError(msg) from e
        except OSError as e:
            msg = f"SWIG execution failed: {e}"
            raise RuntimeError(msg) from e

        if output_xml.exists():
            return output_xml

        msg = "SWIG did not produce output file."
        raise RuntimeError(msg)
