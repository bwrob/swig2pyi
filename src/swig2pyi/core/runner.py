"""SWIG execution runner."""

import os
import shutil
import subprocess
from pathlib import Path

try:
    import swig

    _SWIG_MODULE_AVAILABLE = True
except ImportError:
    _SWIG_MODULE_AVAILABLE = False

import tempfile


class SwigRunner:
    """Handles execution of the SWIG binary to generate XML output."""

    def __init__(self, swig_path: str = "swig") -> None:
        """Initialize the runner."""
        self.swig_path = swig_path
        self.use_module = _SWIG_MODULE_AVAILABLE and swig_path == "swig"

        if not self.use_module and not shutil.which(self.swig_path):
            # We don't raise immediately to allow instantiation, but run will fail.
            pass

    def run(self, includes: list[str], interface_file: Path, output_xml: Path) -> Path:
        """Execute swig -xml -c++ -I... interface.i -o output_xml.

        Returns the path to the generated XML file.
        """
        cmd_env = os.environ.copy()

        if self.use_module:
            # PTH118: Use Path / operator instead of os.path.join?
            # swig.BIN_DIR is a string, so we construct a Path.
            executable_path = Path(swig.BIN_DIR) / "swig"
            if not executable_path.exists() and os.name == "nt":
                executable_path = executable_path.with_suffix(".exe")

            executable = str(executable_path)

            # Merge SWIG lib env
            cmd_env.update(swig.SWIG_LIB_ENV)
            cmd = [executable]

            # Instead of using the real python SWIG library (which causes directive errors in -xml mode),
            # we inject our own mocks that define the minimal types needed.
            # Locate mocks relative to this file: .../core/runner.py -> .../mocks
            mocks_dir = Path(__file__).parent.parent / "mocks"
            if mocks_dir.exists():
                cmd.append(f"-I{mocks_dir}")
        else:
            if not shutil.which(self.swig_path):
                msg = f"SWIG executable not found at '{self.swig_path}'. Please install SWIG."
                raise FileNotFoundError(msg)
            cmd = [self.swig_path]
            # Also try to find mocks if not using module?
            # Assuming installed package structure is consistent.
            mocks_dir = Path(__file__).parent.parent / "mocks"
            if mocks_dir.exists():
                cmd.append(f"-I{mocks_dir}")

        # Note: -xml and -python cannot be used together.
        # We use -xml to get the AST.
        # We DO NOT use -DSWIGPYTHON because it triggers %pythoncode and other implementation-specific
        # directives that crash the XML parser or are irrelevant for the AST.
        # We rely on our config and TypeManager to bridge the gap.
        cmd.extend(["-xml", "-c++"])

        # Output file
        cmd.extend(["-o", str(output_xml)])

        for inc in includes:
            cmd.append(f"-I{inc}")

        # Create a temporary wrapper file to inject preamble
        preamble = """
%define apply_cpptypes(x...)
%enddef
%define pythoncode(x...)
%enddef
"""
        # We include the original file
        # We must escape backslashes for SWIG string if on Windows, but pathlib handles forward slash usually.
        # SWIG %include expects "path".
        abs_interface = interface_file.resolve().as_posix()
        preamble += f'%include "{abs_interface}"\n'

        with tempfile.NamedTemporaryFile(mode="w", suffix=".i", delete=False) as tmp:
            tmp.write(preamble)
            tmp_path = Path(tmp.name)

        cmd.append(str(tmp_path))


        # Execute
        try:
            subprocess.run(cmd, capture_output=True, text=True, check=True, env=cmd_env)  # noqa: S603

            if output_xml.exists():
                return output_xml
            msg = "SWIG did not produce output file."
            raise RuntimeError(msg)
        except subprocess.CalledProcessError as e:
            msg = f"SWIG failed:\n{e.stderr}"
            raise RuntimeError(msg) from e
        finally:
            if tmp_path.exists():
                tmp_path.unlink()
