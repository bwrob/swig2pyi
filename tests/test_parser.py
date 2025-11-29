import pytest
from swig2pyi.core.parser import SwigXmlParser

def test_parse_simple_xml():
    xml = """
    <top>
        <module name="QuantLib">
            <class name="Date">
                <constructor name="Date">
                   <parm type="int" name="d"/>
                </constructor>
                <cdecl kind="function" name="dayOfMonth" type="int"/>
            </class>
            <cdecl kind="function" name="testGlobal" type="void"/>
        </module>
    </top>
    """
    parser = SwigXmlParser()
    top = parser.parse(xml)
    assert top.module is not None
    assert top.module.name == "QuantLib"
    assert len(top.module.classes) == 1
    
    cls = top.module.classes[0]
    assert cls.name == "Date"
    assert len(cls.constructors) == 1
    assert cls.constructors[0].parms[0].name == "d"
    assert cls.constructors[0].parms[0].type == "int"
    
    assert len(cls.cdecls) == 1
    assert cls.cdecls[0].name == "dayOfMonth"
    assert cls.cdecls[0].type == "int"

    assert len(top.module.cdecls) == 1
    assert top.module.cdecls[0].name == "testGlobal"
