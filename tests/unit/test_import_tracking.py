import pytest

from swig2pyi.core.config import Config
from swig2pyi.core.emitter import StubEmitter
from swig2pyi.core.parser import (
    CDecl,
    Class,
    Enum,
    EnumItem,
    Module,
    Parm,
    Top,
)
from swig2pyi.core.type_system import TypeManager


@pytest.fixture
def type_manager() -> TypeManager:
    config = Config(
        module_name="Test",
        includes=[],
        type_map={
            "int": "int",
            "void": "None",
            "std::string": "str",
            "std::vector<int>": "list[int]",
        },
        smart_pointers=[],
        containers={"std::vector": "list"},
        rename_operators=True,
    )
    return TypeManager(config)


def test_import_tracking_basic_and_overload(type_manager: TypeManager) -> None:
    # Set up two overloaded functions to trigger @overload
    cdecl1 = CDecl(
        name="myFunc", kind="function", type="int", parms=[Parm(name="a", type="int")]
    )
    cdecl2 = CDecl(
        name="myFunc",
        kind="function",
        type="int",
        parms=[Parm(name="a", type="int"), Parm(name="b", type="std::string")],
    )
    cls = Class(name="MyClass", kind="class", cdecls=[cdecl1, cdecl2], constructors=[])
    module = Module(name="Test", classes=[cls], cdecls=[])
    top = Top(module=module)

    emitter = StubEmitter(type_manager)
    emitter.emit(top)
    output = emitter.get_output()

    # We expect overload
    assert "overload" in type_manager.needed_imports
    assert "from typing import overload" in output
    assert "@overload" in output


def test_import_tracking_generic_and_enum(type_manager: TypeManager) -> None:
    # A generic class and an enum
    cls = Class(
        name="MyGeneric", kind="class", cdecls=[], constructors=[], is_template=True
    )
    enum = Enum(
        name="MyEnum",
        items=[EnumItem(name="Val1", value="1"), EnumItem(name="Val2", value="2")],
    )
    module = Module(name="Test", classes=[cls], enums=[enum], cdecls=[])
    top = Top(module=module)

    emitter = StubEmitter(type_manager)
    emitter.emit(top)
    output = emitter.get_output()

    assert "Generic" in type_manager.needed_imports
    assert "TypeVar" in type_manager.needed_imports
    assert "IntEnum" in type_manager.needed_imports
    assert "from typing import Generic, TypeVar" in output
    assert "from enum import IntEnum" in output
    assert "class MyEnum(IntEnum):" in output


def test_import_tracking_container_iterators(type_manager: TypeManager) -> None:
    # Create a class with a __getitem__ to trigger Iterator, and is a container to trigger Iterable
    getitem = CDecl(
        name="operator[]",
        kind="function",
        type="int",
        parms=[Parm(name="i", type="int")],
    )
    # The class represents a container std::vector<int>
    cls = Class(
        name="MyVector",
        kind="class",
        cpp_type="std::vector<int>",
        cdecls=[getitem],
        constructors=[],
    )
    module = Module(name="Test", classes=[cls], cdecls=[])
    top = Top(module=module)

    emitter = StubEmitter(type_manager)
    emitter.emit(top)
    output = emitter.get_output()

    assert "Iterable" in type_manager.needed_imports
    assert "Iterator" in type_manager.needed_imports
    assert "overload" in type_manager.needed_imports
    assert "from typing import overload, Iterable, Iterator" in output
    assert "def __iter__(self) -> Iterator[int]: ..." in output
    assert "iterable: Iterable[int]" in output
