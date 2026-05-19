"""SWIG XML parser facade."""

from __future__ import annotations

import io
from typing import TYPE_CHECKING

from .ast_models import (
    AstModel,
    CDecl,
    Class,
    Constructor,
    Destructor,
    Enum,
    EnumItem,
    Module,
    Parm,
    Top,
)
from .builder import AstBuilder
from .ingestion import XmlIngestor

if TYPE_CHECKING:
    from pathlib import Path


class SwigXmlParser:
    """Parses SWIG XML using modular ingestion and building components."""

    def __init__(self) -> None:
        """Initialize parser."""
        self.ingestor = XmlIngestor()
        self.builder = AstBuilder()

    def parse_file(self, xml_path: Path, db_path: Path | None = None) -> Top:
        """Parse a SWIG XML file and return the AST."""
        engine = self.ingestor.run(xml_path, db_path)
        return self.builder.build(engine)

    def parse_string(self, xml_content: str, db_path: Path | None = None) -> Top:
        """Parse SWIG XML content from a string and return the AST."""
        source = io.BytesIO(xml_content.encode("utf-8"))
        engine = self.ingestor.run(source, db_path)
        return self.builder.build(engine)


__all__ = [
    "AstModel",
    "CDecl",
    "Class",
    "Constructor",
    "Destructor",
    "Enum",
    "EnumItem",
    "Module",
    "Parm",
    "SwigXmlParser",
    "Top",
]
