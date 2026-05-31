import pytest

from swig2pyi.core.config import Config
from swig2pyi.core.emitter import StubEmitter
from swig2pyi.core.parser import CDecl, Class, Constructor, Module, Parm, Top
from swig2pyi.core.type_system import TypeManager


@pytest.fixture
def type_manager() -> TypeManager:
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


def test_emit_class_with_method(type_manager: TypeManager) -> None:
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


def test_operator_rename(type_manager: TypeManager) -> None:
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


def test_emit_class_with_variables(type_manager: TypeManager) -> None:
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


def test_emit_const_variables(type_manager: TypeManager) -> None:
    # Set up vectors in the type manager's configuration for realistic resolution
    custom_config = type_manager.config.model_copy(deep=True)
    custom_config.containers["std::vector"] = "list"
    custom_tm = TypeManager(custom_config)

    # 1. Module-level const variable
    module_var = CDecl(name="MY_CONST", kind="variable", type="const int")

    # 2. Class-level const variable
    class_var = CDecl(name="MAX_VAL", kind="variable", type="int const")

    # 3. Class-level non-const variable with const inside template parameter
    class_var_tmpl = CDecl(
        name="vec_const_ptr", kind="variable", type="std::vector<const int>"
    )

    # 4. Class-level const variable with template parameter
    class_var_const_tmpl = CDecl(
        name="const_vec", kind="variable", type="const std::vector<int>"
    )

    cls = Class(
        name="MyClass",
        kind="class",
        cdecls=[class_var, class_var_tmpl, class_var_const_tmpl],
        constructors=[],
    )
    module = Module(name="Test", classes=[cls], cdecls=[module_var])
    top = Top(module=module)

    emitter = StubEmitter(custom_tm)
    emitter.emit(top)
    output = emitter.get_output()

    # Check that Final is imported
    typing_import = next(
        line for line in output.splitlines() if line.startswith("from typing import")
    )
    assert "Final" in typing_import

    # Check module-level const
    assert "MY_CONST: Final[int]" in output

    # Check class-level const
    assert "MAX_VAL: Final[int]" in output

    # Check class-level non-const with const inside template parameter (should NOT be Final)
    assert "vec_const_ptr: list[int]" in output

    # Check class-level const variable with template parameter (should be Final)
    assert "const_vec: Final[list[int]]" in output
