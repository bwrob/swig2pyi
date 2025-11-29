import swig
import sys

print(f"SWIG module dir: {dir(swig)}")
print(f"SWIG function: {swig.swig}")

try:
    # Try to run swig -version
    # Does it take a list? or string? 
    # Usually wrappers mimic subprocess.run or just main()
    # Let's try passing a list of args.
    # Note: The first arg in argv is usually the program name, but libraries might vary.
    print("--- Running swig.swig(['-version']) ---")
    swig.swig(["-version"])
except Exception as e:
    print(f"Error with list: {e}")

try:
    print("--- Running swig.swig('-version') ---")
    swig.swig("-version")
except Exception as e:
    print(f"Error with string: {e}")
