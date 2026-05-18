from sqlmodel import Session, SQLModel, create_engine, select

from swig2pyi.core.schema import Node, Parm, EnumItem, BaseClass

def test_create_db_and_insert_node():
    engine = create_engine("sqlite:///:memory:")
    SQLModel.metadata.create_all(engine)
    
    with Session(engine) as session:
        # Create a class node
        class_node = Node(
            tag="class",
            name="MyClass",
            kind="class",
            is_template=False,
            feature_ignore=False
        )
        session.add(class_node)
        session.commit()
        session.refresh(class_node)
        
        assert class_node.id is not None
        
        # Create a method node linked to the class
        method_node = Node(
            parent_class_id=class_node.id,
            tag="cdecl",
            name="myMethod",
            kind="function",
            type="void",
            decl="void myMethod(int x)",
            feature_ignore=False,
            is_template=False,
            parms=[
                Parm(
                    name="x",
                    type="int",
                    idx=0
                )
            ]
        )
        session.add(method_node)
        session.commit()

    with Session(engine) as session:
        # Verify
        statement = select(Node).where(Node.tag == "cdecl")
        result = session.exec(statement).first()
        
        assert result is not None
        assert result.name == "myMethod"
        assert result.parent_class_id == class_node.id
        assert len(result.parms) == 1
        assert result.parms[0].name == "x"
