from swig2pyi.core.parser import SwigXmlParser


def test_parse_simple_xml() -> None:
    xml = """
    <top>
        <attributelist>
            <attribute name="module" value="QuantLib"/>
        </attributelist>
        <module>
            <class>
                <attributelist>
                    <attribute name="name" value="Date"/>
                </attributelist>
                <constructor>
                    <attributelist>
                         <attribute name="name" value="Date"/>
                    </attributelist>
                    <parm>
                        <attributelist>
                            <attribute name="name" value="d"/>
                            <attribute name="type" value="int"/>
                        </attributelist>
                    </parm>
                </constructor>
                <cdecl>
                    <attributelist>
                        <attribute name="kind" value="function"/>
                        <attribute name="name" value="dayOfMonth"/>
                        <attribute name="type" value="int"/>
                    </attributelist>
                </cdecl>
            </class>
            <cdecl>
                <attributelist>
                    <attribute name="kind" value="function"/>
                    <attribute name="name" value="testGlobal"/>
                    <attribute name="type" value="void"/>
                </attributelist>
            </cdecl>
        </module>
    </top>
    """
    parser = SwigXmlParser()
    top = parser.parse_string(xml)
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


def test_parse_typedef() -> None:
    xml = """
    <top>
        <module>
            <cdecl>
                <attributelist>
                    <attribute name="type" value="double"/>
                    <attribute name="name" value="Real"/>
                    <attribute name="sym_name" value="Real"/>
                    <attribute name="kind" value="typedef"/>
                </attributelist>
            </cdecl>
            <cdecl>
                <attributelist>
                    <attribute name="type" value="char"/>
                    <attribute name="decl" value="p."/>
                    <attribute name="name" value="retString"/>
                    <attribute name="sym_name" value="retString"/>
                    <attribute name="kind" value="typedef"/>
                </attributelist>
            </cdecl>
        </module>
    </top>
    """
    parser = SwigXmlParser()
    top = parser.parse_string(xml)
    assert top.module is not None
    assert top.module.typedefs["Real"] == "double"
    assert top.module.typedefs["retString"] == "char *"
