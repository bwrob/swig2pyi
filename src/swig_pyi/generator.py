"""Logic for generating .pyi content."""

import datetime
import re
from collections import defaultdict
import keyword
from .models import Class, Declaration, Function, Parameter

# A simple type mapping from C++ to Python
CPP_TO_PY_TYPE_MAP = {
    "Natural": "int",
    "Real": "float",
    "Size": "int",
    "Integer": "int",
    "Rate": "float",
    "Spread": "float",
    "Volatility": "float",
    "Time": "float",
    "InterestRate": "float", # Add InterestRate here
    "bool": "bool",
    "std::string": "str",
    "void": "None",
}

CPP_TO_PY_DEFAULT_MAP = {
    "Date()": "Date()",
}


def _map_cpp_type_to_py(cpp_type: str) -> str:
    original_cpp_type = cpp_type # Keep original for recursive calls

    # Handle std::vector<T> -> list[mapped_T]
    vector_match = re.match(r"std::vector<(.*?)>", cpp_type)
    if vector_match:
        inner_type = vector_match.group(1).strip()
        mapped_inner_type = _map_cpp_type_to_py(inner_type)  # Recursive call
        return f"list[{mapped_inner_type}]"
    
    # Handle ext::shared_ptr<T> -> mapped_T
    shared_ptr_match = re.match(r"ext::shared_ptr<(.*?)>", cpp_type)
    if shared_ptr_match:
        inner_type = shared_ptr_match.group(1).strip()
        return _map_cpp_type_to_py(inner_type)  # Recursive call

    # Remove const and & only for basic types after complex type handling
    cpp_type = cpp_type.replace("const ", "").replace("&", "").strip()
    
    # Handle specific types
    if cpp_type == "Period":
        return "datetime.timedelta"

    # Handle other types via map
    return CPP_TO_PY_TYPE_MAP.get(cpp_type, cpp_type)


def _format_parameters(parameters: list[Parameter]) -> str:
    parts = []
    for p in parameters:
        py_type = _map_cpp_type_to_py(p.type)
        if p.name:
            if p.default_value:
                if p.default_value == "Leg()":
                    parts.append(f"{p.name}: {py_type} = []")
                else:
                    py_default = CPP_TO_PY_DEFAULT_MAP.get(
                        p.default_value, p.default_value
                    )
                    parts.append(f"{p.name}: {py_type} = {py_default}")
            else:
                parts.append(f"{p.name}: {py_type}")
        else:
            parts.append(py_type)
    return ", ".join(parts)


def generate_pyi(declarations: list[Declaration]) -> str:
    lines = ["from typing import overload"]

    for decl in declarations:
        if isinstance(decl, Class):
            lines.append(f"class {decl.name}:")
            if not decl.methods:
                lines.append("    ...")
            
            # Group methods by name to handle overloads
            methods_by_name = defaultdict(list)
            for method in decl.methods:
                methods_by_name[method.name].append(method)

            for name, method_group in methods_by_name.items():
                is_overloaded = len(method_group) > 1
                for method in method_group:
                    if is_overloaded:
                        lines.append("    @overload")

                    method_name = method.name
                    return_type = _map_cpp_type_to_py(method.return_type)

                    if method_name == decl.name:
                        method_name = "__init__"
                        return_type = "None"
                    elif keyword.iskeyword(method_name): # Handle Python keywords
                        method_name += "_"
                    
                    params = _format_parameters(method.parameters)
                    self_param = "self"  # __init__ always has self, no special handling here for now
                    
                    # Handle self parameter and empty parameter list
                    if not params:
                        formatted_params = self_param
                    else:
                        formatted_params = f"{self_param}, {params}"

                    lines.append(
                        f"    def {method_name}({formatted_params}) -> {return_type}: ..."
                    )
            lines.append("")
        elif isinstance(decl, Function):
            function_name = decl.name
            if keyword.iskeyword(function_name): # Handle Python keywords
                function_name += "_"
            params = _format_parameters(decl.parameters)
            return_type = _map_cpp_type_to_py(decl.return_type)
            lines.append(f"def {function_name}({params}) -> {return_type}: ...")
            lines.append("")

    return "\n".join(lines)

