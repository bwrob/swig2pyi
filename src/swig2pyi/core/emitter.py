from typing import List, Optional
from .parser import Top, Module, Class, CDecl, Constructor, Parm, Enum
from .type_system import TypeManager

class StubEmitter:
    def __init__(self, type_manager: TypeManager):
        self.tm = type_manager
        self.lines: List[str] = []
        self.indent_level = 0
    
    def indent(self):
        self.indent_level += 1

    def dedent(self):
        self.indent_level = max(0, self.indent_level - 1)

    def write(self, text: str = ""):
        self.lines.append("    " * self.indent_level + text)

    def get_output(self) -> str:
        return "\n".join(self.lines)

    def emit(self, top: Top):
        self.write("import typing")
        self.write("from typing import Any, Optional, overload")
        self.write("import collections.abc")
        self.write("")
        
        if top.module:
            self.visit_module(top.module)

    def visit_module(self, module: Module):
        # Enums
        for enum in module.enums:
            self.visit_enum(enum)

        # Group global functions by name
        func_groups = {}
        for func in module.cdecls:
            if func.kind == "function":
                name = func.name
                if name not in func_groups:
                    func_groups[name] = []
                func_groups[name].append(func)

        for name, group in func_groups.items():
             self.visit_function_group(group, is_method=False)
        
        # Classes
        for cls in module.classes:
            self.visit_class(cls)

    def visit_enum(self, enum: Enum):
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
            val_str = f" = {item.value}" if item.value is not None else ""
            self.write(f"{item.name}: int{val_str}")
            has_items = True
            
        if not has_items:
            self.write("pass")
            
        self.dedent()
        self.write("")

    def visit_class(self, cls: Class):
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
        bases_str = ""
        if cls.bases:
            # Normalize base names
            # We use type manager to clean up namespaces, but we assume bases are classes in the same file 
            # or imported.
            base_names = []
            for b in cls.bases:
                # We can use to_python, which does namespace stripping and checking config.
                # Assuming base classes are mapped or in the same module.
                normalized_base = self.tm.to_python(b)
                base_names.append(normalized_base)
            
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
                 
                 if m_name.startswith("operator"): # Unmapped operator
                     continue

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

    def visit_constructor_group(self, group: List[Constructor]):
        unique_sigs = {}
        
        for ctor in group:
            params = self.format_params(ctor.parms)
            if params:
                full_params = f"self, {params}"
            else:
                full_params = "self"
            
            sig = full_params
            if sig not in unique_sigs:
                unique_sigs[sig] = ctor
        
        sorted_sigs = sorted(unique_sigs.keys())
        use_overload = len(sorted_sigs) > 1
        
        for sig in sorted_sigs:
            if use_overload:
                self.write("@overload")
            self.write(f"def __init__({sig}) -> None: ...")

    def visit_function_group(self, group: List[CDecl], is_method: bool):
        # Deduplicate by Python signature
        unique_sigs = {}
        
        for func in group:
            sig = self._get_function_signature(func, is_method)
            if sig not in unique_sigs:
                unique_sigs[sig] = func
        
        sorted_sigs = sorted(unique_sigs.keys())
        
        # If we have multiple signatures, use @overload
        use_overload = len(sorted_sigs) > 1
        
        for sig in sorted_sigs:
            func = unique_sigs[sig]
            name = func.name
            if is_method and self.tm.config.rename_operators:
                name = self.map_operator(name)

            # Signature components
            params_str, ret_type = sig
            
            if use_overload:
                self.write("@overload")
            
            self.write(f"def {name}({params_str}) -> {ret_type}: ...")

    def _get_function_signature(self, func: CDecl, is_method: bool):
        params = self.format_params(func.parms)
        if is_method:
            if params:
                full_params = f"self, {params}"
            else:
                full_params = "self"
        else:
            full_params = params

        ret_type = self.tm.to_python(func.type) if func.type else "Any"
        if ret_type == "void": 
            ret_type = "None"
            
        return (full_params, ret_type)

    def should_skip_method(self, method: CDecl) -> bool:
        name = method.name
        if name.startswith("operator") and not self.tm.config.rename_operators:
            return True
        if name.startswith("operator") and self.tm.config.rename_operators:
            if self.map_operator(name) == name: # Not mapped
                return True
        # Destructors usually handled separately or ignored in stubs
        if name.startswith("~"):
            return True
        return False

    def format_params(self, parms: List[Parm]) -> str:
        parts = []
        for i, p in enumerate(parms):
            p_name = p.name
            if not p_name:
                 p_name = f"arg{i}" # Default name if missing
            
            # Sanitize keywords
            if p_name in ["from", "in", "global", "lambda", "class", "def", "pass", "None"]:
                p_name += "_"
            
            p_type = self.tm.to_python(p.type) if p.type else "Any"
            parts.append(f"{p_name}: {p_type}")
        
        return ", ".join(parts)

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