"""Pydantic models for the SWIG AST."""

from __future__ import annotations

from typing import TypeAlias

from pydantic import BaseModel


class Parm(BaseModel):
    """AST model for a function parameter."""

    name: str | None = None
    type: str | None = None


class CDecl(BaseModel):
    """AST model for a C++ declaration (function, variable, typedef)."""

    name: str
    type: str | None = None
    kind: str | None = None
    parms: list[Parm] = []
    decl: str | None = None
    is_static: bool = False
    docstring: str | None = None


class Constructor(BaseModel):
    """AST model for a class constructor."""

    name: str
    parms: list[Parm] = []
    is_static: bool = False
    docstring: str | None = None


class Destructor(BaseModel):
    """AST model for a class destructor."""

    name: str
    is_static: bool = False
    docstring: str | None = None


class EnumItem(BaseModel):
    """AST model for an enum member."""

    name: str
    value: str | None = None


class Enum(BaseModel):
    """AST model for an enum."""

    name: str
    items: list[EnumItem] = []
    docstring: str | None = None


class Class(BaseModel):
    """AST model for a class or struct."""

    name: str
    kind: str | None = None
    bases: list[str] = []
    enums: list[Enum] = []
    constructors: list[Constructor] = []
    destructors: list[Destructor] = []
    cdecls: list[CDecl] = []
    classes: list[Class] = []
    is_template: bool = False
    docstring: str | None = None
    cpp_type: str | None = None


class Module(BaseModel):
    """AST model for a SWIG module."""

    name: str
    enums: list[Enum] = []
    classes: list[Class] = []
    cdecls: list[CDecl] = []
    python_code: list[str] = []


class Top(BaseModel):
    """Root of the AST."""

    module: Module | None = None


AstModel: TypeAlias = (
    "CDecl | Constructor | Destructor | Enum | Class | Module | Top | EnumItem | Parm"
)
