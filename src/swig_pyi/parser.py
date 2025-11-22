"""Logic for parsing SWIG .i files."""

import re
from pathlib import Path

from .models import Class, Declaration, Function, Parameter, SwigFile


def _parse_parameter_type_and_name(param_str: str) -> tuple[str, str | None]:
    param_str = param_str.strip()
    # Regex to find an identifier at the end, optionally preceded by * or &
    # This also handles template types, e.g., 'std::vector<int> someVec'
    # The name is assumed to be a valid C++ identifier.
    name_match = re.search(r"([a-zA-Z_]\w*)(?:\s*([*&]))?\s*$", param_str)
    if name_match:
        name = name_match.group(1)
        type_str = param_str[: name_match.start()].strip()

        # If there's an asterisk or ampersand after the name, include it in the name
        if name_match.group(2):
            name += name_match.group(2)

        # If the type is empty, it means the whole string was the name, e.g., "int"
        # In this case, the 'name' is actually the type, and there is no explicit name.
        if not type_str:
            return param_str, None  # Treat whole string as type, no explicit name
        return type_str, name

    # If no clear name is found, treat the whole string as the type, with
    # no explicit name
    return param_str, None


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
    """Parse a SWIG interface file to extract the included files.

    Args:
    ----
        content: The content of the SWIG interface file.

    Returns:
    -------
        A list of included file names.

    """
    include_pattern = re.compile(
        r'^\s*%include\s+["<]?([\w\.]+)[">]?\s*$',
        re.MULTILINE,
    )
    return [match.strip() for match in include_pattern.findall(content)]


def resolve_includes(entry_file: Path) -> list[SwigFile]:
    """Recursively resolve all included files from a given entry file.

    Args:
    ----
        entry_file: The path to the main SWIG interface file.

    Returns:
    -------
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
        processed_files.add(
            current_file_path
        )  # Mark as processed before attempting to read the file.

        try:
            content = current_file_path.read_text()
        except FileNotFoundError:
            # File not found, skip it entirely.
            continue

        included_file_names = get_included_files(content)

        base_dir = current_file_path.parent
        included_paths = [(base_dir / name).resolve() for name in included_file_names]

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
    """Parse a SWIG interface file to extract declarations.

    Args:
    ----
        content: The content of the SWIG interface file.

    Returns:
    -------
        A list of Declaration objects (Class or Function).

    """
    # Regex for class definitions
    class_pattern = re.compile(
        r"(?:%shared_ptr\(\w+\)\s*)?class\s+(\w+)(?:\s*:\s*public\s+\w+)?\s*\{(.*?)\};",
        re.DOTALL,
    )
    # Simplified regex for function definitions.
    function_pattern = re.compile(
        r"\s*(?:static\s+)?(?:const\s+)?([\w<>:*\s&]+)\s+"
        r"([\w]+)\s*\((.*?)\)\s*(const)?;",
        re.DOTALL,
    )

    declarations: list[Declaration] = []

    # Extract class matches
    class_matches = list(class_pattern.finditer(content))

    # Process classes and build non_class_content
    non_class_content_parts = []
    last_end = 0
    for class_match in class_matches:
        # Add content *before* the current class to non_class_content_parts
        non_class_content_parts.append(content[last_end : class_match.start()])

        # Parse the class
        class_name, class_body = class_match.groups()
        # Remove C++ comments, preprocessor directives, SWIG directives,
        # and access specifiers
        clean_class_body = class_body
        clean_class_body = re.sub(r"//.*$", "", clean_class_body, flags=re.MULTILINE)
        clean_class_body = re.sub(r"/\*.*?\*/", "", clean_class_body, flags=re.DOTALL)
        clean_class_body = re.sub(
            r"^\s*(#|%).*$",
            "",
            clean_class_body,
            flags=re.MULTILINE,
        )
        clean_class_body = re.sub(
            r"^\s*(public|private|protected):"
            r".*$",
            "",
            clean_class_body,
            flags=re.MULTILINE,
        )

        methods = []
        for method_match in function_pattern.finditer(clean_class_body):
            return_type, name, params_str, is_const = method_match.groups()
            parameters = []
            if params_str:
                for param in params_str.split(","):
                    param = param.strip()
                    param_type_and_name = param
                    default_value = None

                    # Check for default value
                    if "=" in param:
                        param_parts = param.split("=", 1)
                        param_type_and_name = param_parts[0].strip()
                        default_value = param_parts[1].strip()

                    param_type, param_name = _parse_parameter_type_and_name(
                        param_type_and_name
                    )

                    parameters.append(
                        Parameter(
                            name=param_name,
                            type=param_type,
                            default_value=default_value,
                        )
                    )
            methods.append(
                Function(
                    name=name,
                    parameters=parameters,
                    return_type=return_type.strip(),
                    is_const=bool(is_const),
                )
            )
        declarations.append(Class(name=class_name, methods=methods))

        # Update last_end to after the current class
        last_end = class_match.end()

    # Add any remaining content after the last class to non_class_content_parts
    non_class_content_parts.append(content[last_end:])
    non_class_content = "".join(non_class_content_parts)

    # Parse standalone functions from the content that had classes removed
    for func_match in function_pattern.finditer(non_class_content):
        return_type, name, params_str, is_const = func_match.groups()
        parameters = []
        if params_str:
            for param in params_str.split(","):
                param = param.strip()
                param_type_and_name = param
                default_value = None

                # Check for default value
                if "=" in param:
                    param_parts = param.split("=", 1)
                    param_type_and_name = param_parts[0].strip()
                    default_value = param_parts[1].strip()

                param_type, param_name = _parse_parameter_type_and_name(
                    param_type_and_name
                )

                parameters.append(
                    Parameter(
                        name=param_name, type=param_type, default_value=default_value
                    )
                )
        declarations.append(
            Function(
                name=name,
                parameters=parameters,
                return_type=return_type.strip(),
                is_const=bool(is_const),
            )
        )
    return declarations


def parse_swig_file(
    entry_file: Path,
) -> tuple[str | None, list[SwigFile], list[Declaration]]:
    """Parse a SWIG entry file and all its included files to extract module information and declarations.

    Args:
    ----
        entry_file: The path to the main SWIG interface file.

    Returns:
    -------
        A tuple containing:
            - The module name (str | None).
            - A list of SwigFile objects for the entry file and all its includes.
            - A list of Declaration objects (Class or Function) from all parsed files.

    """
    module_name = parse_module_name(entry_file)
    all_swig_files = resolve_includes(entry_file)

    all_declarations: list[Declaration] = []
    for swig_file in all_swig_files:
        declarations_in_file = parse_declarations(swig_file.content)
        all_declarations.extend(declarations_in_file)

    return module_name, all_swig_files, all_declarations
