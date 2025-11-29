import shutil
import subprocess
import os
from pathlib import Path
from typing import List

try:
    import swig
    _SWIG_MODULE_AVAILABLE = True
except ImportError:
    _SWIG_MODULE_AVAILABLE = False

import tempfile

class SwigRunner:
    def __init__(self, swig_path: str = "swig"):
        self.swig_path = swig_path
        self.use_module = _SWIG_MODULE_AVAILABLE and swig_path == "swig"
        
        if not self.use_module and not shutil.which(self.swig_path):
             # We don't raise immediately to allow instantiation, but run will fail.
             pass

    def run(self, includes: List[str], interface_file: Path) -> str:
        """
        Executes swig -xml -python -c++ -I... interface.i
        Returns the XML output as a string.
        """
        cmd_env = os.environ.copy()
        
        if self.use_module:
            executable = os.path.join(swig.BIN_DIR, "swig")
            if not os.path.exists(executable) and os.name == 'nt':
                 executable += ".exe"
            
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
                raise FileNotFoundError(f"SWIG executable not found at '{self.swig_path}'. Please install SWIG.")
            cmd = [self.swig_path]
            # Also try to find mocks if not using module?
            # Assuming installed package structure is consistent.
            mocks_dir = Path(__file__).parent.parent / "mocks"
            if mocks_dir.exists():
                cmd.append(f"-I{mocks_dir}")

        # Note: -xml and -python cannot be used together. 
        # We use -xml to get the AST, and -DSWIGPYTHON to simulate the Python target definitions.
        cmd.extend(["-xml", "-DSWIGPYTHON", "-c++"])
        
        for inc in includes:
            cmd.append(f"-I{inc}")
            
        # Create a temporary wrapper file to inject preamble
        # We define macros to silence unsupported directives from python.swg
        preamble = """
%define apply_cpptypes(x...)
%enddef
%define fragment(x...)
%enddef
%define typemap(x...)
%enddef
%define feature(x...)
%enddef
"""
        # Note: We are ignoring typemaps/features because they cause parsing errors in -xml mode 
        # or are irrelevant for AST generation. 
        # However, the user wanted %feature("autodoc"). 
        # If ignoring feature silences autodoc, that's bad.
        # But we can't easily parse them if they use unknown directives.
        # Let's try to ONLY silence known bad directives.
        
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
        
        with tempfile.NamedTemporaryFile(mode='w', suffix='.i', delete=False) as tmp:
            tmp.write(preamble)
            tmp_path = tmp.name
            
        cmd.append(tmp_path)
        
        print(f"DEBUG: SWIG command: {' '.join(cmd)}")
        
        # Execute
        try:
            result = subprocess.run(
                cmd, 
                capture_output=True, 
                text=True, 
                check=True,
                env=cmd_env
            )
            return result.stdout
        except subprocess.CalledProcessError as e:
            raise RuntimeError(f"SWIG failed:\n{e.stderr}") from e
        finally:
            if os.path.exists(tmp_path):
                os.unlink(tmp_path)
