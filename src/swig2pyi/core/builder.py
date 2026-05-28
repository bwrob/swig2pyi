"""AST builder for reconstructing the Pydantic AST from SQLite."""

from __future__ import annotations

from collections.abc import Iterable
from typing import TYPE_CHECKING, Any, cast

from sqlmodel import Session, col, select

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
    from sqlalchemy import Engine


class AstBuilder:
    """Reconstructs the Pydantic AST from the SQLite database."""

    def build(self, engine: Engine) -> Top:
        """Build AST from database."""
        with Session(engine) as session:
            top_info = session.exec(select(DbTopInfo.module_name)).first()
            module = Module(name=top_info or "Unknown")

            parms = self._load_parms(session)
            enums = self._load_enums(session)
            bases = self._load_bases(session)

            nodes_by_id = self._load_nodes(session, parms, enums, bases)
            self._assemble_tree(module, nodes_by_id)
            self._load_python_code(session, module)

            return Top(module=module)

    def _load_parms(self, session: Session) -> dict[int, list[Parm]]:
        parms: dict[int, list[Parm]] = {}
        select_stmt = cast(
            Any,  # noqa: TC006
            select(DbParm.node_id, DbParm.name, DbParm.type, DbParm.value),
        )
        rows = cast(
            Iterable[tuple[int | None, str | None, str | None, str | None]],  # noqa: TC006
            session.exec(select_stmt.order_by(DbParm.node_id, DbParm.idx)),
        )
        for node_id, p_name, p_type, p_value in rows:
            n_id = node_id or 0
            if n_id not in parms:
                parms[n_id] = []
            parms[n_id].append(Parm(name=p_name, type=p_type, value=p_value))
        return parms

    def _load_enums(self, session: Session) -> dict[int, list[EnumItem]]:
        enums: dict[int, list[EnumItem]] = {}
        select_stmt = cast(
            Any,  # noqa: TC006
            select(DbEnumItem.node_id, DbEnumItem.name, DbEnumItem.value),
        )
        rows = cast(
            Iterable[tuple[int | None, str, str | None]],  # noqa: TC006
            session.exec(select_stmt.order_by(DbEnumItem.id)),
        )
        for node_id, e_name, e_value in rows:
            n_id = node_id or 0
            if n_id not in enums:
                enums[n_id] = []
            enums[n_id].append(EnumItem(name=e_name, value=e_value))
        return enums

    def _load_bases(self, session: Session) -> dict[int, list[str]]:
        bases: dict[int, list[str]] = {}
        select_stmt = cast(Any, select(DbBaseClass.node_id, DbBaseClass.name))  # noqa: TC006
        rows = cast(
            Iterable[tuple[int | None, str]],  # noqa: TC006
            session.exec(select_stmt.order_by(DbBaseClass.id)),
        )
        for node_id, b_name in rows:
            n_id = node_id or 0
            if n_id not in bases:
                bases[n_id] = []
            bases[n_id].append(b_name)
        return bases

    def _load_nodes(
        self,
        session: Session,
        parms: dict[int, list[Parm]],
        enums: dict[int, list[EnumItem]],
        bases: dict[int, list[str]],
    ) -> dict[int, tuple[int | None, str, AstModel]]:
        nodes_by_id: dict[int, tuple[int | None, str, AstModel]] = {}
        select_stmt = cast(Any, select)(  # noqa: TC006
            DbNode.id,
            DbNode.parent_class_id,
            DbNode.tag,
            DbNode.name,
            DbNode.kind,
            DbNode.type,
            DbNode.decl,
            DbNode.is_template,
            DbNode.is_static,
            DbNode.docstring,
        )
        rows = cast(
            Iterable[  # noqa: TC006
                tuple[
                    int | None,
                    int | None,
                    str,
                    str,
                    str | None,
                    str | None,
                    str | None,
                    bool,
                    bool,
                    str | None,
                ]
            ],
            session.exec(
                select_stmt.where(
                    col(DbNode.feature_ignore) == False,  # noqa: E712
                    col(DbNode.parent_template_id).is_(None),
                )
            ),
        )

        for (
            db_id,
            p_class_id,
            tag,
            name,
            kind,
            type_,
            decl,
            is_template,
            is_static,
            docstring,
        ) in rows:
            if db_id is None:
                continue
            model = self._create_model(
                db_id,
                tag,
                name,
                kind,
                type_,
                decl,
                is_template,
                is_static,
                docstring,
                parms,
                enums,
                bases,
            )
            if model:
                nodes_by_id[db_id] = (
                    p_class_id,
                    tag,
                    model,
                )
        return nodes_by_id

    def _load_python_code(self, session: Session, module: Module) -> None:
        for code in session.exec(select(DbPythonCode.code)):
            module.python_code.append(code)

    def _create_model(  # noqa: PLR0913
        self,
        node_id: int,
        tag: str,
        name: str,
        kind: str | None,
        type_: str | None,
        decl: str | None,
        is_template: bool,  # noqa: FBT001
        is_static: bool,  # noqa: FBT001
        docstring: str | None,
        parms: dict[int, list[Parm]],
        enums: dict[int, list[EnumItem]],
        bases: dict[int, list[str]],
    ) -> AstModel | None:
        result = None
        if tag == "cdecl":
            if kind in ("function", "variable"):
                result = CDecl(
                    name=name,
                    type=type_,
                    kind=kind,
                    decl=decl,
                    parms=parms.get(node_id) or [],
                    is_static=is_static,
                    docstring=docstring,
                )
        elif tag == "constructor":
            result = Constructor(
                name=name,
                parms=parms.get(node_id) or [],
                is_static=is_static,
                docstring=docstring,
            )
        elif tag == "destructor":
            result = Destructor(
                name=name,
                is_static=is_static,
                docstring=docstring,
            )
        elif tag == "enum":
            result = Enum(
                name=name,
                items=enums.get(node_id) or [],
                docstring=docstring,
            )
        elif tag == "class":
            result = Class(
                name=name,
                kind=kind,
                is_template=is_template,
                bases=bases.get(node_id) or [],
                docstring=docstring,
                cpp_type=type_,
            )
        return result

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

        if tag in ("cdecl", "constructor", "destructor"):
            self._add_callable_to_parent(p_model, tag, model)
        elif tag in ("enum", "class"):
            self._add_type_to_parent(p_model, tag, model)

    def _add_callable_to_parent(
        self, p_model: Class, tag: str, model: AstModel
    ) -> None:
        if tag == "cdecl" and isinstance(model, CDecl):
            p_model.cdecls.append(model)
        elif tag == "constructor" and isinstance(model, Constructor):
            p_model.constructors.append(model)
        elif tag == "destructor" and isinstance(model, Destructor):
            p_model.destructors.append(model)

    def _add_type_to_parent(self, p_model: Class, tag: str, model: AstModel) -> None:
        if tag == "enum" and isinstance(model, Enum):
            p_model.enums.append(model)
        elif tag == "class" and isinstance(model, Class):
            p_model.classes.append(model)
