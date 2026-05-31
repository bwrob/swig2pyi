# pyright: reportPrivateUsage=false
# pyright: reportAttributeAccessIssue=false

import pytest

from swig2pyi.core.config import Config
from swig2pyi.core.emitter import StubEmitter
from swig2pyi.core.parser import (
    CDecl,
    Class,
    Constructor,
    Destructor,
    Enum,
    EnumItem,
    Module,
    Parm,
    Top,
)
from swig2pyi.core.type_system import TypeManager


@pytest.fixture
def base_config() -> Config:
    return Config(
        module_name="my_swig_module",
        includes=[],
        type_map={
            "int": "int",
            "double": "float",
            "void": "None",
            "std::string": "str",
            "string": "str",
            "bool": "bool",
        },
        smart_pointers=["std::shared_ptr", "boost::shared_ptr"],
        containers={"std::vector": "list"},
        rename_operators=True,
    )


@pytest.fixture
def type_manager(base_config: Config) -> TypeManager:
    return TypeManager(base_config)


# --- 33.3.1 Modules ---
def test_sec_33_3_1_modules(type_manager: TypeManager) -> None:
    # A SWIG module generates the overall stub file structure and typing imports
    module = Module(name="my_swig_module", cdecls=[], classes=[], enums=[])
    top = Top(module=module)
    emitter = StubEmitter(type_manager)
    emitter.emit(top)
    output = emitter.get_output()
    assert "import" in output or "from typing import" in output


# --- 33.3.2 Functions ---
def test_sec_33_3_2_functions(type_manager: TypeManager) -> None:
    # Basic global function mapping: return types, parameters
    func = CDecl(
        name="calculate_sine",
        kind="function",
        type="double",
        parms=[Parm(name="angle", type="double")],
    )
    module = Module(name="my_swig_module", cdecls=[func])
    top = Top(module=module)
    emitter = StubEmitter(type_manager)
    emitter.emit(top)
    output = emitter.get_output()
    assert "def calculate_sine(" in output
    assert "angle: float" in output
    assert "-> float: ..." in output


# --- 33.3.3 Global variables ---
def test_sec_33_3_3_global_variables(type_manager: TypeManager) -> None:
    # Global variables: const maps to Final[T], normal variables mapped directly
    normal_var = CDecl(name="pi_value", kind="variable", type="double")
    const_var = CDecl(name="max_connections", kind="variable", type="const int")
    module = Module(name="my_swig_module", cdecls=[normal_var, const_var])
    top = Top(module=module)
    emitter = StubEmitter(type_manager)
    emitter.emit(top)
    output = emitter.get_output()
    assert "pi_value: float" in output
    assert "max_connections: Final[int]" in output
    assert "Final" in output


# --- 33.3.4 Constants and enums ---
def test_sec_33_3_4_constants_and_enums(type_manager: TypeManager) -> None:
    # Module level constants and enums (classic enums mapping)
    item_a = EnumItem(name="STATUS_OK", value="0")
    item_b = EnumItem(name="STATUS_ERROR", value="1")
    enum_decl = Enum(name="StatusCode", items=[item_a, item_b])

    # Enum types inside function signatures should map correctly
    func = CDecl(
        name="set_status",
        kind="function",
        type="void",
        parms=[Parm(name="code", type="StatusCode")],
    )

    module = Module(name="my_swig_module", enums=[enum_decl], cdecls=[func])
    top = Top(module=module)

    # We populate the TypeManager's enums set so it knows StatusCode is an enum type
    type_manager.enums.add("StatusCode")

    emitter = StubEmitter(type_manager)
    emitter.emit(top)
    output = emitter.get_output()
    assert "class StatusCode(IntEnum):" in output
    assert "STATUS_OK = 0" in output
    assert "code: Union[StatusCode, int]" in output


# --- 33.3.5 Pointers ---
def test_sec_33_3_5_pointers(type_manager: TypeManager) -> None:
    # Pointer parameters/returns (e.g. Point*) should map to the underlying class name
    func = CDecl(
        name="process_point",
        kind="function",
        type="Point *",
        parms=[Parm(name="p", type="Point *")],
    )
    module = Module(name="my_swig_module", cdecls=[func])
    top = Top(module=module)
    emitter = StubEmitter(type_manager)
    emitter.emit(top)
    output = emitter.get_output()
    assert "def process_point(" in output
    assert "p: Point" in output
    assert "-> Point: ..." in output


# --- 33.3.6 Structures ---
def test_sec_33_3_6_structures(type_manager: TypeManager) -> None:
    # C-style struct mapping to Python class with fields as type annotations
    var_x = CDecl(name="x", kind="variable", type="double")
    var_y = CDecl(name="y", kind="variable", type="double")
    # Struct is represented as a Class with kind="struct"
    structure = Class(name="Vector", kind="struct", cdecls=[var_x, var_y])
    module = Module(name="my_swig_module", classes=[structure])
    top = Top(module=module)
    emitter = StubEmitter(type_manager)
    emitter.emit(top)
    output = emitter.get_output()
    assert "class Vector:" in output
    assert "x: float" in output
    assert "y: float" in output


# --- 33.3.7 C++ classes ---
def test_sec_33_3_7_cpp_classes(type_manager: TypeManager) -> None:
    # C++ classes with methods, constructors, destructors, and static methods
    method = CDecl(name="get_area", kind="function", type="double")
    static_method = CDecl(
        name="create_default", kind="function", type="Shape", is_static=True
    )
    ctor = Constructor(name="Shape", parms=[Parm(name="sides", type="int")])
    dtor = Destructor(name="Shape")

    cls = Class(
        name="Shape",
        kind="class",
        constructors=[ctor],
        destructors=[dtor],
        cdecls=[method, static_method],
    )
    module = Module(name="my_swig_module", classes=[cls])
    top = Top(module=module)
    emitter = StubEmitter(type_manager)
    emitter.emit(top)
    output = emitter.get_output()

    assert "class Shape:" in output
    assert "def __init__(" in output
    assert "sides: int" in output
    assert "@staticmethod" in output
    assert "def create_default() -> Shape: ..." in output
    assert "def get_area(self) -> float: ..." in output


# --- 33.3.8 C++ inheritance ---
def test_sec_33_3_8_cpp_inheritance(type_manager: TypeManager) -> None:
    # Single and multiple inheritance mappings
    parent_a = Class(name="ParentA", kind="class")
    parent_b = Class(name="ParentB", kind="class")
    child = Class(name="Child", kind="class", bases=["ParentA", "ParentB"])
    module = Module(name="my_swig_module", classes=[parent_a, parent_b, child])
    top = Top(module=module)
    emitter = StubEmitter(type_manager)
    emitter.emit(top)
    output = emitter.get_output()
    assert "class Child(ParentA, ParentB):" in output


# --- 33.3.9 Pointers, references, values, and arrays ---
def test_sec_33_3_9_pointers_references_values_arrays(
    type_manager: TypeManager,
) -> None:
    # Function arguments passed by value, pointer, reference, or array
    func = CDecl(
        name="array_func",
        kind="function",
        type="void",
        parms=[
            Parm(name="val", type="int"),
            Parm(name="ptr", type="int *"),
            Parm(name="ref", type="const int &"),
            Parm(name="arr", type="int[]"),
        ],
    )
    module = Module(name="my_swig_module", cdecls=[func])
    top = Top(module=module)
    emitter = StubEmitter(type_manager)
    emitter.emit(top)
    output = emitter.get_output()
    assert "val: int" in output
    assert "ptr: int" in output
    assert "ref: int" in output
    # int[] usually normalizes to int
    assert "arr: int" in output


# --- 33.3.10 C++ overloaded functions ---
def test_sec_33_3_10_cpp_overloaded_functions(type_manager: TypeManager) -> None:
    # Multiple signatures for the same function name should use @overload
    func_1 = CDecl(
        name="compute",
        kind="function",
        type="int",
        parms=[Parm(name="x", type="int")],
        decl="f(int).",
    )
    func_2 = CDecl(
        name="compute",
        kind="function",
        type="double",
        parms=[Parm(name="x", type="double")],
        decl="f(double).",
    )
    module = Module(name="my_swig_module", cdecls=[func_1, func_2])
    top = Top(module=module)
    emitter = StubEmitter(type_manager)
    emitter.emit(top)
    output = emitter.get_output()

    assert "@overload" in output
    assert "def compute(" in output
    assert "x: int" in output
    assert "x: float" in output


# --- 33.3.11 C++ operators ---
def test_sec_33_3_11_cpp_operators(type_manager: TypeManager) -> None:
    # C++ operators mapping to Python dunders
    op_add = CDecl(
        name="operator+",
        kind="function",
        type="Matrix",
        parms=[Parm(name="other", type="Matrix")],
    )
    op_getitem = CDecl(
        name="operator[]",
        kind="function",
        type="double",
        parms=[Parm(name="index", type="size_t")],
    )
    op_eq = CDecl(
        name="operator==",
        kind="function",
        type="bool",
        parms=[Parm(name="other", type="Matrix")],
    )
    cls = Class(name="Matrix", kind="class", cdecls=[op_add, op_getitem, op_eq])
    module = Module(name="my_swig_module", classes=[cls])
    top = Top(module=module)
    emitter = StubEmitter(type_manager)
    emitter.emit(top)
    output = emitter.get_output()

    assert "def __add__(" in output
    assert "other: Matrix" in output
    assert "def __eq__(" in output
    assert "other: object" in output  # __eq__ is customized to accept object
    assert "def __iter__(" in output  # Generated automatically from __getitem__


# --- 33.3.12 C++ namespaces ---
def test_sec_33_3_12_cpp_namespaces(type_manager: TypeManager) -> None:
    # Scoped types (with namespace) get resolved and stripped based on config
    func = CDecl(
        name="scoped_func",
        kind="function",
        type="std::string",
        parms=[Parm(name="param", type="QuantLib::Real")],
    )
    # Let's map QuantLib::Real to float in custom config type_map
    type_manager.config.type_map["QuantLib::Real"] = "float"
    # Reinitialize mappings
    type_manager._type_map = {
        type_manager.clean_cpp_type(k): v
        for k, v in type_manager.config.type_map.items()
    }

    module = Module(name="my_swig_module", cdecls=[func])
    top = Top(module=module)
    emitter = StubEmitter(type_manager)
    emitter.emit(top)
    output = emitter.get_output()
    assert "param: float" in output
    assert "-> str: ..." in output


# --- 33.3.13 C++ templates ---
def test_sec_33_3_13_cpp_templates(type_manager: TypeManager) -> None:
    # Templated types (e.g. std::vector<double>) mapped to containers or template mappings
    func = CDecl(
        name="process_values",
        kind="function",
        type="std::vector<double>",
        parms=[Parm(name="vals", type="std::vector<int>")],
    )
    module = Module(name="my_swig_module", cdecls=[func])
    top = Top(module=module)
    emitter = StubEmitter(type_manager)
    emitter.emit(top)
    output = emitter.get_output()
    # std::vector<int> as param relaxed to Sequence[int]
    assert "vals: Sequence[int]" in output
    assert "-> list[float]" in output


# --- 33.3.14 C++ Smart Pointers ---
def test_sec_33_3_14_cpp_smart_pointers(type_manager: TypeManager) -> None:
    # Smart pointers (e.g. std::shared_ptr<MyClass>) should resolve to the underlying type MyClass
    func = CDecl(
        name="factory",
        kind="function",
        type="std::shared_ptr<Widget>",
        parms=[Parm(name="w", type="boost::shared_ptr<Widget>")],
    )
    module = Module(name="my_swig_module", cdecls=[func])
    top = Top(module=module)
    emitter = StubEmitter(type_manager)
    emitter.emit(top)
    output = emitter.get_output()
    assert "def factory(" in output
    assert "w: Widget" in output
    assert "-> Widget: ..." in output


# --- 33.3.15 C++ reference counted objects ---
def test_sec_33_3_15_cpp_reference_counted(type_manager: TypeManager) -> None:
    # Verify how reference counted styles (or custom pointers/handles) map and emit.
    # In SWIG, handle classes may delegate methods. Let's test delegation mapping.
    # In configuration, we define handle classes using smart_pointers or general template handling.
    # Let's test that classes with handles can be defined.
    handle_cls = Class(
        name="WidgetHandle",
        kind="class",
        bases=[],
        cdecls=[CDecl(name="do_something", kind="function", type="void")],
    )
    module = Module(name="my_swig_module", classes=[handle_cls])
    top = Top(module=module)
    emitter = StubEmitter(type_manager)
    emitter.emit(top)
    output = emitter.get_output()
    assert "class WidgetHandle:" in output
    assert "def do_something(" in output
