from swig2pyi.core.config import Config
from swig2pyi.core.emitter import StubEmitter
from swig2pyi.core.parser import SwigXmlParser
from swig2pyi.core.type_system import TypeManager


def test_parse_and_emit_enum() -> None:
    xml = """
    <top>
        <attributelist><attribute name="module" value="Test"/></attributelist>
        <module>
            <enum>
                <attributelist><attribute name="name" value="Color"/></attributelist>
                <enumitem>
                    <attributelist>
                        <attribute name="name" value="Red"/>
                        <attribute name="enumvalue" value="0"/>
                    </attributelist>
                </enumitem>
                <enumitem>
                    <attributelist>
                        <attribute name="name" value="Green"/>
                        <attribute name="enumvalue" value="1"/>
                    </attributelist>
                </enumitem>
                <enumitem>
                    <attributelist>
                        <attribute name="name" value="Blue"/>
                    </attributelist>
                </enumitem>
            </enum>
            <class>
                <attributelist><attribute name="name" value="Shape"/></attributelist>
                <enum>
                    <attributelist><attribute name="name" value="Shape::Style"/></attributelist>
                    <enumitem>
                        <attributelist>
                            <attribute name="name" value="Solid"/>
                            <attribute name="enumvalue" value="10"/>
                        </attributelist>
                    </enumitem>
                    <enumitem>
                        <attributelist>
                            <attribute name="name" value="Dashed"/>
                            <attribute name="enumvalue" value="20"/>
                        </attributelist>
                    </enumitem>
                </enum>
            </class>
        </module>
    </top>
    """
    parser = SwigXmlParser()
    top = parser.parse_string(xml)

    assert len(top.module.enums) == 1
    color = top.module.enums[0]
    assert color.name == "Color"
    assert len(color.items) == 3
    assert color.items[0].name == "Red"
    assert color.items[0].value == "0"
    assert color.items[2].name == "Blue"
    assert color.items[2].value is None

    assert len(top.module.classes) == 1
    shape = top.module.classes[0]
    assert len(shape.enums) == 1
    style = shape.enums[0]
    assert style.name == "Shape::Style"

    # Test Emission
    config = Config(
        module_name="Test", includes=[], type_map={}, smart_pointers=[], containers={}
    )
    tm = TypeManager(config)
    emitter = StubEmitter(tm)
    emitter.emit(top)
    output = emitter.get_output()

    assert "class Color(int):" in output
    assert "Red: int = 0" in output
    assert "Blue: int" in output

    assert "class Shape:" in output
    assert "class Style(int):" in output
    assert "Solid: int = 10" in output
