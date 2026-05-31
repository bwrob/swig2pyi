"""SWIG execution runner."""

import contextlib
import hashlib
import logging
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

try:
    import swig  # pyright: ignore [reportMissingImports, reportMissingTypeStubs]
except ImportError:
    swig = None  # pyright: ignore [reportMissingImports]

_SWIG_MODULE_AVAILABLE: bool = swig is not None
_logger = logging.getLogger(__name__)


def parse_dependencies(output: str) -> list[str]:
    """Parse Makefile-style dependencies output by swig -MM."""
    idx = output.find(":")
    # Handle Windows drive letter at the start (e.g., C:\...)
    if idx == 1 and output[0].isalpha():
        idx = output.find(":", 2)

    if idx == -1:
        return []

    deps_part = output[idx + 1 :].replace("\\\n", " ").replace("\\\r\n", " ")
    tokens = deps_part.split()

    deps: list[str] = []
    for token in tokens:
        t = token.strip()
        if t and t != "\\":
            deps.append(t)
    return deps


def _safe_stat(path: Path) -> os.stat_result | None:
    """Safely get stat of a file, returning None on OSError."""
    try:
        return path.stat()
    except OSError:
        _logger.debug("Cannot stat dependency %s", path)
        return None


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

    def _run_swig_mm(
        self, wrapper_path: Path, includes: list[str], env: dict[str, str]
    ) -> str:
        """Execute swig -MM to print file dependencies to stdout."""
        exe = self._get_swig_exe()
        cmd = [str(exe), "-MM", "-python", "-c++"]

        mocks_dir = Path(__file__).parent.parent / "mocks"
        if mocks_dir.exists():
            cmd.append(f"-I{mocks_dir}")

        cmd.extend(f"-I{inc}" for inc in includes)
        cmd.append(str(wrapper_path))

        run_env = env.copy()
        if self.use_module and swig:
            run_env.update(swig.SWIG_LIB_ENV)

        res = subprocess.run(  # noqa: S603
            cmd, capture_output=True, text=True, check=True, env=run_env
        )
        return res.stdout

    def _parse_and_filter_dependencies(
        self, output: str, wrapper_path: Path
    ) -> list[Path]:
        """Parse raw dependencies and filter out non-existent and temp files."""
        dep_paths = parse_dependencies(output)
        paths: list[Path] = []
        for p in dep_paths:
            path_obj = Path(p)
            if path_obj.resolve() == wrapper_path.resolve():
                continue
            if path_obj.exists():
                paths.append(path_obj)
        return paths

    def _get_dependencies(
        self, includes: list[str], interface_file: Path, env: dict[str, str]
    ) -> list[Path]:
        """Run swig -MM to find all file dependencies."""
        wrapper_path = self._create_wrapper(interface_file)
        try:
            output = self._run_swig_mm(wrapper_path, includes, env)
            return self._parse_and_filter_dependencies(output, wrapper_path)
        except (OSError, subprocess.CalledProcessError) as e:
            _logger.warning("Failed to run swig -MM for dependency tracking: %s", e)
            return [interface_file] if interface_file.exists() else []
        finally:
            with contextlib.suppress(OSError):
                wrapper_path.unlink()

    def _compute_cache_key(
        self, includes: list[str], interface_file: Path, env: dict[str, str]
    ) -> str:
        """Compute a SHA256 cache key based on inputs."""
        hasher = hashlib.sha256()
        hasher.update(self._get_swig_version(env).encode("utf-8"))
        hasher.update(str(interface_file.resolve()).encode("utf-8"))
        if interface_file.exists():
            hasher.update(interface_file.read_bytes())

        dependencies = self._get_dependencies(includes, interface_file, env)
        for dep in sorted(dependencies, key=lambda p: str(p.resolve())):
            stat = _safe_stat(dep)
            if stat is not None:
                hasher.update(str(dep.resolve()).encode("utf-8"))
                hasher.update(str(stat.st_size).encode("utf-8"))
                hasher.update(str(stat.st_mtime).encode("utf-8"))

        return hasher.hexdigest()

    def _get_cache_dir(self) -> Path:
        """Resolve the OS-appropriate cache directory for SWIG XML files."""
        cache_base = self._get_cache_base_dir()
        if cache_base:
            cache_dir = cache_base / "swig_xml_cache"
        else:
            cache_dir = Path(tempfile.gettempdir()) / "swig_xml_cache"

        try:
            cache_dir.mkdir(parents=True, exist_ok=True)
        except OSError:
            cache_dir = Path(tempfile.gettempdir()) / "swig_xml_cache"
            with contextlib.suppress(OSError):
                cache_dir.mkdir(parents=True, exist_ok=True)
        return cache_dir

    def _get_cache_base_dir(self) -> Path | None:
        """Resolve the OS-appropriate user cache directory."""
        if os.name == "nt":
            local_appdata = os.environ.get("LOCALAPPDATA") or os.environ.get("APPDATA")
            if local_appdata:
                return Path(local_appdata) / "swig2pyi" / "Cache"
            return None

        xdg_cache = os.environ.get("XDG_CACHE_HOME")
        if xdg_cache:
            return Path(xdg_cache) / "swig2pyi"

        if sys.platform == "darwin":
            return Path("~/Library/Caches/swig2pyi").expanduser()

        return Path("~/.cache/swig2pyi").expanduser()

    def run(
        self,
        includes: list[str],
        interface_file: Path,
        output_xml: Path,
        module_name: str = "swig2pyi_wrapper",
    ) -> Path:
        """Execute SWIG to generate XML, using cache if available."""
        cache_dir = self._get_cache_dir()
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
