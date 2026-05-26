import os
import tempfile

from sqlmodel import Session, select

from swig2pyi.core.ingestion import XmlIngestor
from swig2pyi.core.schema import Node, TopInfo


def test_stream_to_db() -> None:
    xml_content = """<?xml version="1.0" ?>
    <top>
        <attributelist><attribute name="module" value="test_module"/></attributelist>
        <class>
            <attributelist><attribute name="name" value="TestClass"/><attribute name="kind" value="class"/></attributelist>
            <cdecl>
                <attributelist><attribute name="name" value="testMethod"/><attribute name="kind" value="function"/><attribute name="type" value="void"/></attributelist>
                <parmlist>
                    <parm>
                        <attributelist><attribute name="name" value="x"/><attribute name="type" value="int"/></attributelist>
                    </parm>
                </parmlist>
            </cdecl>
        </class>
    </top>
    """

    # Write to a temp file
    fd, path = tempfile.mkstemp(suffix=".xml")
    with os.fdopen(fd, "w") as f:
        f.write(xml_content)

    ingestor = XmlIngestor()
    try:
        engine = ingestor.run(path)

        with Session(engine) as session:
            # Check TopInfo
            top = session.exec(select(TopInfo)).first()
            assert top is not None
            assert top.module_name == "test_module"

            # Check Class Node
            class_node = session.exec(select(Node).where(Node.tag == "class")).first()
            assert class_node is not None
            assert class_node.name == "TestClass"
            assert class_node.kind == "class"

            # Check Method Node
            method_node = session.exec(select(Node).where(Node.tag == "cdecl")).first()
            assert method_node is not None
            assert method_node.name == "testMethod"
            assert method_node.parent_class_id == class_node.id
            assert method_node.type == "void"

            # Check Parameters
            assert len(method_node.parms) == 1
            assert method_node.parms[0].name == "x"
            assert method_node.parms[0].type == "int"

    finally:
        os.remove(path)
