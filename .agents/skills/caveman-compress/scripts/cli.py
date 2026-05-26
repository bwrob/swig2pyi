#!/usr/bin/env python3
"""Caveman Compress CLI.

Usage:
    caveman <filepath>
"""

import contextlib
import sys

# Force UTF-8 on stdout/stderr before any code can print. Windows consoles
# default to cp1252 and crash on the ❌ glyphs in error/validation branches,
# masking the real error and leaving the user with a half-compressed file.
for _stream in (sys.stdout, sys.stderr):
    reconfigure = getattr(_stream, "reconfigure", None)
    if callable(reconfigure):
        with contextlib.suppress(Exception):
            reconfigure(encoding="utf-8", errors="replace")

from pathlib import Path

from .compress import compress_file
from .detect import detect_file_type, should_compress


def print_usage() -> None:
    pass


def main() -> None:
    if len(sys.argv) != 2:
        print_usage()
        sys.exit(1)

    filepath = Path(sys.argv[1])

    # Check file exists
    if not filepath.exists():
        sys.exit(1)

    if not filepath.is_file():
        sys.exit(1)

    filepath = filepath.resolve()

    # Detect file type
    detect_file_type(filepath)

    # Check if compressible
    if not should_compress(filepath):
        sys.exit(0)

    try:
        success = compress_file(filepath)

        if success:
            filepath.with_name(filepath.stem + ".original.md")
            sys.exit(0)
        else:
            sys.exit(2)

    except KeyboardInterrupt:
        sys.exit(130)

    except Exception:
        sys.exit(1)


if __name__ == "__main__":
    main()
