from .parser import CDecl, Class, Constructor, Enum, Module, Parm, Top
from .type_system import TypeManager


class StubEmitter:
    def __init__(self, type_manager: TypeManager) -> None:
        self.tm = type_manager
        self.lines: list[str] = []
        self.indent_level = 0

    def indent(self) -> None:
        self.indent_level += 1

    def dedent(self) -> None:
        self.indent_level = max(0, self.indent_level - 1)

    def write(self, text: str = "") -> None:
        line = "    " * self.indent_level + text
        self.lines.append(line.rstrip())

    def get_output(self) -> str:
        return "\n".join(self.lines)

    def emit(self, top: Top) -> None:
        # Suppress strict pyright checks for generated stubs
        self.write("# pyright: reportUnusedImport=false, reportDeprecated=false, reportExplicitAny=false, reportInvalidTypeVarUse=false")
        self.write("import typing")
        self.write("from typing import Any, Optional, overload, Generic, TypeVar")
        self.write("import collections.abc")
        self.write("")
        
        # Define TypeVar for generics
        self.write("_T = TypeVar('_T')")
        self.write("")

        # Emit extra code from config
        for line in self.tm.config.extra_code:
            self.write(line)
        self.write("")

        if top.module:
            self.visit_module(top.module)

    def visit_module(self, module: Module) -> None:
        # Enums
        for enum in module.enums:
            self.visit_enum(enum)

        # Group global functions by name
        func_groups = {}
        for func in module.cdecls:
            if func.kind == "function":
                # Skip global operators (they are C++ artifacts usually)
                if func.name.startswith("operator"):
                    continue
                
                # Skip Handle members appearing as globals
                if func.name in ("linkTo", "currentLink", "empty", "values"):
                    continue

                if self.should_skip_method(func):
                    continue

                name = func.name
                if name not in func_groups:
                    func_groups[name] = []
                func_groups[name].append(func)

        for name, group in func_groups.items():
            self.visit_function_group(group, is_method=False)

        # Classes
        for cls in module.classes:
            self.visit_class(cls)

    def visit_enum(self, enum: Enum) -> None:
        name = enum.name
        if "::" in name:
            name = name.split("::")[-1]

        # Emit as a class inheriting from int
        self.write(f"class {name}(int):")
        self.indent()

        has_items = False
        for item in enum.items:
            # Emit as class variables: NAME: int = VALUE
            # Value is optional, sometimes helpful.
            
            item_name = self._get_sanitized_name(item.name)
            
            val_str = f" = {item.value}" if item.value is not None else ""
            self.write(f"{item_name}: int{val_str}")
            has_items = True

        if not has_items:
            self.write("pass")

        self.dedent()
        self.write("")

    def visit_class(self, cls: Class) -> None:
        name = cls.name

        # Filter invalid or unwanted classes
        if name.startswith("std::"):
            return
        if "<" in name:
            # Template instantiation without %template rename
            return

        # Normalize namespace (e.g. QuantLib::Date -> Date)
        if "::" in name:
            name = name.split("::")[-1]

        # Process bases
        base_names = []
        if cls.bases:
            # Normalize base names
            # We use type manager to clean up namespaces, but we assume bases are classes in the same file
            # or imported.
            for b in cls.bases:
                # We can use to_python, which does namespace stripping and checking config.
                # Assuming base classes are mapped or in the same module.
                normalized_base = self.tm.to_python(b)
                base_names.append(normalized_base)

        if cls.is_template:
            base_names.append("Generic[_T]")

        bases_str = ""
        if base_names:
            bases_str = "(" + ", ".join(base_names) + ")"

        # If kind is struct/class, usually maps to class.
        self.write(f"class {name}{bases_str}:")
        self.indent()

        has_members = False

        # Nested Enums
        for enum in cls.enums:
            self.visit_enum(enum)
            has_members = True

        # Constructors
        if cls.constructors:
            self.visit_constructor_group(cls.constructors)
            has_members = True

        # Group methods by name
        method_groups = {}
        for method in cls.cdecls:
            if method.kind == "function":
                # Skip ignored methods or invalid names
                if self.should_skip_method(method):
                    continue

                # Map operator names for grouping
                m_name = method.name
                if self.tm.config.rename_operators and m_name.startswith("operator"):
                    m_name = self.map_operator(m_name)

                if m_name.startswith("operator"):  # Unmapped operator
                    continue
                
                # Sanitize method name if it's not an operator (operators are already valid dunders)
                if not m_name.startswith("__"):
                     m_name = self._get_sanitized_name(m_name)

                if m_name not in method_groups:
                    method_groups[m_name] = []
                method_groups[m_name].append(method)

        for name, group in method_groups.items():
            self.visit_function_group(group, is_method=True)
            has_members = True

        if not has_members:
            self.write("pass")

        self.dedent()
        self.write("")

    def visit_constructor_group(self, group: list[Constructor]) -> None:
        unique_sigs = {}

        for ctor in group:
            # Create a dummy CDecl for constructor to reuse _get_function_signature
            # Constructors have no return type, so we pass "void" which maps to "None"
            dummy_func = CDecl(
                name="__init__",
                kind="function",
                type="void",
                parms=ctor.parms,
                mname="",
                minfo=""
            )
            # is_method=True because constructors are methods
            sig_tuple = self._get_function_signature(dummy_func, is_method=True)
            
            # Use the full signature tuple as the key for deduplication
            if sig_tuple not in unique_sigs:
                unique_sigs[sig_tuple] = ctor # Store original ctor for other info if needed

        sorted_sigs = sorted(unique_sigs.keys()) # Sort by the tuple itself, which is fine

        use_overload = len(sorted_sigs) > 1

        for sig_tuple in sorted_sigs:
            params_str, ret_type = sig_tuple # Unpack the signature components

            if use_overload:
                self.write("@overload")
            self.write(f"def __init__({params_str}) -> {ret_type}: ...")

    def visit_function_group(self, group: list[CDecl], is_method: bool) -> None:
        # Deduplicate by Python signature
        unique_sigs = {}

        for func in group:
            sig = self._get_function_signature(func, is_method)
            if sig not in unique_sigs:
                unique_sigs[sig] = func

        sorted_sigs = sorted(unique_sigs.keys())

        # If we have multiple signatures, use @overload
        use_overload = len(sorted_sigs) > 1

        for sig_tuple in sorted_sigs: # Renamed sig to sig_tuple for clarity
            func = unique_sigs[sig_tuple]
            name = func.name
            if is_method and self.tm.config.rename_operators:
                name = self.map_operator(name)
            
            # Sanitize name if not operator
            if not name.startswith("__"):
                name = self._get_sanitized_name(name)

            params_str, ret_type = sig_tuple # Unpack the signature components

            if use_overload:
                self.write("@overload")

            self.write(f"def {name}({params_str}) -> {ret_type}: ...")

    def _get_function_signature(self, func: CDecl, is_method: bool):
        param_parts = self.format_params(func.parms)
        
        if is_method:
            param_parts.insert(0, "self")

        if len(param_parts) > 1:
            # Multi-line parameters
            self.indent()
            params_str = ",\n".join(self.indent_level * "    " + p for p in param_parts)
            self.dedent()
            # The extra comma makes it consistent even for one parameter
            full_params = f"\n{params_str},\n" + self.indent_level * "    "
        elif len(param_parts) == 1:
            # Single parameter (like 'self' only, or 'self, param')
            # Forcing multi-line if any actual parameters (other than self)
            if is_method and len(func.parms) == 0:
                full_params = "self" # only self, keep on one line
            else:
                self.indent()
                params_str = ",\n".join(self.indent_level * "    " + p for p in param_parts)
                self.dedent()
                full_params = f"\n{params_str},\n" + self.indent_level * "    "
        else:
            full_params = ""

        ret_type = self.tm.to_python(func.type) if func.type else "Any"
        if ret_type == "void":
            ret_type = "None"

        return (full_params, ret_type)

    def should_skip_method(self, method: CDecl) -> bool:
        name = method.name
        if name.startswith("operator") and not self.tm.config.rename_operators:
            return True
        if name.startswith("operator") and self.tm.config.rename_operators:
            if self.map_operator(name) == name:  # Not mapped
                return True
        # Destructors usually handled separately or ignored in stubs
        return bool(name.startswith("~"))

    def _get_sanitized_name(self, name: str) -> str:
        # Comprehensive list of Python reserved keywords
        reserved_keywords = {
            "False", "None", "True", "and", "as", "assert", "async", "await", "break",
            "class", "continue", "def", "del", "elif", "else", "except", "finally",
            "for", "from", "global", "if", "import", "in", "is", "lambda", "nonlocal",
            "not", "or", "pass", "raise", "return", "try", "while", "with", "yield",
            "str", "open" # Added 'str' and 'open'
        }
        if name in reserved_keywords:
            return name + "_"
        return name

    def format_params(self, parms: list[Parm]) -> list[str]:
        parts = []
        for i, p in enumerate(parms):
            p_name = p.name
            if not p_name:
                p_name = f"arg{i}"  # Default name if missing

            p_name = self._get_sanitized_name(p_name)

            p_type = self.tm.to_python(p.type) if p.type else "Any"
            parts.append(f"{p_name}: {p_type}")

        return parts

    def map_operator(self, name: str) -> str:
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
        }
        return mapping.get(normalized, name)
