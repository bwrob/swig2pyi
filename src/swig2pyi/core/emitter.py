from typing import List, Optional
from .parser import Top, Module, Class, CDecl, Constructor, Parm
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
        self.write("from typing import Any, Optional")
        self.write("import collections.abc")
        self.write("")
        
        if top.module:
            self.visit_module(top.module)

    def visit_module(self, module: Module):
        # Global functions (cdecls with kind='function')
        for func in module.cdecls:
            if func.kind == "function":
                self.visit_function(func)
        
        # Classes
        for cls in module.classes:
            self.visit_class(cls)

    def visit_class(self, cls: Class):
        name = cls.name
        # If kind is struct/class, usually maps to class.
        self.write(f"class {name}:")
        self.indent()
        
        has_members = False

        # Constructors
        if cls.constructors:
            for ctor in cls.constructors:
                self.visit_constructor(ctor)
                has_members = True
        
        # Methods
        for method in cls.cdecls:
            if method.kind == "function":
                 # Skip ignored methods or invalid names
                 if self.should_skip_method(method):
                     continue
                 self.visit_function(method, is_method=True)
                 has_members = True
        
        if not has_members:
            self.write("pass")
        
        self.dedent()
        self.write("")

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

    def visit_constructor(self, ctor: Constructor):
        # __init__
        params = self.format_params(ctor.parms)
        # Prepend self
        if params:
            full_params = f"self, {params}"
        else:
            full_params = "self"
            
        self.write(f"def __init__({full_params}) -> None: ...")

    def visit_function(self, func: CDecl, is_method: bool = False):
        name = func.name
        if is_method and self.tm.config.rename_operators:
            name = self.map_operator(name)
        
        # Double check skip logic
        if name.startswith("operator"): 
             return 

        params = self.format_params(func.parms)
        if is_method:
            if params:
                full_params = f"self, {params}"
            else:
                full_params = "self"
        else:
            full_params = params

        ret_type = self.tm.to_python(func.type) if func.type else "Any"
        
        # Normalize void
        if ret_type == "void": 
            ret_type = "None"

        self.write(f"def {name}({full_params}) -> {ret_type}: ...")

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
        return mapping.get(name, name)
