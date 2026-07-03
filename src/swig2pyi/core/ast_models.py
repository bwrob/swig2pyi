"""Dataclasses for the SWIG AST."""

from __future__ import annotations

import copy
from dataclasses import dataclass, field
from typing import TypeAlias


@dataclass(slots=True)
class Parm:
    """AST model for a function parameter."""

    name: str | None = None
    type: str | None = None
    value: str | None = None


@dataclass(slots=True)
class CDecl:
    """AST model for a C++ declaration (function, variable, typedef)."""

    name: str
    type: str | None = None
    kind: str | None = None
    parms: list[Parm] = field(default_factory=list)
    decl: str | None = None
    is_static: bool = False
    docstring: str | None = None

    def model_copy(self, *, deep: bool = True) -> CDecl:
        """Return a copy of this CDecl."""
        return copy.deepcopy(self) if deep else copy.copy(self)


@dataclass(slots=True)
class Constructor:
    """AST model for a class constructor."""

    name: str
    parms: list[Parm] = field(default_factory=list)
    is_static: bool = False
    docstring: str | None = None


@dataclass(slots=True)
class Destructor:
    """AST model for a class destructor."""

    name: str
    is_static: bool = False
    docstring: str | None = None


@dataclass(slots=True)
class EnumItem:
    """AST model for an enum member."""

    name: str
    value: str | None = None


@dataclass(slots=True)
class Enum:
    """AST model for an enum."""

    name: str
    items: list[EnumItem] = field(default_factory=list)
    docstring: str | None = None


@dataclass(slots=True)
class Class:
    """AST model for a class or struct."""

    name: str
    kind: str | None = None
    bases: list[str] = field(default_factory=list)
    enums: list[Enum] = field(default_factory=list)
    constructors: list[Constructor] = field(default_factory=list)
    destructors: list[Destructor] = field(default_factory=list)
    cdecls: list[CDecl] = field(default_factory=list)
    classes: list[Class] = field(default_factory=list)
    is_template: bool = False
    docstring: str | None = None
    cpp_type: str | None = None


@dataclass(slots=True)
class Module:
    """AST model for a SWIG module."""

    name: str
    enums: list[Enum] = field(default_factory=list)
    classes: list[Class] = field(default_factory=list)
    cdecls: list[CDecl] = field(default_factory=list)
    python_code: list[str] = field(default_factory=list)
    typedefs: dict[str, str] = field(default_factory=dict)


@dataclass(slots=True)
class Top:
    """Root of the AST."""

    module: Module | None = None


AstModel: TypeAlias = (
    "CDecl | Constructor | Destructor | Enum | Class | Module | Top | EnumItem | Parm"
)
