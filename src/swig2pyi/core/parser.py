from __future__ import annotations

import xml.etree.ElementTree as ET
from typing import TYPE_CHECKING

from pydantic import BaseModel

if TYPE_CHECKING:
    from pathlib import Path

# --- Models ---

class Parm(BaseModel):
    """Represents a parameter in a function or method."""

    name: str | None = None
    type: str | None = None


class CDecl(BaseModel):
    """Represents a C-style declaration (function, variable)."""

    name: str
    type: str | None = None
    kind: str | None = None  # e.g. function, variable
    parms: list[Parm] = []
    decl: str | None = None  # e.g. f(int)


class Constructor(BaseModel):
    """Represents a class constructor."""

    name: str
    parms: list[Parm] = []


class Destructor(BaseModel):
    """Represents a class destructor."""

    name: str


class EnumItem(BaseModel):
    """Represents an item within an enumeration."""

    name: str
    value: str | None = None


class Enum(BaseModel):
    """Represents an enumeration."""

    name: str
    items: list[EnumItem] = []


class Class(BaseModel):
    """Represents a C++ class or struct."""

    name: str
    kind: str | None = None  # class, struct
    is_template: bool = False
    bases: list[str] = []
    classes: list[Class] = []  # Nested classes
    enums: list[Enum] = []  # Nested enums
    constructors: list[Constructor] = []
    destructors: list[Destructor] = []
    cdecls: list[CDecl] = []  # methods and members


class Module(BaseModel):
    """Represents a top-level module."""

    name: str
    classes: list[Class] = []
    enums: list[Enum] = []
    cdecls: list[CDecl] = []


class Top(BaseModel):
    """Represents the top-level structure of the parsed XML."""

    module: Module | None = None


# --- Parser ---

class SwigXmlParser:
    """Parses SWIG-generated XML into a structured AST."""

    def parse_file(self, file_path: Path) -> Top:
        """Parse an XML file from SWIG."""
        try:
            tree = ET.parse(str(file_path))  # noqa: S314
            root = tree.getroot()
            return self._parse_root(root)
        except ET.ParseError as e:
            msg = f"Failed to parse XML: {e}"
            raise RuntimeError(msg) from e

    def parse_string(self, xml_content: str) -> Top:
        """Parse an XML string from SWIG."""
        try:
            root = ET.fromstring(xml_content)  # noqa: S314
            return self._parse_root(root)
        except ET.ParseError as e:
            msg = f"Failed to parse XML string: {e}"
            raise RuntimeError(msg) from e

    def _get_attributes(self, node: ET.Element) -> dict[str, str]:
        """Extracts attributes from <attributelist> child."""
        attrs = {}
        # SWIG XML puts attributes in a child <attributelist>
        # <attributelist> contains <attribute name="..." value="..."/>
        attr_list = node.find("attributelist")
        if attr_list is not None:
            for attr_node in attr_list.findall("attribute"):
                name = attr_node.get("name")
                value = attr_node.get("value")
                if name and value is not None:
                    attrs[name] = value

        return attrs

    def _parse_parms(self, node: ET.Element) -> list[Parm]:
        """Parses parameters from a node, looking in direct children and attributelist."""
        parms: list[Parm] = []

        def extract_parm(p_node: ET.Element) -> Parm:
            p_attrs = self._get_attributes(p_node)
            return Parm(
                name=p_attrs.get("name"),
                type=p_attrs.get("type")
            )

        def scan_children(parent: ET.Element) -> None:
            for child in parent:
                if child.tag == "parm":
                    parms.append(extract_parm(child))
                elif child.tag == "parmlist":
                    scan_children(child)

        # Scan direct children
        scan_children(node)

        # Scan children of attributelist
        attr_list = node.find("attributelist")
        if attr_list is not None:
            scan_children(attr_list)

        return parms

    def _parse_cdecl(self, node: ET.Element, attrs: dict[str, str]) -> CDecl:
        """Parses a C-style declaration."""
        return CDecl(
            name=attrs.get("name", ""),
            type=attrs.get("type"),
            kind=attrs.get("kind"),
            decl=attrs.get("decl"),
            parms=self._parse_parms(node)
        )

    def _parse_constructor(self, node: ET.Element, attrs: dict[str, str]) -> Constructor:
        """Parses a constructor declaration."""
        return Constructor(
            name=attrs.get("name", ""),
            parms=self._parse_parms(node)
        )

    def _parse_destructor(self, node: ET.Element, attrs: dict[str, str]) -> Destructor: # noqa: ARG002
        """Parses a destructor declaration."""
        return Destructor(name=attrs.get("name", ""))

    def _parse_enum(self, node: ET.Element, attrs: dict[str, str]) -> Enum:
        """Parses an enumeration."""
        enum_obj = Enum(name=attrs.get("name", ""))

        for child in node:
            if child.tag == "enumitem":
                item_attrs = self._get_attributes(child)
                enum_obj.items.append(EnumItem(
                    name=item_attrs.get("name", ""),
                    value=item_attrs.get("enumvalue")
                ))
        return enum_obj

    def _parse_class(self, node: ET.Element, attrs: dict[str, str], is_template: bool = False) -> Class: # noqa: C901
        """Parses a C++ class or struct declaration."""
        cls = Class(
            name=attrs.get("name", ""),
            kind=attrs.get("kind"),
            is_template=is_template
        )

        # Helper to parse baselist
        def parse_baselist(bl_node: ET.Element) -> None:
            for base in bl_node.findall("base"):
                b_name = base.get("name")
                if b_name:
                    cls.bases.append(b_name)

        # Check for baselist in attributelist
        attr_list = node.find("attributelist")
        if attr_list is not None:
            baselist = attr_list.find("baselist")
            if baselist is not None:
                parse_baselist(baselist)

        # Check for direct baselist (fallback, though seemingly unused by SWIG 4)
        baselist = node.find("baselist")
        if baselist is not None:
            parse_baselist(baselist)

        for child in node:
            if child.tag == "attributelist":
                continue

            # SWIG XML often nests 'cdecl' for methods
            if child.tag == "cdecl":
                c_attrs = self._get_attributes(child)
                # Method or member
                kind = c_attrs.get("kind")
                if kind in ("function", "variable"):
                     cls.cdecls.append(self._parse_cdecl(child, c_attrs))

            elif child.tag == "constructor":
                c_attrs = self._get_attributes(child)
                cls.constructors.append(self._parse_constructor(child, c_attrs))
            elif child.tag == "destructor":
                c_attrs = self._get_attributes(child)
                cls.destructors.append(self._parse_destructor(child, c_attrs))
            elif child.tag == "class":
                 # Nested class
                 c_attrs = self._get_attributes(child)
                 # Nested classes inside a template are also templates/generics
                 cls.classes.append(self._parse_class(child, c_attrs, is_template=is_template))
            elif child.tag == "enum":
                 e_attrs = self._get_attributes(child)
                 cls.enums.append(self._parse_enum(child, e_attrs))

        return cls

    def _parse_root(self, root: ET.Element) -> Top: # noqa: C901
        """Parses the root XML element to build the module AST."""
        top_attrs = self._get_attributes(root)
        module_name = top_attrs.get("module", "Unknown")

        module = Module(name=module_name)
        top = Top(module=module)

        # Recursive traversal
        def visit(node: ET.Element, in_template: bool = False) -> None: # noqa: C901, PLR0912
            # Pre-check for class child if in template
            has_class_child = False
            if in_template:
                for child in node:
                    if child.tag == "class":
                        has_class_child = True
                        break

            for child in node:
                tag = child.tag
                if tag == "attributelist":
                    continue

                if tag == "class":
                    attrs = self._get_attributes(child)
                    if attrs.get("feature_ignore") == "1":
                        continue
                    # If name is missing, it might be anonymous struct or something
                    if not attrs.get("name"):
                        continue

                    cls = self._parse_class(child, attrs, is_template=in_template)
                    module.classes.append(cls)

                elif tag == "cdecl":
                    if in_template and has_class_child:
                        continue

                    attrs = self._get_attributes(child)
                    if attrs.get("feature_ignore") == "1":
                        continue

                    kind = attrs.get("kind")
                    # We strictly want global functions/variables here
                    if kind in ("function", "variable"):
                        func = self._parse_cdecl(child, attrs)
                        module.cdecls.append(func)

                elif tag == "enum":
                    attrs = self._get_attributes(child)
                    # Check if ignoring? usually not for enums
                    module.enums.append(self._parse_enum(child, attrs))

                elif tag == "template":
                    attrs = self._get_attributes(child)
                    if attrs.get("feature_ignore") == "1":
                        continue
                    visit(child, in_template=True)

                elif tag in ("include", "namespace", "module", "top", "insert"):
                    visit(child, in_template)

        visit(root)
        return top
