"""Logic for parsing SWIG .i files."""

import re
from pathlib import Path


def parse_module_name(swig_file: Path) -> str | None:
    """Parse a SWIG interface file to extract the module name.

    Args:
    ----
        swig_file: The path to the SWIG interface file.

    Returns:
    -------
        The name of the module, or None if not found.

    """
    module_pattern = re.compile(r"^\s*%module\s+(.+)$")
    with swig_file.open("r") as f:
        for line in f:
            match = module_pattern.match(line)
            if match:
                return match.group(1).strip()
    return None
