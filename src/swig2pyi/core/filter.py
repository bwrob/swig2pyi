"""Transitive stub filtering logic."""

from __future__ import annotations

import re
from typing import TYPE_CHECKING

from swig2pyi.core.ast_models import CDecl, Class, Enum, Module, Top
from swig2pyi.core.naming import NameManager
from swig2pyi.core.type_system import TypeManager

if TYPE_CHECKING:
    from swig2pyi.core.config import Config


def extract_referenced_symbols(type_str: str | None, tm: TypeManager) -> set[str]:
    """Extract referenced python class/enum names from a type string."""
    if not type_str:
        return set()
    try:
        py_type = tm.to_python(type_str)
    except Exception:  # noqa: BLE001
        py_type = type_str

    words = set(re.findall(r"\b[a-zA-Z_][a-zA-Z0-9_]*\b", py_type))
    ignore = {
        "int",
        "float",
        "str",
        "bool",
        "bytes",
        "object",
        "type",
        "list",
        "dict",
        "set",
        "tuple",
        "None",
        "Any",
        "Optional",
        "Union",
        "Callable",
        "Sequence",
        "Iterable",
        "Iterator",
        "Final",
        "Generic",
        "TypeVar",
        "overload",
    }
    return words - ignore


class FilterState:
    """Helper class to compute transitive closure of required symbols."""

    def __init__(self, top: Top, config: Config) -> None:
        """Initialize filter state mapping variables and queues."""
        self.module = top.module
        self.tm = TypeManager(config, top=top)
        self.nm = NameManager(rename_operators=config.rename_operators)
        self.queue: list[Class | CDecl | Enum] = []
        self.visited_classes: set[str] = set()
        self.visited_enums: set[str] = set()
        self.visited_cdecls: set[str] = set()

        # Populate cpp_to_py_class_names for tm.to_python resolution
        cpp_to_py_class_names: dict[str, str] = {}
        if self.module:
            for cls in self.module.classes:
                if cls.name:
                    key_name = self.tm.clean_cpp_type(cls.name)
                    cpp_to_py_class_names[key_name] = cls.name
                if cls.cpp_type:
                    key = self.tm.clean_cpp_type(cls.cpp_type)
                    cpp_to_py_class_names[key] = cls.name
        self.tm.cpp_to_py_class_names = cpp_to_py_class_names

        # Build symbol maps
        self.class_by_py_name: dict[str, Class] = {}
        self.class_by_cpp_name: dict[str, Class] = {}
        self.enum_by_name: dict[str, Enum] = {}
        self.cdecl_by_name: dict[str, CDecl] = {}
        self._build_symbol_maps()

    def _map_classes(self) -> None:
        """Map classes by C++ and Python names."""
        if not self.module:
            return
        for cls in self.module.classes:
            if cls.name:
                self.class_by_py_name[cls.name] = cls
                cleaned = self.tm.clean_cpp_type(cls.name)
                self.class_by_cpp_name[cleaned] = cls
            if cls.cpp_type:
                cleaned = self.tm.clean_cpp_type(cls.cpp_type)
                self.class_by_cpp_name[cleaned] = cls

    def _map_enums(self) -> None:
        """Map enum nodes by name."""
        if not self.module:
            return
        self.enum_by_name = {enum.name: enum for enum in self.module.enums if enum.name}

    def _map_cdecls(self) -> None:
        """Map global declaration nodes by name."""
        if not self.module:
            return
        for cdecl in self.module.cdecls:
            if cdecl.name:
                self.cdecl_by_name[cdecl.name] = cdecl
                py_name = self.nm.get_python_name(cdecl.name)
                if py_name:
                    self.cdecl_by_name[py_name] = cdecl

    def _build_symbol_maps(self) -> None:
        """Map AST symbols by python and C++ types for efficient lookup."""
        self._map_classes()
        self._map_enums()
        self._map_cdecls()

    def add_symbol_to_queue(self, sym: str) -> None:
        """Find and add symbol to the BFS traversal queue if not visited."""
        if sym in self.class_by_py_name:
            target_cls = self.class_by_py_name[sym]
            if target_cls.name not in self.visited_classes:
                self.visited_classes.add(target_cls.name)
                self.queue.append(target_cls)
        elif sym in self.enum_by_name:
            target_enum = self.enum_by_name[sym]
            if target_enum.name not in self.visited_enums:
                self.visited_enums.add(target_enum.name)
                self.queue.append(target_enum)

    def _collect_seed_class(self, seed: str) -> bool:
        """Add class seeds to the queue."""
        if seed in self.class_by_py_name:
            cls = self.class_by_py_name[seed]
            if cls.name not in self.visited_classes:
                self.visited_classes.add(cls.name)
                self.queue.append(cls)
            return True
        if seed in self.class_by_cpp_name:
            cls = self.class_by_cpp_name[seed]
            if cls.name not in self.visited_classes:
                self.visited_classes.add(cls.name)
                self.queue.append(cls)
            return True
        return False

    def _collect_seed_enum(self, seed: str) -> bool:
        """Add enum seeds to the queue."""
        if seed in self.enum_by_name:
            enum = self.enum_by_name[seed]
            if enum.name not in self.visited_enums:
                self.visited_enums.add(enum.name)
                self.queue.append(enum)
            return True
        return False

    def _collect_seed_cdecl(self, seed: str) -> bool:
        """Add global declaration seeds to the queue."""
        if seed in self.cdecl_by_name:
            cdecl = self.cdecl_by_name[seed]
            if cdecl.name not in self.visited_cdecls:
                self.visited_cdecls.add(cdecl.name)
                self.queue.append(cdecl)
            return True
        return False

    def _collect_single_seed(self, seed: str) -> None:
        """Add a single symbol to the queues if found in maps."""
        if self._collect_seed_class(seed):
            return
        if self._collect_seed_enum(seed):
            return
        if self._collect_seed_cdecl(seed):
            return

    def collect_seeds(self, include_symbols: list[str]) -> None:
        """Initialize visited sets and queues with the user-selected seed symbols."""
        for seed in include_symbols:
            self._collect_single_seed(seed)

    def _traverse_class_bases(self, node: Class) -> None:
        """Process class inheritance parent dependencies."""
        for base in node.bases or []:
            cleaned = self.tm.clean_cpp_type(base)
            if cleaned in self.class_by_cpp_name:
                target_cls = self.class_by_cpp_name[cleaned]
                if target_cls.name not in self.visited_classes:
                    self.visited_classes.add(target_cls.name)
                    self.queue.append(target_cls)

    def _traverse_class_ctors(self, node: Class) -> None:
        """Process constructor parameter type dependencies."""
        for ctor in node.constructors or []:
            for parm in ctor.parms or []:
                for sym in extract_referenced_symbols(parm.type, self.tm):
                    self.add_symbol_to_queue(sym)

    def _traverse_class_members(self, node: Class) -> None:
        """Process method and field type dependencies."""
        for cdecl in node.cdecls or []:
            for parm in cdecl.parms or []:
                for sym in extract_referenced_symbols(parm.type, self.tm):
                    self.add_symbol_to_queue(sym)
            for sym in extract_referenced_symbols(cdecl.type, self.tm):
                self.add_symbol_to_queue(sym)

    def _traverse_class_nested(self, node: Class) -> None:
        """Process nested class definitions."""
        for nested in node.classes or []:
            if nested.name not in self.visited_classes:
                self.visited_classes.add(nested.name)
                self.queue.append(nested)

    def traverse_class(self, node: Class) -> None:
        """Process class bases, constructor signatures, methods and members."""
        self._traverse_class_bases(node)
        self._traverse_class_ctors(node)
        self._traverse_class_members(node)
        self._traverse_class_nested(node)

    def traverse_cdecl(self, node: CDecl) -> None:
        """Process global variables or global function signatures."""
        for parm in node.parms or []:
            for sym in extract_referenced_symbols(parm.type, self.tm):
                self.add_symbol_to_queue(sym)
        for sym in extract_referenced_symbols(node.type, self.tm):
            self.add_symbol_to_queue(sym)

    def traverse(self) -> None:
        """Run BFS transitive dependency resolution queue until empty."""
        while self.queue:
            node = self.queue.pop(0)
            if isinstance(node, Class):
                self.traverse_class(node)
            elif isinstance(node, CDecl):
                self.traverse_cdecl(node)


def filter_ast(top: Top, include_symbols: list[str], config: Config) -> Top:
    """Filter the Top AST module.

    Only includes symbols and their transitive dependencies.
    """
    if not top.module or not include_symbols:
        return top

    state = FilterState(top, config)
    state.collect_seeds(include_symbols)
    state.traverse()

    # Build new filtered Module
    module = top.module
    filtered_enums = [e for e in module.enums if e.name in state.visited_enums]
    filtered_classes = [c for c in module.classes if c.name in state.visited_classes]
    filtered_cdecls = [c for c in module.cdecls if c.name in state.visited_cdecls]

    filtered_module = Module(
        name=module.name,
        enums=filtered_enums,
        classes=filtered_classes,
        cdecls=filtered_cdecls,
        python_code=module.python_code,
        typedefs=module.typedefs,
    )
    return Top(module=filtered_module)
