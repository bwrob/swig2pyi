"""Stub emitter for generating .pyi files."""

import re

from .parser import CDecl, Class, Constructor, Enum, Module, Parm, Top
from .type_system import TypeManager


class StubEmitter:
    """Generates Python type stubs from AST."""

    def __init__(self, type_manager: TypeManager) -> None:
        """Initialize with type manager."""
        self.tm = type_manager
        self.lines: list[str] = []
        self.indent_level = 0

    def indent(self) -> None:
        """Increment indentation level."""
        self.indent_level += 1

    def dedent(self) -> None:
        """Decrement indentation level."""
        self.indent_level = max(0, self.indent_level - 1)

    def write(self, text: str = "") -> None:
        """Write a line of text with current indentation."""
        line = "    " * self.indent_level + text
        self.lines.append(line.rstrip())

    def get_output(self) -> str:
        """Return the accumulated output as a string."""
        return "\n".join(self.lines)

    def emit(self, top: Top) -> None:
        """Generate the full stub output from the Top AST node."""
        self.write("import typing")
        self.write("from typing import Any, Optional, overload, Generic, TypeVar")
        self.write("import collections.abc")
        self.write("")
        self.write("_T = TypeVar('_T')")
        self.write("")
        for line in self.tm.config.extra_code:
            self.write(line)
        self.write("")
        if top.module:
            self.visit_module(top.module)

    def visit_module(self, module: Module) -> None:
        """Visit a module and emit its contents."""
        self._emit_module_enums(module)
        self._emit_module_functions(module)
        for cls in module.classes:
            self.visit_class(cls)

    def _emit_module_enums(self, module: Module) -> None:
        for enum in module.enums:
            self.visit_enum(enum)
            name = enum.name.split("::")[-1]
            for item in enum.items:
                self.write(f"{self._get_sanitized_name(item.name)}: {name}")
            self.write("")

    def _emit_module_functions(self, module: Module) -> None:
        func_groups = {}
        for func in module.cdecls:
            if func.kind != "function":
                continue
            if func.name.startswith("operator") or func.name in (
                "linkTo",
                "currentLink",
                "empty",
                "values",
            ):
                continue
            if self.should_skip_method(func):
                continue
            name = func.name.split("::")[-1]
            func_groups.setdefault(name, []).append(func)

        for name, group in func_groups.items():
            self.visit_function_group(name, group, is_method=False)

    def visit_enum(self, enum: Enum) -> None:
        """Emit a Python IntEnum from a C++ enum."""
        name = enum.name.split("::")[-1]
        self.write(f"class {name}(IntEnum):")
        self.indent()
        has_items = False
        for item in enum.items:
            item_name = self._get_sanitized_name(item.name)
            val_str = f" = {item.value}" if item.value is not None else ""
            self.write(f"{item_name}{val_str}")
            has_items = True
        if not has_items:
            self.write("pass")
        self.dedent()
        self.write("")

    def visit_class(self, cls: Class) -> None:
        """Emit a Python class from a C++ class/struct."""
        name = cls.name
        if name.startswith("std::") or "<" in name:
            return
        name = name.split("::")[-1]

        bases_str = self._get_bases_str(cls)
        self.write(f"class {name}{bases_str}:")
        self.indent()

        has_members = False
        if cls.enums:
            for enum in cls.enums:
                self.visit_enum(enum)
            has_members = True

        if cls.constructors:
            self.visit_constructor_group(cls.constructors)
            has_members = True

        prop_method_ids = self._emit_properties(cls)
        if prop_method_ids:
            has_members = True

        if self._emit_methods(cls, prop_method_ids):
            has_members = True

        if not has_members:
            self.write("pass")

        self.dedent()
        self.write("")

    def _get_bases_str(self, cls: Class) -> str:
        base_names = []
        if cls.bases:
            for b in cls.bases:
                base_names.extend(self._get_base_names(b))
        if cls.is_template:
            base_names.append("Generic[_T]")
        return f"({', '.join(base_names)})" if base_names else ""

    def _get_base_names(self, base_type: str) -> list[str]:
        names = []
        normalized_base = self.tm.to_python(base_type)
        names.append(normalized_base)
        match = re.search(
            r"(?:^|\.)(?:Handle|RelinkableHandle)\[(.+)\]$", normalized_base
        )
        if match:
            wrapped_type = match.group(1)
            if wrapped_type not in names:
                names.append(wrapped_type)
        return names

    def _emit_properties(self, cls: Class) -> set[int]:
        properties = self._collect_properties(cls)
        prop_method_ids = set()
        for prop_name, p_info in properties.items():
            if not p_info["get"]:
                continue
            self._emit_property(prop_name, p_info)
            prop_method_ids.add(id(p_info["get"]))
            if p_info["set"]:
                prop_method_ids.add(id(p_info["set"]))
        return prop_method_ids

    def _collect_properties(self, cls: Class) -> dict:
        properties = {}
        prefix_len = 3
        for method in cls.cdecls:
            if method.kind != "function":
                continue
            m_name = method.name.split("::")[-1]
            if len(m_name) <= prefix_len or not m_name[prefix_len].isupper():
                continue

            prop_name = m_name[prefix_len].lower() + m_name[prefix_len + 1 :]
            if m_name.startswith("get"):
                properties.setdefault(prop_name, {"get": None, "set": None})["get"] = (
                    method
                )
            elif m_name.startswith("set"):
                properties.setdefault(prop_name, {"get": None, "set": None})["set"] = (
                    method
                )
        return properties

    def _emit_property(self, prop_name: str, p_info: dict) -> None:
        ret_type = (
            self.tm.to_python(p_info["get"].type) if p_info["get"].type else "Any"
        )
        if ret_type == "void":
            ret_type = "None"
        self.write("@property")
        self.write(f"def {prop_name}(self) -> {ret_type}: ...")
        if p_info["set"]:
            self.write(f"@{prop_name}.setter")
            p_type = (
                self.tm.to_python(p_info["set"].parms[0].type)
                if p_info["set"].parms and p_info["set"].parms[0].type
                else "Any"
            )
            self.write(f"def {prop_name}(self, value: {p_type}) -> None: ...")

    def _emit_methods(self, cls: Class, skip_ids: set[int]) -> bool:
        method_groups = self._group_methods(cls, skip_ids)
        for name, group in method_groups.items():
            self.visit_function_group(name, group, is_method=True)
        return len(method_groups) > 0

    def _group_methods(self, cls: Class, skip_ids: set[int]) -> dict:
        method_groups = {}
        for method in cls.cdecls:
            if (
                id(method) in skip_ids
                or method.kind != "function"
                or self.should_skip_method(method)
            ):
                continue

            m_name = self._get_method_python_name(method)
            if m_name:
                method_groups.setdefault(m_name, []).append(method)
        return method_groups

    def _get_method_python_name(self, method: CDecl) -> str | None:
        m_name = method.name.split("::")[-1]
        if self.tm.config.rename_operators and m_name.startswith("operator"):
            m_name = self.map_operator(m_name)

        if m_name.startswith("operator"):
            return None

        if not m_name.startswith("__"):
            m_name = self._get_sanitized_name(m_name)
        return m_name

    def visit_constructor_group(self, group: list[Constructor]) -> None:
        """Emit a group of constructors as @overload __init__ methods."""
        unique_sigs = {}
        for ctor in group:
            dummy_func = CDecl(
                name="__init__",
                kind="function",
                type="void",
                parms=ctor.parms,
                is_static=False,
            )
            sig_tuple = self._get_function_signature(dummy_func, is_method=True)
            unique_sigs.setdefault(sig_tuple, ctor)

        sorted_sigs = sorted(unique_sigs.keys())
        use_overload = len(sorted_sigs) > 1
        for sig_tuple in sorted_sigs:
            params_str, ret_type = sig_tuple
            if use_overload:
                self.write("@overload")
            self.write(f"def __init__({params_str}) -> {ret_type}: ...")

    def visit_function_group(
        self, group_name: str, group: list[CDecl], *, is_method: bool
    ) -> None:
        """Emit a group of functions as @overload methods/functions."""
        unique_sigs = {}
        for func in group:
            sig = self._get_function_signature(func, is_method=is_method)
            unique_sigs.setdefault(sig, func)

        sorted_sigs = sorted(unique_sigs.keys())
        use_overload = len(sorted_sigs) > 1
        for sig_tuple in sorted_sigs:
            func = unique_sigs[sig_tuple]
            params_str, ret_type = sig_tuple
            if is_method and getattr(func, "is_static", False):
                self.write("@staticmethod")
            if use_overload:
                self.write("@overload")
            self.write(f"def {group_name}({params_str}) -> {ret_type}: ...")

    def _get_function_signature(
        self, func: CDecl, *, is_method: bool
    ) -> tuple[str, str]:
        param_parts = self.format_params(func.parms)
        is_static = getattr(func, "is_static", False)
        if is_method and not is_static:
            param_parts.insert(0, "self")

        if len(param_parts) > 1 or (
            is_method and not is_static and len(func.parms) > 0
        ):
            self.indent()
            params_str = ",\n".join(self.indent_level * "    " + p for p in param_parts)
            self.dedent()
            full_params = f"\n{params_str},\n" + self.indent_level * "    "
        elif len(param_parts) == 1:
            full_params = param_parts[0]
        else:
            full_params = ""

        ret_type = self.tm.to_python(func.type) if func.type else "Any"
        if ret_type == "void":
            ret_type = "None"
        return (full_params, ret_type)

    def should_skip_method(self, method: CDecl) -> bool:
        """Determine if a method should be excluded from stubs."""
        name = method.name
        if name.startswith("operator") and (
            not self.tm.config.rename_operators or self.map_operator(name) == name
        ):
            return True
        return bool(name.startswith("~"))

    def _get_sanitized_name(self, name: str) -> str:
        reserved = {
            "False",
            "None",
            "True",
            "and",
            "as",
            "assert",
            "async",
            "await",
            "break",
            "class",
            "continue",
            "def",
            "del",
            "elif",
            "else",
            "except",
            "finally",
            "for",
            "from",
            "global",
            "if",
            "import",
            "in",
            "is",
            "lambda",
            "nonlocal",
            "not",
            "or",
            "pass",
            "raise",
            "return",
            "try",
            "while",
            "with",
            "yield",
            "str",
            "open",
        }
        return name + "_" if name in reserved else name

    def format_params(self, parms: list[Parm]) -> list[str]:
        """Format parameter list for Python function signature."""
        parts = []
        for i, p in enumerate(parms):
            p_name = self._get_sanitized_name(p.name or f"arg{i}")
            p_type = self.tm.to_python(p.type) if p.type else "Any"
            parts.append(f"{p_name}: {p_type}")
        return parts

    def map_operator(self, name: str) -> str:
        """Map C++ operator name to Python dunder method name."""
        normalized = name.replace(" ", "")
        mapping = {
            "operator+": "__add__",
            "operator-": "__sub__",
            "operator*": "__mul__",
            "operator/": "__truediv__",
            "operator==": "__eq__",
            "operator!=": "__ne__",
            "operator<": "__lt__",
            "operator>": "__gt__",
            "operator<=": "__le__",
            "operator>=": "__ge__",
            "operator()": "__call__",
            "operator[]": "__getitem__",
            "operator->": "__deref__",
        }
        return mapping.get(normalized, name)
