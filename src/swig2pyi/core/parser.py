"""SWIG XML parser facade (direct in-memory implementation)."""

from __future__ import annotations

import io
import xml.etree.ElementTree as ET
from collections import defaultdict
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

if TYPE_CHECKING:
    from pathlib import Path


class SwigXmlParser:
    """Parses SWIG XML directly into the Pydantic AST in a single pass."""

    def __init__(self) -> None:
        """Initialize parser state variables."""
        self.elem_stack: list[ET.Element] = []
        self.class_elem_stack: list[ET.Element] = []
        self.children_by_parent: dict[ET.Element, list[AstModel]] = defaultdict(list)
        self.module: Module | None = None
        self.template_depth = 0

    def parse_file(self, xml_path: Path, db_path: Path | None = None) -> Top:
        """Parse a SWIG XML file and return the AST."""
        _ = db_path  # Database path is obsolete but kept for compatibility
        return self._parse_xml(xml_path)

    def parse_string(self, xml_content: str, db_path: Path | None = None) -> Top:
        """Parse SWIG XML content from a string and return the AST."""
        _ = db_path  # Database path is obsolete but kept for compatibility
        source = io.BytesIO(xml_content.encode("utf-8"))
        return self._parse_xml(source)

    def _reset_state(self) -> None:
        self.elem_stack = []
        self.class_elem_stack = []
        self.children_by_parent = defaultdict(list)
        self.module = None
        self.template_depth = 0

    def _parse_xml(self, source: io.BytesIO | Path) -> Top:
        self._reset_state()
        context = ET.iterparse(source, events=("start", "end"))  # noqa: S314
        for event, elem in context:
            if event == "start":
                self._handle_start(elem)
            elif event == "end":
                self._handle_end(elem)
        return Top(module=self.module)

    def _handle_start(self, elem: ET.Element) -> None:
        tag = elem.tag
        self.elem_stack.append(elem)
        if tag == "top":
            self.module = Module(name="Unknown")
        elif tag == "template":
            self.template_depth += 1
        elif tag == "class" and self.template_depth == 0:
            self.class_elem_stack.append(elem)

    def _handle_end(self, elem: ET.Element) -> None:
        tag = elem.tag
        self.elem_stack.pop()

        if tag == "template":
            self._handle_template_end(elem)
            return

        if self.template_depth > 0:
            self._discard_element(elem)
            return

        self._process_end_tag(elem, tag)

    def _handle_template_end(self, elem: ET.Element) -> None:
        self.template_depth -= 1
        self._discard_element(elem)

    def _discard_element(self, elem: ET.Element) -> None:
        elem.clear()
        if self.elem_stack:
            self.elem_stack[-1].remove(elem)

    def _handle_top_end(self, elem: ET.Element) -> None:
        attrs = self._get_attrs(elem)
        if self.module:
            self.module.name = attrs.get("module", "Unknown")

    def _handle_insert_end(self, elem: ET.Element) -> None:
        attrs = self._get_attrs(elem)
        if attrs.get("section") == "python" and "code" in attrs:
            code = attrs["code"].strip()
            if code and self.module:
                self.module.python_code.append(code)

    def _process_end_tag(self, elem: ET.Element, tag: str) -> None:
        if tag == "top":
            self._handle_top_end(elem)
        elif tag == "insert":
            self._handle_insert_end(elem)
        elif tag in ("class", "cdecl", "enum", "constructor", "destructor"):
            self._parse_node(elem, tag)

        is_discardable = tag in (
            "class",
            "cdecl",
            "enum",
            "constructor",
            "destructor",
            "template",
            "include",
            "namespace",
            "module",
        )
        if is_discardable:
            self._discard_element(elem)

    def _parse_node(self, elem: ET.Element, tag: str) -> None:
        attrs = self._get_attrs(elem)
        name = attrs.get("sym_name") or attrs.get("name", "")

        if tag == "class":
            self.class_elem_stack.pop()

        ignore_cond = attrs.get("feature_ignore") == "1" or (
            not name and tag == "class"
        )
        if ignore_cond:
            return

        model = self._create_model(elem, tag, attrs, name)
        if model is not None:
            self._register_model(model)

    def _register_model(self, model: AstModel) -> None:
        if self.class_elem_stack:
            parent_elem = self.class_elem_stack[-1]
            self.children_by_parent[parent_elem].append(model)
        elif self.module:
            if isinstance(model, CDecl):
                self.module.cdecls.append(model)
            elif isinstance(model, Class):
                self.module.classes.append(model)
            elif isinstance(model, Enum):
                self.module.enums.append(model)

    def _create_model(
        self,
        elem: ET.Element,
        tag: str,
        attrs: dict[str, str],
        name: str,
    ) -> AstModel | None:
        is_static = attrs.get("storage") == "static"
        docstring = attrs.get("feature_docstring")

        if tag == "cdecl":
            kind = attrs.get("kind")
            if kind in ("function", "variable"):
                return CDecl(
                    name=name,
                    type=attrs.get("type"),
                    kind=kind,
                    decl=attrs.get("decl"),
                    parms=self._extract_parms(elem),
                    is_static=is_static,
                    docstring=docstring,
                )
        elif tag == "constructor":
            return Constructor(
                name=name,
                parms=self._extract_parms(elem),
                is_static=is_static,
                docstring=docstring,
            )
        elif tag == "destructor":
            return Destructor(
                name=name,
                is_static=is_static,
                docstring=docstring,
            )
        elif tag == "enum":
            return Enum(
                name=name,
                items=self._extract_enum_items(elem),
                docstring=docstring,
            )
        elif tag == "class":
            return self._create_class_model(elem, attrs, name, docstring)
        return None

    def _create_class_model(
        self,
        elem: ET.Element,
        attrs: dict[str, str],
        name: str,
        docstring: str | None,
    ) -> Class:
        model = Class(
            name=name,
            kind=attrs.get("kind"),
            is_template=False,
            bases=self._extract_class_bases(elem),
            docstring=docstring,
            cpp_type=attrs.get("classtype") or attrs.get("name"),
        )
        # Populate nested children
        children = self.children_by_parent.pop(elem, [])
        for child in children:
            if isinstance(child, CDecl):
                model.cdecls.append(child)
            elif isinstance(child, Constructor):
                model.constructors.append(child)
            elif isinstance(child, Destructor):
                model.destructors.append(child)
            elif isinstance(child, Enum):
                model.enums.append(child)
            elif isinstance(child, Class):
                model.classes.append(child)
        return model

    def _get_attrs(self, node: ET.Element) -> dict[str, str]:
        attrs: dict[str, str] = {}
        attr_list = node.find("attributelist")
        if attr_list is not None:
            for a in attr_list.findall("attribute"):
                val = a.get("value")
                name = a.get("name")
                if name and val is not None:
                    attrs[name] = val
        return attrs

    def _extract_class_bases(self, elem: ET.Element) -> list[str]:
        bases: list[str] = []

        def add_bases(bl_node: ET.Element) -> None:
            for base in bl_node.findall("base"):
                b_name = base.get("name")
                if b_name:
                    bases.append(b_name)

        if (bl := elem.find("baselist")) is not None:
            add_bases(bl)

        if (al := elem.find("attributelist")) is not None and (
            bl := al.find("baselist")
        ) is not None:
            add_bases(bl)
        return bases

    def _extract_parms(self, node: ET.Element) -> list[Parm]:
        parms: list[Parm] = []

        def scan(parent: ET.Element) -> None:
            for child in parent:
                if child.tag == "parm":
                    attrs = self._get_attrs(child)
                    parms.append(
                        Parm(
                            name=attrs.get("name"),
                            type=attrs.get("type"),
                            value=attrs.get("value"),
                        )
                    )
                elif child.tag == "parmlist":
                    scan(child)

        scan(node)
        attr_list = node.find("attributelist")
        if attr_list is not None:
            scan(attr_list)
        return parms

    def _extract_enum_items(self, elem: ET.Element) -> list[EnumItem]:
        items: list[EnumItem] = []
        for child in elem:
            if child.tag == "enumitem":
                attrs = self._get_attrs(child)
                name = attrs.get("sym_name") or attrs.get("name", "")
                items.append(
                    EnumItem(
                        name=name,
                        value=attrs.get("enumvalue"),
                    )
                )
        return items


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
