"""Data models for representing parsed SWIG entities."""

from dataclasses import dataclass
from pathlib import Path


@dataclass
class SwigFile:
    """Represents a single parsed SWIG interface file."""

    path: Path
    includes: list[Path]
    content: str