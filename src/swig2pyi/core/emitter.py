"""Stub emitter for generating .pyi files."""

from __future__ import annotations

import re
from typing import TYPE_CHECKING

from .ast_models import CDecl, Class, Constructor, Enum, Module, Top
from .naming import NameManager
from .signature import SignatureFormatter

if TYPE_CHECKING:
    from .type_system import TypeManager


class StubEmitter:
    """Generates Python type stubs from AST."""

    def __init__(self, type_manager: TypeManager) -> None:
        """Initialize with type manager."""
        self.tm = type_manager
        self.nm = NameManager(rename_operators=type_manager.config.rename_operators)
        self.sf = SignatureFormatter(type_manager, self.nm)
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

    def _write_docstring(self, doc: str | None) -> None:
        if not doc:
            return
        # Clean up docstring (strip whitespace, ensure triple quotes)
        doc = doc.strip()
        if not doc:
            return

        if "\n" in doc:
            self.write('"""' + doc)
            self.write('"""')
        else:
            self.write(f'"""{doc}"""')

    def get_output(self) -> str:
        """Return the accumulated output as a string."""
        body = "\n".join(self.lines)
        needed_imports: list[str] = []

        # Scan body for utilized typing features using word boundaries
        typing_symbols = [
            sym
            for sym in (
                "Any",
                "Optional",
                "overload",
                "Generic",
                "TypeVar",
                "Union",
                "Callable",
            )
            if re.search(rf"\b{sym}\b", body)
        ]
        if typing_symbols:
            needed_imports.append(f"from typing import {', '.join(typing_symbols)}")

        if re.search(r"\bIntEnum\b", body):
            needed_imports.append("from enum import IntEnum")
        if re.search(r"\bcollections\.abc\b", body):
            needed_imports.append("import collections.abc")
        if re.search(r"\btyping\.", body):
            needed_imports.append("import typing")

        header = "\n".join(needed_imports)
        if header:
            header += "\n\n"
        return header + body

    def emit(self, top: Top) -> None:
        """Generate the full stub output from the Top AST node."""
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
                self.write(f"{self.nm.sanitize(item.name)}: {name}")
            self.write("")

    def _emit_module_functions(self, module: Module) -> None:
        func_groups: dict[str, list[CDecl]] = {}
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
        self._write_docstring(enum.docstring)
        has_items = False
        for item in enum.items:
            item_name = self.nm.sanitize(item.name)
            if item.value is not None:
                self.write(f"{item_name} = {item.value}")
            else:
                self.write(f"{item_name} = ...")
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
        self._write_docstring(cls.docstring)

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
        base_names: list[str] = []
        if cls.bases:
            for b in cls.bases:
                base_names.extend(self._get_base_names(b))
        if cls.is_template:
            base_names.append("Generic[_T]")
        return f"({', '.join(base_names)})" if base_names else ""

    def _get_base_names(self, base_type: str) -> list[str]:
        names: list[str] = []
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
        prop_method_ids: set[int] = set()
        for prop_name, p_info in properties.items():
            if not p_info["get"]:
                continue
            self._emit_property(prop_name, p_info)
            prop_method_ids.add(id(p_info["get"]))
            if p_info["set"]:
                prop_method_ids.add(id(p_info["set"]))
        return prop_method_ids

    def _collect_properties(self, cls: Class) -> dict[str, dict[str, CDecl | None]]:
        properties: dict[str, dict[str, CDecl | None]] = {}
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

    def _emit_property(self, prop_name: str, p_info: dict[str, CDecl | None]) -> None:
        getter = p_info["get"]
        if not getter:
            return
        ret_type = self.tm.to_python(getter.type) if getter.type else "Any"
        if ret_type == "void":
            ret_type = "None"
        self.write("@property")
        self.write(f"def {prop_name}(self) -> {ret_type}: ...")
        setter = p_info["set"]
        if setter:
            self.write(f"@{prop_name}.setter")
            p_type = (
                self.tm.to_python(setter.parms[0].type)
                if setter.parms and setter.parms[0].type
                else "Any"
            )
            self.write(f"def {prop_name}(self, value: {p_type}) -> None: ...")

    def _emit_methods(self, cls: Class, skip_ids: set[int]) -> bool:
        method_groups = self._group_methods(cls, skip_ids)
        for name, group in method_groups.items():
            self.visit_function_group(name, group, is_method=True)
        return len(method_groups) > 0

    def _group_methods(self, cls: Class, skip_ids: set[int]) -> dict[str, list[CDecl]]:
        method_groups: dict[str, list[CDecl]] = {}
        for method in cls.cdecls:
            if (
                id(method) in skip_ids
                or method.kind not in ("function", "variable")
                or self.should_skip_method(method)
            ):
                continue

            m_name = self.nm.get_python_name(method.name)
            if m_name:
                if m_name not in method_groups:
                    method_groups[m_name] = []
                method_groups[m_name].append(method)
        return method_groups

    def visit_constructor_group(self, group: list[Constructor]) -> None:
        """Emit a group of constructors as @overload __init__ methods."""
        unique_sigs: dict[tuple[str, str], Constructor] = {}
        for ctor in group:
            dummy_func = CDecl(
                name="__init__",
                kind="function",
                type="void",
                parms=ctor.parms,
                is_static=False,
            )
            sig_tuple = self.sf.get_signature(
                dummy_func, is_method=True, indent_level=self.indent_level
            )
            unique_sigs[sig_tuple] = ctor

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
        # Handle member variables as properties
        if is_method and any(getattr(m, "kind", None) == "variable" for m in group):
            self._emit_variable_group(group_name, group)
            return

        self._emit_overloaded_functions(group_name, group, is_method=is_method)

    def _emit_variable_group(self, group_name: str, group: list[CDecl]) -> None:
        for var in group:
            ret_type = self.tm.to_python(var.type) if var.type else "Any"
            if ret_type == "void":
                ret_type = "None"
            self.write(f"{group_name}: {ret_type}")
            self._write_docstring(var.docstring)

    def _emit_overloaded_functions(
        self, group_name: str, group: list[CDecl], *, is_method: bool
    ) -> None:
        unique_sigs: dict[tuple[str, str], CDecl] = {}
        for func in group:
            sig = self.sf.get_signature(
                func, is_method=is_method, indent_level=self.indent_level
            )
            unique_sigs[sig] = func

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
            if not use_overload:
                self._write_docstring(func.docstring)

    def should_skip_method(self, method: CDecl) -> bool:
        """Determine if a method should be excluded from stubs."""
        name = method.name
        if name.startswith("operator") and (
            not self.tm.config.rename_operators or self.nm.map_operator(name) == name
        ):
            return True
        return bool(name.startswith("~"))
