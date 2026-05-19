from sqlmodel import Session, SQLModel, create_engine

from swig2pyi.core.builder import AstBuilder
from swig2pyi.core.schema import BaseClass as DbBaseClass
from swig2pyi.core.schema import Node as DbNode
from swig2pyi.core.schema import Parm as DbParm
from swig2pyi.core.schema import TopInfo as DbTopInfo


def test_build_ast_from_db() -> None:
    engine = create_engine("sqlite:///:memory:")
    SQLModel.metadata.create_all(engine)

    # Pre-populate DB
    with Session(engine) as session:
        session.add(DbTopInfo(module_name="test_ast"))

        class_node = DbNode(tag="class", name="MyASTClass", kind="class")
        session.add(class_node)
        session.flush()

        # Add a base class
        base = DbBaseClass(node_id=class_node.id, name="MyBase")
        session.add(base)

        # Add a method
        method_node = DbNode(
            parent_class_id=class_node.id,
            tag="cdecl",
            name="astMethod",
            kind="function",
            type="int",
        )
        session.add(method_node)
        session.flush()

        # Add a parm
        parm = DbParm(node_id=method_node.id, name="p1", type="float", idx=0)
        session.add(parm)
        session.commit()

    builder = AstBuilder()
    top = builder.build(engine)

    # Assertions
    assert top.module is not None
    assert top.module.name == "test_ast"

    assert len(top.module.classes) == 1
    cls = top.module.classes[0]
    assert cls.name == "MyASTClass"
    assert cls.bases == ["MyBase"]

    assert len(cls.cdecls) == 1
    func = cls.cdecls[0]
    assert func.name == "astMethod"
    assert func.type == "int"

    assert len(func.parms) == 1
    assert func.parms[0].name == "p1"
    assert func.parms[0].type == "float"
