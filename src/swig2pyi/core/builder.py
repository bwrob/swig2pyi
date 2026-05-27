"""AST builder for reconstructing the Pydantic AST from SQLite."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, TypeVar

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
    from collections.abc import Callable

    from sqlalchemy import Engine

    from .schema import SQLModel

T = TypeVar("T", bound="SQLModel")


class AstBuilder:
    """Reconstructs the Pydantic AST from the SQLite database."""

    def build(self, engine: Engine) -> Top:
        """Build AST from database."""
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

            nodes_by_id: dict[int, tuple[int | None, str, AstModel]] = {}
            for db_node in session.exec(
                select(DbNode).where(
                    DbNode.feature_ignore == False,  # noqa: E712
                    col(DbNode.parent_template_id).is_(None),
                )
            ):
                model = self._create_model(db_node, parms, enums, bases)
                if model and db_node.id is not None:
                    nodes_by_id[db_node.id] = (
                        db_node.parent_class_id,
                        db_node.tag,
                        model,
                    )

            self._assemble_tree(module, nodes_by_id)

            # Load %pythoncode blocks
            for pc in session.exec(select(DbPythonCode)):
                module.python_code.append(pc.code)

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
            if key not in res:
                res[key] = []
            res[key].append(val)
        return res

    def _create_model(
        self,
        db_node: DbNode,
        parms: dict[int, list[Parm]],
        enums: dict[int, list[EnumItem]],
        bases: dict[int, list[str]],
    ) -> AstModel | None:
        if db_node.id is None:
            return None
        node_id = db_node.id
        result = None
        if db_node.tag == "cdecl":
            if db_node.kind in ("function", "variable"):
                result = CDecl(
                    name=db_node.name,
                    type=db_node.type,
                    kind=db_node.kind,
                    decl=db_node.decl,
                    parms=parms.get(node_id) or [],
                    is_static=db_node.is_static,
                    docstring=db_node.docstring,
                )
        elif db_node.tag == "constructor":
            result = Constructor(
                name=db_node.name,
                parms=parms.get(node_id) or [],
                is_static=db_node.is_static,
                docstring=db_node.docstring,
            )
        elif db_node.tag == "destructor":
            result = Destructor(
                name=db_node.name,
                is_static=db_node.is_static,
                docstring=db_node.docstring,
            )
        elif db_node.tag == "enum":
            result = Enum(
                name=db_node.name,
                items=enums.get(node_id) or [],
                docstring=db_node.docstring,
            )
        elif db_node.tag == "class":
            result = Class(
                name=db_node.name,
                kind=db_node.kind,
                is_template=db_node.is_template,
                bases=bases.get(node_id) or [],
                docstring=db_node.docstring,
                cpp_type=db_node.type,
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
