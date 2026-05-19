import pytest

from swig2pyi.core.config import Config
from swig2pyi.core.emitter import StubEmitter
from swig2pyi.core.parser import CDecl, Class, Constructor, Module, Parm, Top
from swig2pyi.core.type_system import TypeManager


@pytest.fixture
def type_manager():
    # Minimal config
    config = Config(
        module_name="Test",
        includes=[],
        type_map={"int": "int", "void": "None", "std::string": "str"},
        smart_pointers=[],
        containers={},
        rename_operators=True,
    )
    return TypeManager(config)


def test_emit_class_with_method(type_manager) -> None:
    # Construct a mock Top
    cdecl = CDecl(
        name="myFunc", kind="function", type="int", parms=[Parm(name="a", type="int")]
    )
    ctor = Constructor(name="MyClass", parms=[])
    cls = Class(name="MyClass", kind="class", cdecls=[cdecl], constructors=[ctor])
    module = Module(name="Test", classes=[cls], cdecls=[])
    top = Top(module=module)

    emitter = StubEmitter(type_manager)
    emitter.emit(top)
    output = emitter.get_output()

    assert "class MyClass:" in output
    assert "def __init__(self) -> None: ..." in output
    assert (
        """
    def myFunc(
        self,
        a: int,
    ) -> int: ...
"""
        in output
    )


def test_operator_rename(type_manager) -> None:
    # operator+ -> __add__
    cdecl = CDecl(
        name="operator+",
        kind="function",
        type="int",
        parms=[Parm(name="other", type="int")],
    )
    cls = Class(name="MyClass", kind="class", cdecls=[cdecl], constructors=[])
    module = Module(name="Test", classes=[cls], cdecls=[])
    top = Top(module=module)

    emitter = StubEmitter(type_manager)
    emitter.emit(top)
    output = emitter.get_output()

    assert (
        """
    def __add__(
        self,
        other: int,
    ) -> int: ...
"""
        in output
    )


def test_emit_class_with_variables(type_manager) -> None:
    # Construct a mock Top with variables
    var_x = CDecl(name="x", kind="variable", type="int")
    var_y = CDecl(name="y", kind="variable", type="int")
    cls = Class(name="Point", kind="class", cdecls=[var_x, var_y], constructors=[])
    module = Module(name="Test", classes=[cls], cdecls=[])
    top = Top(module=module)

    emitter = StubEmitter(type_manager)
    emitter.emit(top)
    output = emitter.get_output()

    assert "class Point:" in output
    assert "x: int" in output
    assert "y: int" in output
