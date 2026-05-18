"""Type normalization and mapping system."""

import re

from .config import Config


class TypeManager:
    """Manages C++ to Python type conversions based on configuration."""

    def __init__(self, config: Config) -> None:
        """Initialize with configuration."""
        self.config = config
        self._smart_ptr_regex = self._build_smart_ptr_regex()
        self._swig_prefix_regex = re.compile(r"([pqra](\([^)]*\))?\.)")

    def _build_smart_ptr_regex(self) -> re.Pattern:
        patterns = [re.escape(ptr) for ptr in self.config.smart_pointers]
        return re.compile(rf"^(?:{'|'.join(patterns)})\s*<(.+)>$")

    def normalize_type(self, cpp_type: str) -> str:
        """Normalize a C++ type string to a valid Python type hint."""
        cpp_type = self._clean_cpp_type(cpp_type.strip())

        if match := self._smart_ptr_regex.match(cpp_type):
            return self.normalize_type(match.group(1))

        if mapped := self._resolve_typedefs(cpp_type):
            return mapped

        if container := self._resolve_containers(cpp_type):
            return container

        if template := self._resolve_general_template(cpp_type):
            return template

        py_type = cpp_type.replace("::", ".")
        if self.config.module_name and py_type.startswith(self.config.module_name + "."):
            py_type = py_type[len(self.config.module_name) + 1 :]
        return py_type

    def to_python(self, cpp_type_str: str) -> str:
        """Public interface to convert a C++ type string to a Python type hint."""
        return self.normalize_type(cpp_type_str)

    def _clean_cpp_type(self, cpp_type: str) -> str:
        while True:
            new_type = self._swig_prefix_regex.sub("", cpp_type)
            if new_type == cpp_type:
                break
            cpp_type = new_type

        cpp_type = cpp_type.replace("const ", "").replace("volatile ", "").strip()
        while cpp_type and (cpp_type.endswith(("&", "*"))):
            cpp_type = cpp_type[:-1].strip()
        while cpp_type.startswith("(") and cpp_type.endswith(")"):
            cpp_type = cpp_type[1:-1].strip()

        return (
            cpp_type.replace(" <", "<")
            .replace("< ", "<")
            .replace(" >", ">")
            .replace("> ", ">")
            .replace(" ,", ",")
            .replace(", ", ",")
        )

    def _resolve_typedefs(self, cpp_type: str) -> str | None:
        if cpp_type in self.config.type_map:
            return self.config.type_map[cpp_type]

        if self.config.module_name:
            namespaced = f"{self.config.module_name}::{cpp_type}"
            if namespaced in self.config.type_map:
                return self.config.type_map[namespaced]

        basic_types = {
            "int": "int",
            "long": "int",
            "short": "int",
            "unsigned int": "int",
            "unsigned long": "int",
            "long long": "int",
            "unsigned long long": "int",
            "double": "float",
            "float": "float",
            "char": "str",
            "void": "None",
            "bool": "bool",
        }
        return basic_types.get(cpp_type)

    def _resolve_containers(self, cpp_type: str) -> str | None:
        for cpp_container, py_abc in self.config.containers.items():
            prefix = cpp_container + "<"
            if cpp_type.startswith(prefix) and cpp_type.endswith(">") and (
                self._get_matching_bracket_index(cpp_type, len(cpp_container))
                == len(cpp_type) - 1
            ):
                inner = cpp_type[len(prefix) : -1].strip()
                args = [
                    self.normalize_type(a) for a in self._split_template_args(inner)
                ]
                return f"{py_abc}[{', '.join(args)}]"
        return None

    def _get_matching_bracket_index(self, text: str, start_index: int) -> int:
        depth = 0
        for i in range(start_index, len(text)):
            if text[i] == "<":
                depth += 1
            elif text[i] == ">":
                depth -= 1
                if depth == 0:
                    return i
        return -1

    def _resolve_general_template(self, cpp_type: str) -> str | None:
        if "<" in cpp_type and cpp_type.endswith(">"):
            idx = cpp_type.find("<")
            base = self.normalize_type(cpp_type[:idx].strip())
            args = [
                self.normalize_type(a)
                for a in self._split_template_args(cpp_type[idx + 1 : -1].strip())
            ]
            return f"{base}[{', '.join(args)}]"
        return None

    def _split_template_args(self, args: str) -> list[str]:
        """Split template arguments by comma, respecting nested brackets and parens."""
        parts, current, depth, p_depth = [], [], 0, 0
        for char in args:
            depth += (char == "<") - (char == ">")
            p_depth += (char == "(") - (char == ")")

            if char == "," and depth == 0 and p_depth == 0:
                parts.append("".join(current).strip())
                current = []
            else:
                current.append(char)
        if current:
            parts.append("".join(current).strip())
        return parts
