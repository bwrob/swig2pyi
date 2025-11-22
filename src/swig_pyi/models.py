"""Data models for representing parsed SWIG entities."""

from dataclasses import dataclass, field
from pathlib import Path


@dataclass
class SwigFile:
    """Represents a single parsed SWIG interface file."""

    path: Path
    includes: list[Path]
    content: str


@dataclass
class Parameter:
    """Represents a function or method parameter."""

    name: str
    type: str


@dataclass
class Function:
    """Represents a C++ function."""

    name: str
    parameters: list[Parameter]
    return_type: str


@dataclass
class Class:
    """Represents a C++ class."""

    name: str
    methods: list[Function] = field(default_factory=list)