"""Logic for parsing SWIG .i files."""

import re
from pathlib import Path
from typing import Union

from .models import Class, Function, Parameter, SwigFile

Declaration = Union[Class, Function]


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


def parse_declarations(content: str) -> list[Declaration]:
    """
    Parse a SWIG interface file to extract declarations.

    Args:
        content: The content of the SWIG interface file.

    Returns:
        A list of Declaration objects (Class or Function).
    """
    # Regex for class definitions
    class_pattern = re.compile(r"class\s+(\w+)\s*\{(.*?)\};", re.DOTALL)
    # Simplified regex for function definitions.
    function_pattern = re.compile(
        r"\s*(?:const\s+)?(?:static\s+)?([\w<>:*\s&]+?)\s+(\w+)\s*\(([^)]*)\);", re.MULTILINE
    )

    declarations: list[Declaration] = []
    
    # Extract class matches
    class_matches = list(class_pattern.finditer(content))
    
    # Process classes and build non_class_content
    non_class_content_parts = []
    last_end = 0
    for class_match in class_matches:
        # Add content *before* the current class to non_class_content_parts
        non_class_content_parts.append(content[last_end:class_match.start()])
        
        # Parse the class
        class_name, class_body = class_match.groups()
        # Remove C++ comments, preprocessor directives, SWIG directives, and access specifiers
        clean_class_body = class_body
        clean_class_body = re.sub(r'//.*$', '', clean_class_body, flags=re.MULTILINE)
        clean_class_body = re.sub(r'/\*.*?\*/', '', clean_class_body, flags=re.DOTALL)
        clean_class_body = re.sub(r'^\s*(#|%).*$', '', clean_class_body, flags=re.MULTILINE)
        clean_class_body = re.sub(r'^\s*(public|private|protected):.*$', '', clean_class_body, flags=re.MULTILINE)
        
        methods = []
        for method_match in function_pattern.finditer(clean_class_body):
            return_type, name, params_str = method_match.groups()
            parameters = []
            if params_str:
                for param in params_str.split(","):
                    param = param.strip()
                    parts = param.rsplit(" ", 1)
                    if len(parts) == 2:
                        param_type, param_name = parts
                        parameters.append(Parameter(name=param_name.strip(), type=param_type.strip()))
            methods.append(
                Function(name=name, parameters=parameters, return_type=return_type.strip())
            )
        declarations.append(Class(name=class_name, methods=methods))
        
        # Update last_end to after the current class
        last_end = class_match.end()

    # Add any remaining content after the last class to non_class_content_parts
    non_class_content_parts.append(content[last_end:])
    non_class_content = "".join(non_class_content_parts)

    # Parse standalone functions from the content that had classes removed
    for func_match in function_pattern.finditer(non_class_content):
        return_type, name, params_str = func_match.groups()
        parameters = []
        if params_str:
            for param in params_str.split(","):
                param = param.strip()
                parts = param.rsplit(" ", 1)
                if len(parts) == 2:
                    param_type, param_name = parts
                    parameters.append(Parameter(name=param_name.strip(), type=param_type.strip()))
        declarations.append(
            Function(name=name, parameters=parameters, return_type=return_type.strip())
        )

    return declarations
