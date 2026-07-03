"""Stub emitter for generating .pyi files."""

from __future__ import annotations

import ast as pyast
import re
import textwrap
from typing import TYPE_CHECKING

from .ast_models import CDecl, Class, Constructor, Enum, Module, Parm, Top
from .naming import NameManager

if TYPE_CHECKING:
    from .type_system import TypeManager


class StubEmitter:
    """Generates Python type stubs from AST."""

    def __init__(self, type_manager: TypeManager) -> None:
        """Initialize with type manager."""
        self.tm = type_manager
        self.nm = NameManager(rename_operators=type_manager.config.rename_operators)
        self.lines: list[str] = []
        self.indent_level = 0
        self.needs_typevar_t = False
        self.emitted_classes: set[str] = set()
        self._extra_classes: set[str] = set()
        for line in type_manager.config.extra_code:
            match = re.match(r"^\s*class\s+([a-zA-Z0-9_]+)", line)
            if match:
                self._extra_classes.add(match.group(1))

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
        if self.needs_typevar_t or re.search(r"\b_T\b", body):
            self.needs_typevar_t = True
            self.tm.needed_imports.add("TypeVar")
            body = "_T = TypeVar('_T')\n\n" + body
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
            "Final",
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
        self._scan_extra_code()
        self.write("")
        if top.module:
            self.visit_module(top.module)

    def _scan_extra_code(self) -> None:
        for line in self.tm.config.extra_code:
            self.write(line)
            self._scan_extra_code_line(line)

    def _scan_extra_code_line(self, line: str) -> None:
        # Scan extra_code line for typing and other imports
        for sym in (
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
            "Final",
        ):
            if re.search(rf"\b{sym}\b", line):
                self.tm.needed_imports.add(sym)
        if re.search(r"\bIntEnum\b", line):
            self.tm.needed_imports.add("IntEnum")
        if re.search(r"\bcollections\.abc\b", line):
            self.tm.needed_imports.add("collections.abc")
        if re.search(r"\btyping\.", line):
            self.tm.needed_imports.add("typing")

    def visit_module(self, module: Module) -> None:
        """Visit a module and emit its contents."""
        self.emitted_classes.clear()
        self._cpp_to_py_class_names: dict[str, str] = {}
        for cls in module.classes:
            if cls.name:
                key_name = self.tm.clean_cpp_type(cls.name)
                self._cpp_to_py_class_names[key_name] = cls.name
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
            (
                self.nm.get_python_name(m.name),
                tuple(self.tm.to_python(p.type or "") for p in m.parms),
            )
            for m in cls.cdecls
            if self.nm.get_python_name(m.name)
        }
        for method in collected:
            py_name = self.nm.get_python_name(method.name)
            if not py_name or py_name in originally_defined_names:
                continue
            sig_key = (
                py_name,
                tuple(self.tm.to_python(p.type or "") for p in method.parms),
            )
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
                self._emit_pythoncode_node(node)

    def _emit_pythoncode_node(self, node: pyast.AST) -> None:
        if isinstance(node, pyast.FunctionDef):
            self._emit_pythoncode_func(node)
        elif isinstance(node, pyast.ClassDef):
            self._emit_pythoncode_class(node)
        elif isinstance(node, pyast.Assign):
            self._emit_pythoncode_assign(node)
        elif isinstance(node, pyast.AnnAssign):
            self._emit_pythoncode_annassign(node)
        elif isinstance(node, (pyast.Import, pyast.ImportFrom)):
            self.write(pyast.unparse(node))

    def _emit_pythoncode_assign(self, node: pyast.Assign) -> None:
        for target in node.targets:
            if isinstance(target, pyast.Name) and not target.id.startswith("_"):
                self.write(f"{target.id}: Any")
                self.tm.needed_imports.add("Any")

    def _emit_pythoncode_annassign(self, node: pyast.AnnAssign) -> None:
        if isinstance(node.target, pyast.Name) and not node.target.id.startswith("_"):
            ann = pyast.unparse(node.annotation)
            self.tm.record_imports(ann)
            self.write(f"{node.target.id}: {ann}")

    def _emit_pythoncode_func(self, node: pyast.FunctionDef) -> None:
        """Emit a stub for a function defined in %pythoncode."""
        if node.name.startswith("_"):
            return
        sig_override = self.tm.config.pythoncode_signatures.get(node.name)
        if sig_override:
            self.write(f"def {node.name}{sig_override}: ...")
            self.tm.record_imports(sig_override)
            return

        parts = self._format_pythoncode_args(node.args)
        sig = ", ".join(parts)
        ret_ann = self._get_pythoncode_returns(node.returns)
        self.write(f"def {node.name}({sig}) -> {ret_ann}: ...")

    def _format_pythoncode_arg(self, arg_node: pyast.arg, *, has_default: bool) -> str:
        name = arg_node.arg
        if arg_node.annotation:
            ann = pyast.unparse(arg_node.annotation)
            self.tm.record_imports(ann)
            res = f"{name}: {ann}"
        else:
            res = name
        if has_default:
            return f"{res} = ..."
        return res

    def _format_pythoncode_args(self, args_node: pyast.arguments) -> list[str]:
        parts: list[str] = []
        posonlyargs = getattr(args_node, "posonlyargs", [])
        args = args_node.args
        all_pos_args = posonlyargs + args
        num_defaults = len(args_node.defaults)
        start_default_idx = len(all_pos_args) - num_defaults

        for i, arg in enumerate(posonlyargs):
            parts.append(
                self._format_pythoncode_arg(arg, has_default=i >= start_default_idx)
            )

        if posonlyargs:
            parts.append("/")

        for i, arg in enumerate(args):
            actual_idx = len(posonlyargs) + i
            parts.append(
                self._format_pythoncode_arg(
                    arg, has_default=actual_idx >= start_default_idx
                )
            )

        self._format_pythoncode_varargs(args_node, parts)
        return parts

    def _format_pythoncode_varargs(
        self, args_node: pyast.arguments, parts: list[str]
    ) -> None:
        if args_node.vararg:
            vararg_ann = ""
            if args_node.vararg.annotation:
                ann = pyast.unparse(args_node.vararg.annotation)
                self.tm.record_imports(ann)
                vararg_ann = f": {ann}"
            parts.append(f"*{args_node.vararg.arg}{vararg_ann}")
        elif args_node.kwonlyargs:
            parts.append("*")

        for arg, kw_default in zip(
            args_node.kwonlyargs, args_node.kw_defaults, strict=False
        ):
            parts.append(
                self._format_pythoncode_arg(arg, has_default=kw_default is not None)
            )

        if args_node.kwarg:
            kwarg_ann = ""
            if args_node.kwarg.annotation:
                ann = pyast.unparse(args_node.kwarg.annotation)
                self.tm.record_imports(ann)
                kwarg_ann = f": {ann}"
            parts.append(f"**{args_node.kwarg.arg}{kwarg_ann}")

    def _get_pythoncode_returns(self, returns_node: pyast.expr | None) -> str:
        if returns_node:
            ret_ann = pyast.unparse(returns_node)
            self.tm.record_imports(ret_ann)
            return ret_ann
        self.tm.needed_imports.add("Any")
        return "Any"

    def _emit_pythoncode_class(self, node: pyast.ClassDef) -> None:
        """Emit a stub for a class defined in %pythoncode."""
        if node.name.startswith("_"):
            return
        bases = [base.id for base in node.bases if isinstance(base, pyast.Name)]
        bases_str = f"({', '.join(bases)})" if bases else ""
        self.write(f"class {node.name}{bases_str}:")
        self.indent()
        has_body = False
        for item in node.body:
            if self._emit_pythoncode_class_item(item):
                has_body = True
        if not has_body:
            self.write("pass")
        self.dedent()
        self.write("")

    def _emit_pythoncode_class_item(self, item: pyast.AST) -> bool:
        if isinstance(item, pyast.FunctionDef) and not item.name.startswith("_"):
            self._emit_pythoncode_func(item)
            return True
        if isinstance(item, pyast.Assign):
            self._emit_pythoncode_assign(item)
            return any(
                isinstance(t, pyast.Name) and not t.id.startswith("_")
                for t in item.targets
            )
        if isinstance(item, pyast.AnnAssign):
            self._emit_pythoncode_annassign(item)
            return isinstance(
                item.target, pyast.Name
            ) and not item.target.id.startswith("_")
        return False

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
            if (
                func.name.startswith("operator")
                or func.name in self.tm.config.skip_functions
            ):
                continue
            if self.should_skip_method(func):
                continue
            name = func.name.split("::")[-1]
            func_groups.setdefault(name, []).append(func)

        for name, group in func_groups.items():
            self.visit_function_group(name, group, is_method=False)

    def _is_const_type(self, type_str: str | None) -> bool:
        if not type_str:
            return False
        before_template = type_str.split("<", 1)[0]
        return bool(re.search(r"\bconst\b", before_template))

    def _resolve_var_type(self, var_type: str | None) -> str:
        if var_type:
            ret_type = self.tm.to_python(var_type)
        else:
            ret_type = "Any"
            self.tm.needed_imports.add("Any")
        if ret_type == "void":
            ret_type = "None"
        if self._is_const_type(var_type):
            ret_type = f"Final[{ret_type}]"
            self.tm.needed_imports.add("Final")
        return ret_type

    def _emit_module_variables(self, module: Module) -> None:
        """Emit module-level variables and the SWIG cvar object."""
        variables: list[tuple[str, str, str | None]] = []
        for var in module.cdecls:
            if var.kind != "variable":
                continue
            name = self.nm.get_python_name(var.name)
            if not name:
                continue
            ret_type = self._resolve_var_type(var.type)
            variables.append((name, ret_type, var.docstring))

        if not variables:
            return

        for name, ret_type, docstring in variables:
            self.write(f"{name}: {ret_type}")
            self._write_docstring(docstring)

        self.write("")
        self.write("class cvar_class:")
        self.indent()
        for name, ret_type, docstring in variables:
            self.write(f"{name}: {ret_type}")
            self._write_docstring(docstring)
        self.dedent()
        self.write("")
        self.write("cvar: cvar_class")
        self.write("")

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

        if name in self.emitted_classes:
            return
        self.emitted_classes.add(name)

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

        if self._emit_methods(cls):
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
            self.tm.needed_imports.add("TypeVar")
            self.needs_typevar_t = True
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

        # Filter base class: it must be a class defined in this module,
        # a standard generic container base, or an imported/extra base.
        base_name_only = normalized_base.split("[", 1)[0]
        is_valid_base = (
            base_name_only in self._cpp_to_py_class_names.values()
            or base_name_only in self._extra_classes
            or base_name_only in self.tm.config.delegate_templates
            or base_name_only
            in (
                "list",
                "dict",
                "set",
                "tuple",
                "Sequence",
                "Iterable",
                "Iterator",
                "Generic",
                "IntEnum",
                "object",
                "Exception",
            )
        )
        if not is_valid_base:
            return []

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

    def _emit_getitem_iter(self, getitem_funcs: list[CDecl]) -> None:
        ret_type = "Any"
        if getitem_funcs and getitem_funcs[0].type:
            ret_type = self.tm.to_python(getitem_funcs[0].type)
            if ret_type == "None":
                ret_type = "Any"
        if ret_type == "Any":
            self.tm.needed_imports.add("Any")
        self.write(f"def __iter__(self) -> Iterator[{ret_type}]: ...")
        self.tm.needed_imports.add("Iterator")

    def _emit_methods(self, cls: Class) -> bool:
        method_groups = self._group_methods(cls)
        is_container = self._get_container_elem_type(cls) is not None
        for name, group in method_groups.items():
            if is_container and name in (
                "push_back",
                "resize",
                "size",
                "empty",
                "clear",
            ):
                continue
            self.visit_function_group(name, group, is_method=True)
        if "__getitem__" in method_groups:
            self._emit_getitem_iter(method_groups["__getitem__"])
        return len(method_groups) > 0

    def _group_methods(self, cls: Class) -> dict[str, list[CDecl]]:
        method_groups: dict[str, list[CDecl]] = {}
        for method in cls.cdecls:
            if method.kind not in ("function", "variable") or self.should_skip_method(
                method
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
            sig_tuple = self.get_signature(
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
            ret_type = self._resolve_var_type(var.type)
            self.write(f"{group_name}: {ret_type}")
            self._write_docstring(var.docstring)

    def _emit_overloaded_functions(
        self, group_name: str, group: list[CDecl], *, is_method: bool
    ) -> None:
        unique_sigs: dict[tuple[str, str], CDecl] = {}
        for func in group:
            sig = self.get_signature(
                func, is_method=is_method, indent_level=self.indent_level
            )
            unique_sigs[sig] = func

        sorted_sigs = sorted(unique_sigs.keys())
        use_overload = len(sorted_sigs) > 1
        for sig_tuple in sorted_sigs:
            func = unique_sigs[sig_tuple]
            params_str, ret_type = sig_tuple
            if use_overload:
                self.write("@overload")
                self.tm.needed_imports.add("overload")
            if is_method and getattr(func, "is_static", False):
                self.write("@staticmethod")
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

    def format_params(self, parms: list[Parm]) -> list[str]:
        """Format parameter list for Python function signature."""
        parts: list[str] = []
        for i, p in enumerate(parms):
            p_name = self.nm.sanitize(p.name or f"arg{i}")
            if p.type:
                p_type = self.tm.to_python(p.type, is_parameter=True)
            else:
                self.tm.needed_imports.add("Any")
                p_type = "Any"

            if p_type in self.tm.enums:
                self.tm.needed_imports.add("Union")
                p_type = f"Union[{p_type}, int]"
            if p.value is not None:
                parts.append(f"{p_name}: {p_type} = ...")
            else:
                parts.append(f"{p_name}: {p_type}")
        return parts

    def _get_param_parts(
        self, func: CDecl, *, is_method: bool, mapped_name: str | None
    ) -> list[str]:
        is_cmp = is_method and mapped_name in ("__eq__", "__ne__")
        if is_cmp:
            return ["other: object"]
        return self.format_params(func.parms)

    def _format_params_string(
        self,
        param_parts: list[str],
        *,
        is_method: bool,
        is_static: bool,
        num_parms: int,
        indent_level: int,
    ) -> str:
        if is_method and not is_static:
            param_parts.insert(0, "self")

        if len(param_parts) > 1 or (is_method and not is_static and num_parms > 0):
            params_str = ",\n".join(
                (indent_level + 1) * "    " + p for p in param_parts
            )
            return f"\n{params_str},\n" + indent_level * "    "
        if len(param_parts) == 1:
            return param_parts[0]
        return ""

    def _get_return_type(self, func_type: str | None) -> str:
        if not func_type:
            self.tm.needed_imports.add("Any")
            return "Any"
        ret_type = self.tm.to_python(func_type)
        if ret_type == "void":
            return "None"
        return ret_type

    def get_signature(
        self, func: CDecl, *, is_method: bool, indent_level: int = 0
    ) -> tuple[str, str]:
        """Get the parameters string and return type for a function/method."""
        mapped_name = self.nm.get_python_name(func.name) if is_method else func.name
        param_parts = self._get_param_parts(
            func, is_method=is_method, mapped_name=mapped_name
        )
        is_static = getattr(func, "is_static", False)
        full_params = self._format_params_string(
            param_parts,
            is_method=is_method,
            is_static=is_static,
            num_parms=len(func.parms),
            indent_level=indent_level,
        )
        ret_type = self._get_return_type(func.type)
        return (full_params, ret_type)
