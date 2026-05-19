"""SWIG XML parser using relational streaming ingestion."""

from __future__ import annotations

import io
import xml.etree.ElementTree as ET
from typing import TYPE_CHECKING, Any, TypeAlias, TypeVar

if TYPE_CHECKING:
    from collections.abc import Callable
    from pathlib import Path

from pydantic import BaseModel
from sqlalchemy import Engine, create_engine
from sqlmodel import Session, SQLModel, select, text

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
    TopInfo as DbTopInfo,
)

AstModel: TypeAlias = (
    "CDecl | Constructor | Destructor | Enum | Class | Module | Top | EnumItem | Parm"
)

T = TypeVar("T", bound=SQLModel)


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


class Module(BaseModel):
    """AST model for a SWIG module."""

    name: str
    enums: list[Enum] = []
    classes: list[Class] = []
    cdecls: list[CDecl] = []


class Top(BaseModel):
    """Root of the AST."""

    module: Module | None = None


class SwigXmlParser:
    """Parses SWIG XML using a streaming SQLite ingestion strategy."""

    def __init__(self) -> None:
        """Initialize parser."""
        self.node_id_seq = 1

    def parse_file(self, xml_path: Path, db_path: Path | None = None) -> Top:
        """Parse a SWIG XML file and return the AST."""
        engine = self._run_parser(xml_path, db_path)
        return self._build_ast_from_db(engine)

    def parse_string(self, xml_content: str, db_path: Path | None = None) -> Top:
        """Parse SWIG XML content from a string and return the AST."""
        source = io.BytesIO(xml_content.encode("utf-8"))
        engine = self._run_parser(source, db_path)
        return self._build_ast_from_db(engine)

    def _run_parser(
        self, source: str | Path | io.BytesIO, db_path: Path | None = None
    ) -> Engine:
        if db_path:
            url = f"sqlite:///{db_path}"
            if db_path.exists():
                db_path.unlink()
        else:
            url = "sqlite://"

        engine = create_engine(url)
        SQLModel.metadata.create_all(engine)
        self._stream_to_db(source, engine)
        return engine

    def _get_attrs(self, node: ET.Element) -> dict[str, str]:
        attrs = {}
        attr_list = node.find("attributelist")
        if attr_list is not None:
            for a in attr_list.findall("attribute"):
                val = a.get("value")
                name = a.get("name")
                if name and val is not None:
                    attrs[name] = val
        return attrs

    def _extract_parms(self, node: ET.Element, node_id: int, session: Session) -> None:
        def scan(parent: ET.Element, idx_counter: list[int]) -> None:
            for child in parent:
                if child.tag == "parm":
                    attrs = self._get_attrs(child)
                    session.add(
                        DbParm(
                            node_id=node_id,
                            name=attrs.get("name"),
                            type=attrs.get("type"),
                            idx=idx_counter[0],
                        )
                    )
                    idx_counter[0] += 1
                elif child.tag == "parmlist":
                    scan(child, idx_counter)

        counter = [0]
        scan(node, counter)
        attr_list = node.find("attributelist")
        if attr_list is not None:
            scan(attr_list, counter)

    def _stream_to_db(self, source: str | Path | io.BytesIO, engine: Engine) -> None:
        context = ET.iterparse(source, events=("start", "end"))  # noqa: S314
        stack: list[tuple[ET.Element, int]] = []
        class_stack: list[int] = []
        template_stack: list[int] = []
        self.node_id_seq = 1

        with Session(engine) as session:
            for event, elem in context:
                if event == "start":
                    self._handle_start(elem, stack, class_stack, template_stack)
                else:
                    self._handle_end(elem, stack, class_stack, template_stack, session)

            session.exec(
                text(
                    "DELETE FROM nodes WHERE tag = 'cdecl' AND parent_template_id IN "
                    "(SELECT parent_template_id FROM nodes WHERE tag = 'class' "
                    "AND parent_template_id IS NOT NULL)"
                )
            )
            session.commit()

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
        session: Session,
    ) -> None:
        _, node_id = stack.pop()
        if elem.tag == "class":
            class_stack.pop()
        elif elem.tag == "template":
            template_stack.pop()

        p_class_id = class_stack[-1] if class_stack else None
        p_template_id = template_stack[-1] if template_stack else None
        self._process_node(elem, node_id, p_class_id, p_template_id, session)

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

    def _process_node(
        self,
        elem: ET.Element,
        node_id: int,
        parent_class_id: int | None,
        parent_template_id: int | None,
        session: Session,
    ) -> None:
        if elem.tag == "top":
            session.add(
                DbTopInfo(module_name=self._get_attrs(elem).get("module", "Unknown"))
            )

        if elem.tag not in ("class", "cdecl", "enum", "constructor", "destructor"):
            return

        attrs = self._get_attrs(elem)
        name = attrs.get("sym_name") or attrs.get("name", "")
        if not name and elem.tag == "class":
            return

        db_node = DbNode(
            id=node_id,
            parent_class_id=parent_class_id,
            parent_template_id=parent_template_id,
            tag=elem.tag,
            name=name,
            kind=attrs.get("kind"),
            type=attrs.get("type"),
            decl=attrs.get("decl"),
            feature_ignore=attrs.get("feature_ignore") == "1",
            is_template=parent_template_id is not None,
            is_static=attrs.get("storage") == "static",
            docstring=attrs.get("feature_docstring"),
        )
        session.add(db_node)
        self._dispatch_extraction(elem, node_id, session)

    def _dispatch_extraction(
        self, elem: ET.Element, node_id: int, session: Session
    ) -> None:
        if elem.tag in ("cdecl", "constructor"):
            self._extract_parms(elem, node_id, session)
        elif elem.tag == "enum":
            self._extract_enum_items(elem, node_id, session)
        elif elem.tag == "class":
            self._extract_class_bases(elem, node_id, session)

    def _extract_enum_items(
        self, elem: ET.Element, node_id: int, session: Session
    ) -> None:
        for child in elem:
            if child.tag == "enumitem":
                attrs = self._get_attrs(child)
                session.add(
                    DbEnumItem(
                        node_id=node_id,
                        name=attrs.get("name", ""),
                        value=attrs.get("enumvalue"),
                    )
                )

    def _extract_class_bases(
        self, elem: ET.Element, node_id: int, session: Session
    ) -> None:
        def add_bases(bl_node: ET.Element) -> None:
            for base in bl_node.findall("base"):
                b_name = base.get("name")
                if b_name:
                    session.add(DbBaseClass(node_id=node_id, name=b_name))

        if (bl := elem.find("baselist")) is not None:
            add_bases(bl)

        if (al := elem.find("attributelist")) is not None and (
            bl := al.find("baselist")
        ) is not None:
            add_bases(bl)

    def _build_ast_from_db(self, engine: Engine) -> Top:
        with Session(engine) as session:
            top_info = session.exec(select(DbTopInfo)).first()
            module = Module(name=top_info.module_name if top_info else "Unknown")

            parms = self._load_dict(
                session,
                DbParm,
                lambda p: (p.node_id or 0, Parm(name=p.name, type=p.type)),
            )
            enums = self._load_dict(
                session,
                DbEnumItem,
                lambda e: (e.node_id or 0, EnumItem(name=e.name, value=e.value)),
            )
            bases = self._load_dict(
                session,
                DbBaseClass,
                lambda b: (b.node_id or 0, b.name),
            )

            nodes_by_id = {}
            for db_node in session.exec(
                select(DbNode).where(DbNode.feature_ignore == False)  # noqa: E712
            ):
                model = self._create_model(db_node, parms, enums, bases)
                if model:
                    nodes_by_id[db_node.id] = (
                        db_node.parent_class_id,
                        db_node.tag,
                        model,
                    )

            self._assemble_tree(module, nodes_by_id)
            return Top(module=module)

    def _load_dict(
        self,
        session: Session,
        model_type: type[T],
        mapper: Callable[[T], tuple[int, Any]],
    ) -> dict[int, list[Any]]:
        res: dict[int, list[Any]] = {}
        for item in session.exec(select(model_type)):
            key, val = mapper(item)
            res.setdefault(key, []).append(val)
        return res

    def _create_model(
        self,
        db_node: DbNode,
        parms: dict[int, list[Parm]],
        enums: dict[int, list[EnumItem]],
        bases: dict[int, list[str]],
    ) -> AstModel | None:
        if db_node.tag == "cdecl":
            if db_node.kind in ("function", "variable"):
                return CDecl(
                    name=db_node.name,
                    type=db_node.type,
                    kind=db_node.kind,
                    decl=db_node.decl,
                    parms=parms.get(db_node.id, []),
                    is_static=db_node.is_static,
                    docstring=db_node.docstring,
                )
        elif db_node.tag == "constructor":
            return Constructor(
                name=db_node.name,
                parms=parms.get(db_node.id, []),
                is_static=db_node.is_static,
                docstring=db_node.docstring,
            )
        elif db_node.tag == "destructor":
            return Destructor(
                name=db_node.name,
                is_static=db_node.is_static,
                docstring=db_node.docstring,
            )
        elif db_node.tag == "enum":
            return Enum(
                name=db_node.name,
                items=enums.get(db_node.id, []),
                docstring=db_node.docstring,
            )
        elif db_node.tag == "class":
            return Class(
                name=db_node.name,
                kind=db_node.kind,
                is_template=db_node.is_template,
                bases=bases.get(db_node.id, []),
                docstring=db_node.docstring,
            )
        return None

    def _assemble_tree(
        self, module: Module, nodes_by_id: dict[int, tuple[int | None, str, AstModel]]
    ) -> None:
        for parent_id, tag, model in nodes_by_id.values():
            if parent_id is None:
                self._add_to_module(module, tag, model)
            elif (parent := nodes_by_id.get(parent_id)) and (p_model := parent[2]):
                self._add_to_parent(p_model, tag, model)

    def _add_to_module(self, module: Module, tag: str, model: AstModel) -> None:
        if tag == "cdecl" and isinstance(model, CDecl):
            module.cdecls.append(model)
        elif tag == "class" and isinstance(model, Class):
            module.classes.append(model)
        elif tag == "enum" and isinstance(model, Enum):
            module.enums.append(model)

    def _add_to_parent(
        self,
        p_model: AstModel,
        tag: str,
        model: AstModel,
    ) -> None:
        if not isinstance(p_model, Class):
            return

        if tag == "cdecl" and isinstance(model, CDecl):
            p_model.cdecls.append(model)
        elif tag == "constructor" and isinstance(model, Constructor):
            p_model.constructors.append(model)
        elif tag == "destructor" and isinstance(model, Destructor):
            p_model.destructors.append(model)
        elif tag == "enum" and isinstance(model, Enum):
            p_model.enums.append(model)
        elif tag == "class" and isinstance(model, Class):
            p_model.classes.append(model)
