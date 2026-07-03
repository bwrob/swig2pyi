from swig2pyi.core.config import Config
from swig2pyi.core.emitter import StubEmitter
from swig2pyi.core.parser import SwigXmlParser
from swig2pyi.core.type_system import TypeManager


def test_emit_docstrings() -> None:
    xml = """
    <top>
        <attributelist><attribute name="module" value="Test"/></attributelist>
        <module>
            <class>
                <attributelist>
                    <attribute name="name" value="Documented"/>
                    <attribute name="feature_docstring" value="This is a class docstring"/>
                </attributelist>
                <cdecl>
                    <attributelist>
                         <attribute name="kind" value="function"/>
                         <attribute name="name" value="greet"/>
                         <attribute name="type" value="void"/>
                         <attribute name="feature_docstring" value="Say hello to someone"/>
                    </attributelist>
                </cdecl>
                <cdecl>
                    <attributelist>
                         <attribute name="kind" value="variable"/>
                         <attribute name="name" value="answer"/>
                         <attribute name="type" value="int"/>
                         <attribute name="feature_docstring" value="The ultimate answer"/>
                    </attributelist>
                </cdecl>
            </class>
            <enum>
                <attributelist>
                    <attribute name="name" value="Status"/>
                    <attribute name="feature_docstring" value="Enum documentation"/>
                </attributelist>
                <enumitem>
                    <attributelist>
                        <attribute name="name" value="OK"/>
                        <attribute name="enumvalue" value="0"/>
                    </attributelist>
                </enumitem>
            </enum>
        </module>
    </top>
    """
    parser = SwigXmlParser()
    top = parser.parse_string(xml)

    config = Config(
        module_name="Test",
        includes=[],
        type_map={"int": "int", "void": "None"},
        smart_pointers=[],
        containers={},
    )
    tm = TypeManager(config)
    emitter = StubEmitter(tm)
    emitter.emit(top)
    output = emitter.get_output()

    assert "class Documented:" in output
    assert '    """This is a class docstring"""' in output
    assert "    def greet(self) -> None: ..." in output
    assert '    """Say hello to someone"""' in output
    assert "    answer: int" in output
    assert '    """The ultimate answer"""' in output
    assert "class Status(IntEnum):" in output
    assert '    """Enum documentation"""' in output


def test_multiline_docstring() -> None:
    xml = """
    <top>
        <attributelist><attribute name="module" value="Test"/></attributelist>
        <module>
            <cdecl>
                <attributelist>
                     <attribute name="kind" value="function"/>
                     <attribute name="name" value="multiline"/>
                     <attribute name="type" value="void"/>
                     <attribute name="feature_docstring" value="Line 1\\nLine 2"/>
                </attributelist>
            </cdecl>
        </module>
    </top>
    """
    parser = SwigXmlParser()
    top = parser.parse_string(xml)

    config = Config(
        module_name="Test",
        includes=[],
        type_map={"void": "None"},
        smart_pointers=[],
        containers={},
    )
    tm = TypeManager(config)
    emitter = StubEmitter(tm)
    emitter.emit(top)
    output = emitter.get_output()

    assert '"""Line 1' in output
    assert 'Line 2"""' in output
