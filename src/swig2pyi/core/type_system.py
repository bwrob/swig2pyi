"""Type normalization and mapping system."""

import re
from typing import ClassVar

from .config import Config


class TypeManager:
    """Manages C++ to Python type conversions based on configuration."""

    BASIC_TYPES: ClassVar[dict[str, str]] = {
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

    def __init__(self, config: Config) -> None:
        """Initialize with configuration."""
        self.config = config
        self._smart_ptr_regex: re.Pattern[str] = self._build_smart_ptr_regex()
        self._swig_prefix_regex: re.Pattern[str] = re.compile(r"([pqra](\([^)]*\))?\.)")
        self._type_map: dict[str, str] = {
            self._clean_cpp_type(k): v for k, v in self.config.type_map.items()
        }
        self._containers: dict[str, str] = {
            self._clean_cpp_type(k): v for k, v in self.config.containers.items()
        }

    def _build_smart_ptr_regex(self) -> re.Pattern[str]:
        patterns = [re.escape(ptr) for ptr in self.config.smart_pointers]
        if not patterns:
            return re.compile(r"$.^")  # Match nothing
        return re.compile(rf"^(?:{'|'.join(patterns)})\s*<(.+)>$")

    def normalize_type(self, cpp_type: str) -> str:
        """Normalize a C++ type string to a valid Python type hint."""
        cpp_type = cpp_type.strip()

        basic_cleaned = self._clean_basic(cpp_type)
        if match := self._smart_ptr_regex.match(basic_cleaned):
            return self.normalize_type(match.group(1))

        cpp_type = self._clean_cpp_type(cpp_type)

        if mapped := self._resolve_typedefs(cpp_type):
            return mapped

        if container := self._resolve_containers(cpp_type):
            return container

        if template := self._resolve_general_template(cpp_type):
            return template

        if resolved_scope := self._resolve_scopes(cpp_type):
            return resolved_scope

        py_type = cpp_type.replace("::", ".")
        prefix = self.config.module_name + "." if self.config.module_name else ""
        if prefix and py_type.startswith(prefix):
            py_type = py_type[len(prefix) :]
        return py_type

    def to_python(self, cpp_type_str: str) -> str:
        """Public interface to convert a C++ type string to a Python type hint."""
        return self.normalize_type(cpp_type_str)

    def _clean_basic(self, cpp_type: str) -> str:
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

    def _clean_cpp_type(self, cpp_type: str) -> str:
        cpp_type = self._clean_basic(cpp_type)
        for ns in self.config.namespaces_to_remove:
            cpp_type = cpp_type.replace(ns, "")
        return cpp_type

    def _resolve_typedefs(self, cpp_type: str) -> str | None:
        if cpp_type in self._type_map:
            return self._type_map[cpp_type]

        if self.config.module_name:
            namespaced = f"{self.config.module_name}::{cpp_type}"
            cleaned_namespaced = self._clean_cpp_type(namespaced)
            if cleaned_namespaced in self._type_map:
                return self._type_map[cleaned_namespaced]

        return self.BASIC_TYPES.get(cpp_type)

    def _resolve_containers(self, cpp_type: str) -> str | None:
        for cpp_container, py_abc in self._containers.items():
            prefix = cpp_container + "<"
            if (
                cpp_type.startswith(prefix)
                and cpp_type.endswith(">")
                and (
                    self._get_matching_bracket_index(cpp_type, len(cpp_container))
                    == len(cpp_type) - 1
                )
            ):
                inner = cpp_type[len(prefix) : -1].strip()
                inner = self._clean_template_inner(inner)
                args = [
                    self.normalize_type(a) for a in self._split_template_args(inner)
                ]
                return f"{py_abc}[{', '.join(args)}]"
        return None

    def _clean_template_inner(self, inner: str) -> str:
        inner = inner.strip()
        while inner.startswith("(") and inner.endswith(")"):
            matching_idx = self._find_matching_paren_index(inner)
            if matching_idx == len(inner) - 1:
                inner = inner[1:-1].strip()
            else:
                break
        return inner

    def _resolve_scopes(self, cpp_type: str) -> str | None:
        scopes = self._split_scopes(cpp_type)
        if len(scopes) > 1:
            if self.config.module_name and scopes[0] == self.config.module_name:
                scopes = scopes[1:]
            if len(scopes) > 1:
                return ".".join(self.normalize_type(s) for s in scopes)
            if len(scopes) == 1:
                return self.normalize_type(scopes[0])
        return None

    def _find_matching_paren_index(self, text: str) -> int:
        depth = 0
        for i, char in enumerate(text):
            if char == "(":
                depth += 1
            elif char == ")":
                depth -= 1
                if depth == 0:
                    return i
        return -1

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
            inner = cpp_type[idx + 1 : -1].strip()
            inner = self._clean_template_inner(inner)
            args = [self.normalize_type(a) for a in self._split_template_args(inner)]
            return f"{base}[{', '.join(args)}]"
        return None

    def _split_template_args(self, args: str) -> list[str]:
        """Split template arguments by comma, respecting nested brackets and parens."""
        parts: list[str] = []
        current: list[str] = []
        depth: int = 0
        p_depth: int = 0
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

    def _split_scopes(self, cpp_type: str) -> list[str]:
        """Split C++ namespaces and nested scopes.

        Respects nested brackets and parens.
        """
        parts: list[str] = []
        current: list[str] = []
        depth = 0
        p_depth = 0
        i = 0
        while i < len(cpp_type):
            char = cpp_type[i]

            # Check for ::
            if (
                char == ":"
                and i + 1 < len(cpp_type)
                and cpp_type[i + 1] == ":"
                and depth == 0
                and p_depth == 0
            ):
                parts.append("".join(current).strip())
                current = []
                i += 2
                continue

            depth += (char == "<") - (char == ">")
            p_depth += (char == "(") - (char == ")")
            current.append(char)
            i += 1

        if current:
            parts.append("".join(current).strip())
        return parts
