"""Logic for parsing SWIG .i files."""

import re
from pathlib import Path

from .models import SwigFile


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


def get_included_files(content: str) -> list[str]:
    """
    Parse a SWIG interface file to extract the included files.

    Args:
        content: The content of the SWIG interface file.

    Returns:
        A list of included file names.
    """
    include_pattern = re.compile(r'^\s*%include\s+["<]?([\w\.]+)[">]?\s*$', re.MULTILINE)
    return [match.strip() for match in include_pattern.findall(content)]


def resolve_includes(entry_file: Path) -> list[SwigFile]:
    """
    Recursively resolve all included files from a given entry file.

    Args:
        entry_file: The path to the main SWIG interface file.

    Returns:
        A list of SwigFile objects, representing all the files that make up the module.
    """
    files_to_process = [entry_file.resolve()]
    processed_files: set[Path] = set()
    all_swig_files: list[SwigFile] = []

    while files_to_process:
        current_file_path = files_to_process.pop(0)

        # Ensure we don't process the same file multiple times
        if current_file_path in processed_files:
            continue
        processed_files.add(current_file_path) # Mark as processed before attempting to read

        try:
            content = current_file_path.read_text()
        except FileNotFoundError:
            # File not found, skip it entirely.
            continue

        included_file_names = get_included_files(content)

        base_dir = current_file_path.parent
        included_paths = [
            (base_dir / name).resolve() for name in included_file_names
        ]

        all_swig_files.append(
            SwigFile(
                path=current_file_path,
                includes=included_paths,
                content=content,
            ),
        )

        for path in included_paths:
            if path not in processed_files:
                files_to_process.append(path)

    return all_swig_files
