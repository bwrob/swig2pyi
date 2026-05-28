"""XML ingestion logic for SWIG XML files."""

from __future__ import annotations

import xml.etree.ElementTree as ET
from typing import TYPE_CHECKING, Any

from sqlalchemy import StaticPool, insert, text
from sqlmodel import Session, SQLModel, create_engine

from .schema import (
    BaseClass as DbBaseClass,
)
from .schema import (
    EnumItem as DbEnumItem,
)
from .schema import (
    Node as DbNode,
)
from .schema import (
    Parm as DbParm,
)
from .schema import (
    PythonCode as DbPythonCode,
)
from .schema import (
    TopInfo as DbTopInfo,
)

if TYPE_CHECKING:
    import io
    from collections.abc import Iterable
    from pathlib import Path

    from sqlalchemy import Engine


class XmlIngestor:
    """Streams SWIG XML into a SQLite database."""

    def __init__(self) -> None:
        """Initialize ingestor."""
        self.node_id_seq = 1
        self.nodes_to_insert: list[dict[str, Any]] = []
        self.parms_to_insert: list[dict[str, Any]] = []
        self.enum_items_to_insert: list[dict[str, Any]] = []
        self.base_classes_to_insert: list[dict[str, Any]] = []
        self.top_infos_to_insert: list[dict[str, Any]] = []
        self.python_codes_to_insert: list[dict[str, Any]] = []

    def run(
        self, source: str | Path | io.BytesIO, db_path: Path | None = None
    ) -> Engine:
        """Run ingestion process."""
        if db_path:
            url = f"sqlite:///{db_path}"
            if db_path.exists():
                db_path.unlink()
            engine = create_engine(url)
        else:
            url = "sqlite://"
            engine = create_engine(
                url,
                connect_args={"check_same_thread": False},
                poolclass=StaticPool,
            )

        SQLModel.metadata.create_all(engine)
        self._stream_to_db(source, engine)
        return engine

    def _stream_to_db(self, source: str | Path | io.BytesIO, engine: Engine) -> None:
        context = ET.iterparse(source, events=("start", "end"))  # noqa: S314
        stack: list[tuple[ET.Element, int]] = []
        class_stack: list[int] = []
        template_stack: list[int] = []
        self.node_id_seq = 1

        self.nodes_to_insert.clear()
        self.parms_to_insert.clear()
        self.enum_items_to_insert.clear()
        self.base_classes_to_insert.clear()
        self.top_infos_to_insert.clear()
        self.python_codes_to_insert.clear()

        with Session(engine) as session:
            self._parse_loop(context, stack, class_stack, template_stack)
            self._execute_bulk_inserts(session)

            session.execute(  # pyright: ignore [reportDeprecated]
                text(
                    "DELETE FROM nodes WHERE tag = 'cdecl' AND parent_template_id IN "
                    "(SELECT parent_template_id FROM nodes WHERE tag = 'class' "
                    "AND parent_template_id IS NOT NULL)"
                )
            )
            session.commit()

    def _parse_loop(
        self,
        context: Iterable[tuple[str, ET.Element]],
        stack: list[tuple[ET.Element, int]],
        class_stack: list[int],
        template_stack: list[int],
    ) -> None:
        for event, elem in context:
            if event == "start":
                self._handle_start(elem, stack, class_stack, template_stack)
            else:
                self._handle_end(elem, stack, class_stack, template_stack)

    def _execute_bulk_inserts(self, session: Session) -> None:
        if self.top_infos_to_insert:
            session.execute(insert(DbTopInfo), self.top_infos_to_insert)  # pyright: ignore [reportDeprecated]
        if self.python_codes_to_insert:
            session.execute(insert(DbPythonCode), self.python_codes_to_insert)  # pyright: ignore [reportDeprecated]
        if self.nodes_to_insert:
            session.execute(insert(DbNode), self.nodes_to_insert)  # pyright: ignore [reportDeprecated]
        if self.parms_to_insert:
            session.execute(insert(DbParm), self.parms_to_insert)  # pyright: ignore [reportDeprecated]
        if self.enum_items_to_insert:
            session.execute(insert(DbEnumItem), self.enum_items_to_insert)  # pyright: ignore [reportDeprecated]
        if self.base_classes_to_insert:
            session.execute(insert(DbBaseClass), self.base_classes_to_insert)  # pyright: ignore [reportDeprecated]

    def _handle_start(
        self,
        elem: ET.Element,
        stack: list[tuple[ET.Element, int]],
        class_stack: list[int],
        template_stack: list[int],
    ) -> None:
        node_id = self.node_id_seq
        stack.append((elem, node_id))
        self.node_id_seq += 1
        if elem.tag == "class":
            class_stack.append(node_id)
        elif elem.tag == "template":
            template_stack.append(node_id)

    def _handle_end(
        self,
        elem: ET.Element,
        stack: list[tuple[ET.Element, int]],
        class_stack: list[int],
        template_stack: list[int],
    ) -> None:
        _, node_id = stack.pop()
        if elem.tag == "class":
            class_stack.pop()
        elif elem.tag == "template":
            template_stack.pop()

        p_class_id = class_stack[-1] if class_stack else None
        p_template_id = template_stack[-1] if template_stack else None
        self._process_node(elem, node_id, p_class_id, p_template_id)

        if elem.tag in (
            "class",
            "cdecl",
            "enum",
            "constructor",
            "destructor",
            "template",
            "include",
            "namespace",
            "module",
        ):
            elem.clear()
            if stack:
                stack[-1][0].remove(elem)

    def _process_top(self, elem: ET.Element) -> None:
        self.top_infos_to_insert.append(
            {"module_name": self._get_attrs(elem).get("module", "Unknown")}
        )

    def _process_insert(self, elem: ET.Element) -> None:
        attrs = self._get_attrs(elem)
        if attrs.get("section") == "python" and "code" in attrs:
            code = attrs["code"].strip()
            if code:
                self.python_codes_to_insert.append({"code": code})

    def _process_node(
        self,
        elem: ET.Element,
        node_id: int,
        parent_class_id: int | None,
        parent_template_id: int | None,
    ) -> None:
        if elem.tag == "top":
            self._process_top(elem)

        if elem.tag == "insert":
            self._process_insert(elem)

        if elem.tag not in ("class", "cdecl", "enum", "constructor", "destructor"):
            return

        attrs = self._get_attrs(elem)
        name = attrs.get("sym_name") or attrs.get("name", "")
        if not name and elem.tag == "class":
            return

        self.nodes_to_insert.append(
            {
                "id": node_id,
                "parent_class_id": parent_class_id,
                "parent_template_id": parent_template_id,
                "tag": elem.tag,
                "name": name,
                "kind": attrs.get("kind"),
                "type": attrs.get("classtype") or attrs.get("name")
                if elem.tag == "class"
                else attrs.get("type"),
                "decl": attrs.get("decl"),
                "feature_ignore": attrs.get("feature_ignore") == "1",
                "is_template": parent_template_id is not None,
                "is_static": attrs.get("storage") == "static",
                "docstring": attrs.get("feature_docstring"),
            }
        )
        self._dispatch_extraction(elem, node_id)

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

    def _dispatch_extraction(self, elem: ET.Element, node_id: int) -> None:
        if elem.tag in ("cdecl", "constructor"):
            self._extract_parms(elem, node_id)
        elif elem.tag == "enum":
            self._extract_enum_items(elem, node_id)
        elif elem.tag == "class":
            self._extract_class_bases(elem, node_id)

    def _extract_parms(self, node: ET.Element, node_id: int) -> None:
        def scan(parent: ET.Element, idx_counter: list[int]) -> None:
            for child in parent:
                if child.tag == "parm":
                    attrs = self._get_attrs(child)
                    self.parms_to_insert.append(
                        {
                            "node_id": node_id,
                            "name": attrs.get("name"),
                            "type": attrs.get("type"),
                            "value": attrs.get("value"),
                            "idx": idx_counter[0],
                        }
                    )
                    idx_counter[0] += 1
                elif child.tag == "parmlist":
                    scan(child, idx_counter)

        counter = [0]
        scan(node, counter)
        attr_list = node.find("attributelist")
        if attr_list is not None:
            scan(attr_list, counter)

    def _extract_enum_items(self, elem: ET.Element, node_id: int) -> None:
        for child in elem:
            if child.tag == "enumitem":
                attrs = self._get_attrs(child)
                name = attrs.get("sym_name") or attrs.get("name", "")
                self.enum_items_to_insert.append(
                    {
                        "node_id": node_id,
                        "name": name,
                        "value": attrs.get("enumvalue"),
                    }
                )

    def _extract_class_bases(self, elem: ET.Element, node_id: int) -> None:
        def add_bases(bl_node: ET.Element) -> None:
            for base in bl_node.findall("base"):
                b_name = base.get("name")
                if b_name:
                    self.base_classes_to_insert.append(
                        {
                            "node_id": node_id,
                            "name": b_name,
                        }
                    )

        if (bl := elem.find("baselist")) is not None:
            add_bases(bl)

        if (al := elem.find("attributelist")) is not None and (
            bl := al.find("baselist")
        ) is not None:
            add_bases(bl)
