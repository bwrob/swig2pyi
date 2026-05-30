"""Stub emitter for generating .pyi files."""

from __future__ import annotations

import ast as pyast
import re
import textwrap
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

        typing_symbols_list = (
            "Any",
            "Optional",
            "overload",
            "Generic",
            "TypeVar",
            "Union",
            "Callable",
            "Sequence",
            "Iterable",
            "Iterator",
        )
        typing_symbols = [
            sym for sym in typing_symbols_list if sym in self.tm.needed_imports
        ]
        if typing_symbols:
            needed_imports.append(f"from typing import {', '.join(typing_symbols)}")

        if "IntEnum" in self.tm.needed_imports:
            needed_imports.append("from enum import IntEnum")
        if "collections.abc" in self.tm.needed_imports:
            needed_imports.append("import collections.abc")
        if "typing" in self.tm.needed_imports:
            needed_imports.append("import typing")

        header = "\n".join(needed_imports)
        if header:
            header += "\n\n"
        return header + body

    def emit(self, top: Top) -> None:
        """Generate the full stub output from the Top AST node."""
        self.write("_T = TypeVar('_T')")
        self.tm.needed_imports.add("TypeVar")
        self.write("")
        for line in self.tm.config.extra_code:
            self.write(line)
        self.write("")
        if top.module:
            self.visit_module(top.module)

    def visit_module(self, module: Module) -> None:
        """Visit a module and emit its contents."""
        self._cpp_to_py_class_names: dict[str, str] = {}
        for cls in module.classes:
            if cls.cpp_type:
                key = self.tm.clean_cpp_type(cls.cpp_type)
                self._cpp_to_py_class_names[key] = cls.name
        self.tm.cpp_to_py_class_names = self._cpp_to_py_class_names
        self.tm.py_class_to_cpp_types = {
            cls.name: cls.cpp_type for cls in module.classes if cls.cpp_type
        }

        self._delegate_handle_methods(module)

        self._emit_module_enums(module)
        self._emit_module_functions(module)
        self._emit_module_variables(module)
        for cls in module.classes:
            self.visit_class(cls)
        self._emit_python_code(module)

    def _collect_class_methods(
        self, cls_name: str, name_to_class: dict[str, Class], visited: set[str]
    ) -> list[CDecl]:
        """Recursively collect cdecls from a class and its base classes."""
        if cls_name in visited:
            return []
        visited.add(cls_name)
        target_cls = name_to_class.get(cls_name)
        if not target_cls:
            return []
        methods = list(target_cls.cdecls)
        for base in target_cls.bases:
            cleaned_base = self.tm.clean_cpp_type(base)
            py_base_name = self._cpp_to_py_class_names.get(cleaned_base)
            if py_base_name:
                methods.extend(
                    self._collect_class_methods(py_base_name, name_to_class, visited)
                )
        return methods

    def _get_delegate_target(self, cpp_type: str) -> str | None:
        """Parse delegate target name from C++ type string."""
        if not cpp_type or not self.tm.config.delegate_templates:
            return None

        escaped_templates = "|".join(
            re.escape(t) for t in self.tm.config.delegate_templates
        )
        ns_prefixes = "|".join(
            re.escape(ns)
            for ns in self.tm.config.namespaces_to_remove
            if ns.endswith("::")
        )
        ns_pattern = f"(?:{ns_prefixes})?" if ns_prefixes else ""

        pattern = rf"^{ns_pattern}(?:{escaped_templates})<\s*(.*?)\s*>$"
        match = re.match(pattern, cpp_type)
        if not match:
            return None

        target_type = match.group(1).strip("() ")
        cleaned_target = self.tm.clean_cpp_type(target_type)
        return self._cpp_to_py_class_names.get(cleaned_target)

    def _delegate_single_handle(
        self, cls: Class, name_to_class: dict[str, Class]
    ) -> None:
        """Delegate methods for a single Handle class."""
        if not cls.cpp_type:
            return
        py_target_name = self._get_delegate_target(cls.cpp_type)
        if not py_target_name:
            return

        collected = self._collect_class_methods(py_target_name, name_to_class, set())
        originally_defined_names = {
            self.nm.get_python_name(m.name)
            for m in cls.cdecls
            if self.nm.get_python_name(m.name)
        }
        existing_signatures = {
            (self.nm.get_python_name(m.name), tuple(p.type for p in m.parms))
            for m in cls.cdecls
            if self.nm.get_python_name(m.name)
        }
        for method in collected:
            py_name = self.nm.get_python_name(method.name)
            if not py_name or py_name in originally_defined_names:
                continue
            sig_key = (py_name, tuple(p.type for p in method.parms))
            if sig_key not in existing_signatures:
                cls.cdecls.append(method.model_copy(deep=True))
                existing_signatures.add(sig_key)

    def _delegate_handle_methods(self, module: Module) -> None:
        """Delegate methods from target classes to Handle wrappers."""
        name_to_class = {cls.name: cls for cls in module.classes}
        for cls in module.classes:
            self._delegate_single_handle(cls, name_to_class)

    def _emit_python_code(self, module: Module) -> None:
        """Extract and emit stub signatures from %pythoncode blocks."""
        for code_block in module.python_code:
            dedented = textwrap.dedent(code_block)
            try:
                tree = pyast.parse(dedented)
            except SyntaxError:
                continue

            for node in tree.body:
                if isinstance(node, pyast.FunctionDef):
                    self._emit_pythoncode_func(node)
                elif isinstance(node, pyast.ClassDef):
                    self._emit_pythoncode_class(node)

    def _emit_pythoncode_func(self, node: pyast.FunctionDef) -> None:
        """Emit a stub for a function defined in %pythoncode."""
        if node.name.startswith("_"):
            return
        args = [a.arg for a in node.args.args]
        defaults_count = len(node.args.defaults)
        parts: list[str] = []
        for i, arg in enumerate(args):
            default_idx = i - (len(args) - defaults_count)
            if default_idx >= 0:
                parts.append(f"{arg}=...")
            else:
                parts.append(arg)
        if node.args.vararg:
            parts.append(f"*{node.args.vararg.arg}")
        if node.args.kwarg:
            parts.append(f"**{node.args.kwarg.arg}")
        sig = ", ".join(parts)
        self.write(f"def {node.name}({sig}) -> Any: ...")

    def _emit_pythoncode_class(self, node: pyast.ClassDef) -> None:
        """Emit a stub for a class defined in %pythoncode."""
        if node.name.startswith("_"):
            return
        bases = [base.id for base in node.bases if isinstance(base, pyast.Name)]
        bases_str = f"({', '.join(bases)})" if bases else ""
        self.write(f"class {node.name}{bases_str}:")
        self.indent()
        has_methods = False
        for item in node.body:
            if isinstance(item, pyast.FunctionDef) and not item.name.startswith("_"):
                self._emit_pythoncode_func(item)
                has_methods = True
        if not has_methods:
            self.write("pass")
        self.dedent()
        self.write("")

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

    def _emit_module_variables(self, module: Module) -> None:
        """Emit module-level variables (e.g. __version__)."""
        for var in module.cdecls:
            if var.kind != "variable":
                continue
            name = self.nm.get_python_name(var.name)
            if not name:
                continue
            ret_type = self.tm.to_python(var.type) if var.type else "Any"
            if ret_type == "void":
                ret_type = "None"
            self.write(f"{name}: {ret_type}")
            self._write_docstring(var.docstring)

    def visit_enum(self, enum: Enum) -> None:
        """Emit a Python IntEnum from a C++ enum."""
        name = enum.name.split("::")[-1]
        self.write(f"class {name}(IntEnum):")
        self.tm.needed_imports.add("IntEnum")
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

    def _emit_class_enums(self, cls: Class) -> bool:
        """Emit nested enums and flat class attributes."""
        if not cls.enums:
            return False
        for enum in cls.enums:
            self.visit_enum(enum)
            enum_name = enum.name.split("::")[-1]
            for item in enum.items:
                item_name = self.nm.sanitize(item.name)
                self.write(f"{item_name}: {enum_name}")
        return True

    def _get_container_elem_type(self, cls: Class) -> str | None:
        if not cls.cpp_type:
            return None
        resolved = self.tm.to_python(cls.cpp_type, bypass_mapping=True)
        if resolved.startswith("list[") and resolved.endswith("]"):
            return resolved[5:-1]
        return None

    def _emit_container_methods(self, container_elem_type: str) -> None:
        self.write(f"def push_back(self, x: {container_elem_type}) -> None: ...")
        self.write("def resize(self, n: int) -> None: ...")
        self.write("def size(self) -> int: ...")
        self.write("def empty(self) -> bool: ...")
        self.write("def clear(self) -> None: ...")

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

        has_members = self._emit_class_enums(cls)

        container_elem_type = self._get_container_elem_type(cls)

        if cls.constructors:
            self.visit_constructor_group(cls.constructors, container_elem_type)
            has_members = True
        elif container_elem_type:
            self.visit_constructor_group([], container_elem_type)
            has_members = True

        if container_elem_type:
            self._emit_container_methods(container_elem_type)
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
        for b in cls.bases or []:
            base_names.extend(self._get_base_names(b))
        if cls.cpp_type:
            self._add_cpp_type_base(cls.cpp_type, base_names)
        if cls.is_template:
            base_names.append("Generic[_T]")
            self.tm.needed_imports.add("Generic")
        return f"({', '.join(base_names)})" if base_names else ""

    def _add_cpp_type_base(self, cpp_type: str, base_names: list[str]) -> None:
        resolved = self.tm.to_python(cpp_type, bypass_mapping=True)
        is_generic = self._is_container_type(resolved) or any(
            resolved.startswith(f"{t}[") for t in self.tm.config.generic_templates
        )
        if is_generic and resolved not in base_names:
            base_names.append(resolved)
            self._add_delegate_base(resolved, base_names)

    def _add_delegate_base(self, resolved: str, base_names: list[str]) -> None:
        if not self.tm.config.delegate_templates:
            return
        escaped_templates = "|".join(
            re.escape(t) for t in self.tm.config.delegate_templates
        )
        pattern = rf"(?:^|\.)(?:{escaped_templates})\[(.+)\]$"
        match = re.search(pattern, resolved)
        if match:
            wrapped_type = match.group(1)
            if wrapped_type not in base_names:
                base_names.append(wrapped_type)

    def _is_container_type(self, resolved: str) -> bool:
        for py_abc in self.tm.config.containers.values():
            if resolved.startswith(py_abc + "[") or resolved == py_abc:
                return True
        return False

    def _get_base_names(self, base_type: str) -> list[str]:
        names: list[str] = []
        cleaned = self.tm.clean_cpp_type(base_type)
        if cleaned in self._cpp_to_py_class_names:
            normalized_base = self._cpp_to_py_class_names[cleaned]
        else:
            normalized_base = self.tm.to_python(base_type)
        names.append(normalized_base)
        if self.tm.config.delegate_templates:
            escaped_templates = "|".join(
                re.escape(t) for t in self.tm.config.delegate_templates
            )
            pattern = rf"(?:^|\.)(?:{escaped_templates})\[(.+)\]$"
            match = re.search(pattern, normalized_base)
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
        """Collect getter/setter properties from class methods."""
        _ = cls  # Reserved for future use
        return {}

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
        if "__getitem__" in method_groups:
            getitem_funcs = method_groups["__getitem__"]
            ret_type = "Any"
            if getitem_funcs and getitem_funcs[0].type:
                ret_type = self.tm.to_python(getitem_funcs[0].type)
                if ret_type == "None":
                    ret_type = "Any"
            self.write(f"def __iter__(self) -> Iterator[{ret_type}]: ...")
            self.tm.needed_imports.add("Iterator")
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

    def _add_container_ctor_overloads(
        self, unique_sigs: dict[tuple[str, str], Constructor | None], elem_type: str
    ) -> None:
        iterable_sig = (f"self, iterable: Iterable[{elem_type}] = ...", "None")
        if iterable_sig not in unique_sigs:
            unique_sigs[iterable_sig] = None
        size_sig = ("self, size: int", "None")
        if size_sig not in unique_sigs:
            unique_sigs[size_sig] = None
        size_val_sig = (f"self, size: int, value: {elem_type}", "None")
        if size_val_sig not in unique_sigs:
            unique_sigs[size_val_sig] = None
        self.tm.needed_imports.add("Iterable")

    def visit_constructor_group(
        self, group: list[Constructor], container_elem_type: str | None = None
    ) -> None:
        """Emit a group of constructors as @overload __init__ methods."""
        unique_sigs: dict[tuple[str, str], Constructor | None] = {}
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

        if container_elem_type:
            self._add_container_ctor_overloads(unique_sigs, container_elem_type)

        sorted_sigs = sorted(unique_sigs.keys())
        use_overload = len(sorted_sigs) > 1
        for sig_tuple in sorted_sigs:
            params_str, ret_type = sig_tuple
            if use_overload:
                self.write("@overload")
                self.tm.needed_imports.add("overload")
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
                self.tm.needed_imports.add("overload")
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
