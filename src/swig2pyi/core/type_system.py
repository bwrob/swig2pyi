"""Type normalization and mapping system."""

from __future__ import annotations

import re
from typing import TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from .ast_models import Class, Top
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
        "unsigned short": "int",
        "unsigned char": "int",
        "signed char": "int",
        "long double": "float",
        "double": "float",
        "float": "float",
        "char": "str",
        "void": "None",
        "bool": "bool",
        "size_t": "int",
        "std::size_t": "int",
        "ptrdiff_t": "int",
        "std::ptrdiff_t": "int",
        "wchar_t": "str",
        "char16_t": "str",
        "char32_t": "str",
        "int8_t": "int",
        "uint8_t": "int",
        "int16_t": "int",
        "uint16_t": "int",
        "int32_t": "int",
        "uint32_t": "int",
        "int64_t": "int",
        "uint64_t": "int",
        "std::int8_t": "int",
        "std::uint8_t": "int",
        "std::int16_t": "int",
        "std::uint16_t": "int",
        "std::int32_t": "int",
        "std::uint32_t": "int",
        "std::int64_t": "int",
        "std::uint64_t": "int",
    }

    DEFAULT_TEMPLATE_ARG_COUNTS: ClassVar[dict[str, int]] = {
        "list": 1,
        "set": 1,
        "dict": 2,
        "tuple": 2,
        "Sequence": 1,
        "Iterable": 1,
        "Iterator": 1,
        "Optional": 1,
        "Generic": 1,
        "Handle": 1,
        "RelinkableHandle": 1,
    }

    def __init__(
        self,
        config: Config,
        enums: set[str] | None = None,
        top: Top | None = None,
    ) -> None:
        """Initialize with configuration."""
        self.config = config
        if top is not None:
            self.enums = _collect_enums(top)
        else:
            self.enums = enums or set()
        self.needed_imports: set[str] = set()
        self.cpp_to_py_class_names: dict[str, str] = {}
        self.py_class_to_cpp_types: dict[str, str] = {}
        self._smart_ptr_regex: re.Pattern[str] = self._build_smart_ptr_regex()
        self._swig_prefix_regex: re.Pattern[str] = re.compile(r"([pqra](\([^)]*\))?\.)")
        self._type_map: dict[str, str] = {
            self.clean_cpp_type(k): v for k, v in self.config.type_map.items()
        }
        self._containers: dict[str, str] = {
            self.clean_cpp_type(k): v for k, v in self.config.containers.items()
        }
        self.typedefs: dict[str, str] = {}
        if top is not None and top.module is not None:
            self.typedefs = {
                self.clean_cpp_type(k): self.clean_cpp_type(v)
                for k, v in top.module.typedefs.items()
            }

    def _build_smart_ptr_regex(self) -> re.Pattern[str]:
        patterns = [re.escape(ptr) for ptr in self.config.smart_pointers]
        if not patterns:
            return re.compile(r"$.^")  # Match nothing
        return re.compile(rf"^(?:{'|'.join(patterns)})\s*<(.+)>$")

    def normalize_type(
        self,
        cpp_type: str,
        *,
        bypass_mapping: bool = False,
        visited: set[str] | None = None,
    ) -> str:
        """Normalize a C++ type string to a valid Python type hint."""
        cpp_type = cpp_type.strip()

        if visited is None:
            visited = set()

        if cpp_type in visited:
            return cpp_type.replace("::", ".")

        # Create a new set branch to allow independent resolving paths
        # but prevent loop cycles.
        visited = visited | {cpp_type}

        basic_cleaned = self._clean_basic(cpp_type)
        if match := self._smart_ptr_regex.match(basic_cleaned):
            return self.normalize_type(
                match.group(1), bypass_mapping=bypass_mapping, visited=visited
            )

        cpp_type = self.clean_cpp_type(cpp_type)

        typedef_res = self._resolve_typedefs(cpp_type, visited=visited)
        if typedef_res is not None:
            return typedef_res

        if not bypass_mapping and cpp_type in self.cpp_to_py_class_names:
            return self.cpp_to_py_class_names[cpp_type]

        result = (
            self._resolve_containers(
                cpp_type, bypass_mapping=bypass_mapping, visited=visited
            )
            or self._resolve_general_template(
                cpp_type, bypass_mapping=bypass_mapping, visited=visited
            )
            or self._resolve_scopes(
                cpp_type, bypass_mapping=bypass_mapping, visited=visited
            )
        )
        if result is not None:
            return result

        return self._clean_prefix(cpp_type)

    def _clean_prefix(self, cpp_type: str) -> str:
        py_type = cpp_type.replace("::", ".")
        prefix = self.config.module_name + "." if self.config.module_name else ""
        if prefix and py_type.startswith(prefix):
            return py_type[len(prefix) :]
        return py_type

    def to_python(
        self,
        cpp_type_str: str,
        *,
        bypass_mapping: bool = False,
        is_parameter: bool = False,
    ) -> str:
        """Public interface to convert a C++ type string to a Python type hint."""
        resolved = self.normalize_type(cpp_type_str, bypass_mapping=bypass_mapping)
        if is_parameter:
            resolved = self._to_python_parameter(resolved, cpp_type_str)

        self.record_imports(resolved)
        return resolved

    def _to_python_parameter(self, resolved: str, cpp_type_str: str) -> str:
        if resolved in self.config.parameter_relaxation:
            return self.config.parameter_relaxation[resolved]

        underlying = self.py_class_to_cpp_types.get(resolved, cpp_type_str)
        generic = self.normalize_type(underlying, bypass_mapping=True)
        param_type = self._make_parameter_type(generic)
        if param_type == resolved:
            return resolved

        if resolved.startswith(("list[", "Sequence[", "Union[", "Optional[")):
            return param_type

        self.needed_imports.add("Union")
        return f"Union[{resolved}, {param_type}]"

    def record_imports(self, resolved: str) -> None:
        """Record necessary imports for the resolved Python type."""
        for sym in (
            "Any",
            "Optional",
            "Union",
            "Callable",
            "Sequence",
            "Iterable",
            "Iterator",
            "Final",
        ):
            if re.search(rf"\b{sym}\b", resolved):
                self.needed_imports.add(sym)
        if "collections.abc" in resolved:
            self.needed_imports.add("collections.abc")
        if "typing." in resolved:
            self.needed_imports.add("typing")

    def _make_parameter_type(self, type_str: str) -> str:
        if type_str.startswith("list[") and type_str.endswith("]"):
            inner = type_str[5:-1]
            return f"Sequence[{self._make_parameter_type(inner)}]"
        if type_str.startswith("tuple[") and type_str.endswith("]"):
            inner = type_str[6:-1]
            args = self._split_template_args(inner)
            return f"tuple[{', '.join(self._make_parameter_type(a) for a in args)}]"
        if type_str.startswith("Union[") and type_str.endswith("]"):
            inner = type_str[6:-1]
            args = self._split_template_args(inner)
            return f"Union[{', '.join(self._make_parameter_type(a) for a in args)}]"
        if type_str.startswith("Optional[") and type_str.endswith("]"):
            inner = type_str[9:-1]
            return f"Optional[{self._make_parameter_type(inner)}]"
        return type_str

    def _clean_basic(self, cpp_type: str) -> str:
        while True:
            new_type = self._swig_prefix_regex.sub("", cpp_type)
            if new_type == cpp_type:
                break
            cpp_type = new_type

        cpp_type = re.sub(r"\b(const|volatile)\b\s*", "", cpp_type).strip()
        while cpp_type and (cpp_type.endswith(("&", "*"))):
            cpp_type = cpp_type[:-1].strip()
        cpp_type = cpp_type.replace("(", "").replace(")", "")

        return (
            cpp_type.replace(" <", "<")
            .replace("< ", "<")
            .replace(" >", ">")
            .replace("> ", ">")
            .replace(" ,", ",")
            .replace(", ", ",")
        )

    def clean_cpp_type(self, cpp_type: str) -> str:
        """Clean and normalize C++ type string consistently."""
        cpp_type = self._clean_basic(cpp_type)
        for ns in self.config.namespaces_to_remove:
            cpp_type = cpp_type.replace(ns, "")
        return cpp_type

    def _resolve_typedefs(
        self, cpp_type: str, visited: set[str] | None = None
    ) -> str | None:
        if visited is None:
            visited = set()
        if cpp_type.endswith(("::size_type", ".size_type")):
            return "int"

        # 1. Resolve from static type map
        mapped = self._lookup_type_map(cpp_type)
        if mapped is not None:
            return mapped

        # 2. Resolve from XML parsed typedefs
        resolved = self._lookup_typedefs(cpp_type, visited=visited)
        if resolved is not None:
            return resolved

        return self.BASIC_TYPES.get(cpp_type)

    def _lookup_type_map(self, cpp_type: str) -> str | None:
        """Look up the C++ type in the static type map config."""
        if cpp_type in self._type_map:
            return self._type_map[cpp_type]

        if self.config.module_name:
            namespaced = f"{self.config.module_name}::{cpp_type}"
            cleaned = self.clean_cpp_type(namespaced)
            if cleaned in self._type_map:
                return self._type_map[cleaned]
        return None

    def _lookup_typedefs(
        self, cpp_type: str, visited: set[str] | None = None
    ) -> str | None:
        """Look up the C++ type in parsed typedefs and recursively normalize."""
        if visited is None:
            visited = set()
        if cpp_type in self.typedefs:
            underlying = self.typedefs[cpp_type]
            if underlying != cpp_type:
                return self.normalize_type(underlying, visited=visited)

        if self.config.module_name:
            namespaced = f"{self.config.module_name}::{cpp_type}"
            cleaned = self.clean_cpp_type(namespaced)
            if cleaned in self.typedefs:
                underlying = self.typedefs[cleaned]
                if underlying != cleaned:
                    return self.normalize_type(underlying, visited=visited)
        return None

    def _get_template_arg_limit(self, template_name: str) -> int | None:
        base_name = template_name.rsplit(".", maxsplit=1)[-1]
        if base_name in self.config.template_arg_counts:
            return self.config.template_arg_counts[base_name]
        return self.DEFAULT_TEMPLATE_ARG_COUNTS.get(base_name)

    def _resolve_containers(
        self,
        cpp_type: str,
        *,
        bypass_mapping: bool = False,
        visited: set[str] | None = None,
    ) -> str | None:
        if visited is None:
            visited = set()
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
                    self.normalize_type(
                        a, bypass_mapping=bypass_mapping, visited=visited
                    )
                    for a in self._split_template_args(inner)
                ]
                limit = self._get_template_arg_limit(py_abc)
                if limit is not None:
                    args = args[:limit]
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

    def _resolve_scopes(
        self,
        cpp_type: str,
        *,
        bypass_mapping: bool = False,
        visited: set[str] | None = None,
    ) -> str | None:
        if visited is None:
            visited = set()
        scopes = self._split_scopes(cpp_type)
        if len(scopes) <= 1:
            return None

        if self.config.module_name and scopes[0] == self.config.module_name:
            scopes = scopes[1:]

        if len(scopes) == 1:
            return self.normalize_type(
                scopes[0], bypass_mapping=bypass_mapping, visited=visited
            )

        resolved_components: list[str] = [
            self._resolve_single_scope_component(
                i, s, len(scopes), bypass_mapping=bypass_mapping, visited=visited
            )
            for i, s in enumerate(scopes)
        ]
        return ".".join(resolved_components)

    def _resolve_single_scope_component(
        self,
        i: int,
        s: str,
        scopes_len: int,
        *,
        bypass_mapping: bool,
        visited: set[str],
    ) -> str:
        if i < scopes_len - 1 and "<" in s:
            s = s.split("<", 1)[0].strip()
        return self.normalize_type(s, bypass_mapping=bypass_mapping, visited=visited)

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

    def _resolve_general_template(
        self,
        cpp_type: str,
        *,
        bypass_mapping: bool = False,
        visited: set[str] | None = None,
    ) -> str | None:
        if visited is None:
            visited = set()
        if "<" in cpp_type and cpp_type.endswith(">"):
            idx = cpp_type.find("<")
            base = self.normalize_type(
                cpp_type[:idx].strip(), bypass_mapping=bypass_mapping, visited=visited
            )
            inner = cpp_type[idx + 1 : -1].strip()
            inner = self._clean_template_inner(inner)
            args = [
                self.normalize_type(a, bypass_mapping=bypass_mapping, visited=visited)
                for a in self._split_template_args(inner)
            ]
            limit = self._get_template_arg_limit(base)
            if limit is not None:
                args = args[:limit]
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


def _collect_enums(top: Top) -> set[str]:
    """Collect all enum names from the AST recursively."""
    enums: set[str] = set()
    if not top.module:
        return enums

    # Module-level enums
    for enum in top.module.enums:
        name = enum.name.split("::")[-1]
        enums.add(name)

    # Class-level enums
    def visit_class(cls: Class, prefix: str = "") -> None:
        cls_name = cls.name.split("::")[-1]
        current_prefix = f"{prefix}{cls_name}." if prefix else f"{cls_name}."
        for enum in cls.enums:
            enum_name = enum.name.split("::")[-1]
            enums.add(current_prefix + enum_name)
            enums.add(enum_name)
        for sub_cls in cls.classes:
            visit_class(sub_cls, current_prefix)

    for cls in top.module.classes:
        visit_class(cls)

    return enums
