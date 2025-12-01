
import contextlib

import swig

try:
    # Try to run swig -version
    # Does it take a list? or string?
    # Usually wrappers mimic subprocess.run or just main()
    # Let's try passing a list of args.
    # Note: The first arg in argv is usually the program name, but libraries might vary.
    swig.swig(["-version"])
except Exception:
    pass

with contextlib.suppress(Exception):
    swig.swig("-version")
