"""SWIG execution runner."""

import hashlib
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
    """Handles execution of the SWIG binary to generate XML output."""

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

    def _hash_directory_files(
        self,
        hasher: "hashlib._Hash",  # pyright: ignore [reportPrivateUsage]
        directory: Path,
        suffixes: tuple[str, ...] = (),
    ) -> None:
        """Hash file metadata from a directory into the hasher."""
        if not directory.exists() or not directory.is_dir():
            return
        for root, _, files in os.walk(directory):
            for file in sorted(files):
                if suffixes and not file.endswith(suffixes):
                    continue
                file_path = Path(root) / file
                try:
                    stat = file_path.stat()
                except OSError:
                    _logger.debug("Cannot stat %s", file_path)
                    continue
                hasher.update(file.encode("utf-8"))
                hasher.update(str(stat.st_size).encode("utf-8"))
                hasher.update(str(stat.st_mtime).encode("utf-8"))

    def _compute_cache_key(
        self, includes: list[str], interface_file: Path, env: dict[str, str]
    ) -> str:
        """Compute a SHA256 cache key based on inputs."""
        hasher = hashlib.sha256()
        hasher.update(self._get_swig_version(env).encode("utf-8"))
        hasher.update(str(interface_file.resolve()).encode("utf-8"))
        if interface_file.exists():
            hasher.update(interface_file.read_bytes())

        for inc_dir in sorted(includes):
            self._hash_directory_files(
                hasher, Path(inc_dir), suffixes=(".i", ".h", ".hpp")
            )

        mocks_dir = Path(__file__).parent.parent / "mocks"
        self._hash_directory_files(hasher, mocks_dir)
        return hasher.hexdigest()

    def run(
        self,
        includes: list[str],
        interface_file: Path,
        output_xml: Path,
        module_name: str = "swig2pyi_wrapper",
    ) -> Path:
        """Execute SWIG to generate XML, using cache if available."""
        project_root = Path(__file__).parent.parent.parent.parent
        cache_dir = project_root / ".temp" / "swig_xml_cache"

        env = os.environ.copy()
        cache_key = self._compute_cache_key(includes, interface_file, env)
        cache_file = cache_dir / f"{cache_key}.xml"

        if cache_file.exists():
            output_xml.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(cache_file, output_xml)
            return output_xml

        with tempfile.TemporaryDirectory() as temp_dir:
            temp_dir_path = Path(temp_dir)
            dummy_cpp = temp_dir_path / "dummy_wrap.cpp"

            cmd, env = self._build_command(
                includes, output_xml, dummy_cpp, temp_dir_path
            )
            tmp_path = self._create_wrapper(interface_file, module_name)
            cmd.append(str(tmp_path))

            try:
                result_path = self._execute(cmd, env, output_xml)
                try:
                    cache_dir.mkdir(parents=True, exist_ok=True)
                    shutil.copy2(result_path, cache_file)
                except OSError:
                    _logger.debug("Failed to cache SWIG XML output")
                return result_path
            finally:
                if tmp_path.exists():
                    tmp_path.unlink()

    def _build_command(
        self, includes: list[str], output_xml: Path, dummy_cpp: Path, outdir: Path
    ) -> tuple[list[str], dict[str, str]]:
        """Build the SWIG command and environment."""
        env = os.environ.copy()
        if self.use_module and swig:
            exe = Path(swig.BIN_DIR) / "swig"
            if not exe.exists() and os.name == "nt":
                exe = exe.with_suffix(".exe")
            env.update(swig.SWIG_LIB_ENV)
            cmd = [str(exe)]
        else:
            if not shutil.which(self.swig_path):
                msg = f"SWIG not found at '{self.swig_path}'"
                raise FileNotFoundError(msg)
            cmd = [self.swig_path]

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

    def _create_wrapper(self, interface_file: Path, module_name: str) -> Path:
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
