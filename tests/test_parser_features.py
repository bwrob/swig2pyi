from swig2pyi.core.parser import SwigXmlParser


def test_parse_nested_parmlist() -> None:
    xml = """
    <top>
        <attributelist><attribute name="module" value="Test"/></attributelist>
        <module>
            <class>
                <attributelist><attribute name="name" value="Complex"/></attributelist>
                <cdecl>
                    <attributelist>
                        <attribute name="kind" value="function"/>
                        <attribute name="name" value="add"/>
                        <attribute name="type" value="void"/>
                        <parmlist>
                            <parm>
                                <attributelist>
                                    <attribute name="name" value="x"/>
                                    <attribute name="type" value="int"/>
                                </attributelist>
                            </parm>
                        </parmlist>
                    </attributelist>
                </cdecl>
            </class>
        </module>
    </top>
    """
    parser = SwigXmlParser()
    top = parser.parse_string(xml)
    cls = top.module.classes[0]
    method = cls.cdecls[0]
    assert method.name == "add"
    assert len(method.parms) == 1
    assert method.parms[0].name == "x"
    assert method.parms[0].type == "int"


def test_parse_overloads_structure() -> None:
    xml = """
    <top>
        <attributelist><attribute name="module" value="Test"/></attributelist>
        <module>
            <class>
                <attributelist><attribute name="name" value="Math"/></attributelist>
                <cdecl>
                    <attributelist>
                         <attribute name="kind" value="function"/>
                         <attribute name="name" value="compute"/>
                         <attribute name="type" value="int"/>
                         <attribute name="decl" value="f(int)."/>
                    </attributelist>
                </cdecl>
                <cdecl>
                    <attributelist>
                         <attribute name="kind" value="function"/>
                         <attribute name="name" value="compute"/>
                         <attribute name="type" value="int"/>
                         <attribute name="decl" value="f(double)."/>
                    </attributelist>
                </cdecl>
            </class>
        </module>
    </top>
    """
    parser = SwigXmlParser()
    top = parser.parse_string(xml)
    cls = top.module.classes[0]
    assert len(cls.cdecls) == 2
    assert cls.cdecls[0].name == "compute"
    assert cls.cdecls[1].name == "compute"


def test_parse_member_variables() -> None:
    xml = """
    <top>
        <attributelist><attribute name="module" value="Test"/></attributelist>
        <module>
            <class>
                <attributelist><attribute name="name" value="Point"/></attributelist>
                <cdecl>
                    <attributelist>
                         <attribute name="kind" value="variable"/>
                         <attribute name="name" value="x"/>
                         <attribute name="type" value="double"/>
                    </attributelist>
                </cdecl>
                <cdecl>
                    <attributelist>
                         <attribute name="kind" value="variable"/>
                         <attribute name="name" value="y"/>
                         <attribute name="type" value="double"/>
                    </attributelist>
                </cdecl>
            </class>
        </module>
    </top>
    """
    parser = SwigXmlParser()
    top = parser.parse_string(xml)
    cls = top.module.classes[0]
    assert len(cls.cdecls) == 2
    assert cls.cdecls[0].name == "x"
    assert cls.cdecls[0].kind == "variable"
    assert cls.cdecls[1].name == "y"
    assert cls.cdecls[1].kind == "variable"
