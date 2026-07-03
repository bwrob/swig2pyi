from pathlib import Path

import pytest

from swig2pyi.core.ast_models import CDecl, Class, Constructor, Enum, Module, Parm, Top
from swig2pyi.core.config import Config
from swig2pyi.core.filter import filter_ast


def test_transitive_filtering() -> None:
    config = Config(
        module_name="TestModule",
        includes=[],
        type_map={},
        smart_pointers=[],
        containers={},
    )

    # Construct AST
    class_b = Class(name="B")
    class_d = Class(name="D")

    # Class C has a method returning D
    class_c = Class(name="C", cdecls=[CDecl(name="get_d", type="D", kind="function")])

    # Class A inherits from B and has a constructor taking C
    class_a = Class(
        name="A",
        bases=["B"],
        constructors=[Constructor(name="A", parms=[Parm(name="c", type="C")])],
    )

    # Class E is completely independent
    class_e = Class(name="E")

    # EnumX
    enum_x = Enum(name="EnumX")

    # Global cdecls
    global_func = CDecl(name="global_func", type="A", kind="function")
    global_var = CDecl(name="global_var", type="EnumX", kind="variable")

    module = Module(
        name="TestModule",
        classes=[class_a, class_b, class_c, class_d, class_e],
        enums=[enum_x],
        cdecls=[global_func, global_var],
    )
    top = Top(module=module)

    # Test 1: Seed with "A"
    filtered = filter_ast(top, ["A"], config)
    assert filtered.module is not None
    kept_classes = {c.name for c in filtered.module.classes}
    assert kept_classes == {"A", "B", "C", "D"}
    assert not filtered.module.enums
    assert not filtered.module.cdecls

    # Test 2: Seed with "global_func"
    filtered2 = filter_ast(top, ["global_func"], config)
    assert filtered2.module is not None
    assert {c.name for c in filtered2.module.classes} == {"A", "B", "C", "D"}
    assert {c.name for c in filtered2.module.cdecls} == {"global_func"}

    # Test 3: Seed with "global_var"
    filtered3 = filter_ast(top, ["global_var"], config)
    assert filtered3.module is not None
    assert not filtered3.module.classes
    assert {e.name for e in filtered3.module.enums} == {"EnumX"}
    assert {c.name for c in filtered3.module.cdecls} == {"global_var"}


def test_filter_edge_cases(monkeypatch: pytest.MonkeyPatch) -> None:
    from swig2pyi.core.filter import FilterState, extract_referenced_symbols
    from swig2pyi.core.type_system import TypeManager

    config = Config(
        module_name="TestModule",
        includes=[],
        type_map={},
        smart_pointers=[],
        containers={},
    )

    # 1. extract_referenced_symbols with None or empty type_str
    tm = TypeManager(config, top=Top(module=None))
    assert extract_referenced_symbols(None, tm) == set()
    assert extract_referenced_symbols("", tm) == set()

    # 2. extract_referenced_symbols handles exceptions in to_python
    def mock_to_python(self: TypeManager, t: str) -> str:
        msg = "mock error"
        raise ValueError(msg)

    monkeypatch.setattr(TypeManager, "to_python", mock_to_python)
    assert extract_referenced_symbols("MyType", tm) == {"MyType"}
    monkeypatch.undo()

    # 3. Class with cpp_type and seed by C++ name
    cls_a = Class(name="PyA", cpp_type="cpp::A")
    module = Module(name="TestModule", classes=[cls_a], enums=[], cdecls=[])
    top = Top(module=module)

    # Test seed by Python name
    filtered = filter_ast(top, ["PyA"], config)
    assert filtered.module is not None
    assert {c.name for c in filtered.module.classes} == {"PyA"}

    # Test seed by C++ name
    filtered_cpp = filter_ast(top, ["cpp::A"], config)
    assert filtered_cpp.module is not None
    assert {c.name for c in filtered_cpp.module.classes} == {"PyA"}

    # Test already visited logic for classes (seeding twice doesn't double-queue)
    state = FilterState(top, config)
    state.collect_seeds(["PyA", "PyA"])
    assert len(state.queue) == 1

    # 4. Empty top.module
    empty_top = Top(module=None)
    assert filter_ast(empty_top, ["A"], config) is empty_top

    # Instantiate FilterState with empty top to cover early returns
    state_empty = FilterState(empty_top, config)
    assert not state_empty.class_by_py_name

    # Empty include_symbols
    assert filter_ast(top, [], config) is top

    # 5. Enum & CDecl visited checks, seed checks
    enum_x = Enum(name="EnumX")
    cdecl_y = CDecl(name="CDeclY", type="int")
    module2 = Module(name="TestModule", classes=[], enums=[enum_x], cdecls=[cdecl_y])
    top2 = Top(module=module2)
    state2 = FilterState(top2, config)
    state2.collect_seeds(["EnumX", "EnumX", "CDeclY", "CDeclY", "NonexistentSymbol"])
    assert len(state2.queue) == 2

    # 6. Nested classes traversal
    nested_cls = Class(name="Nested")
    parent_cls = Class(name="Parent", classes=[nested_cls])
    module3 = Module(name="TestModule", classes=[parent_cls, nested_cls])
    top3 = Top(module=module3)
    filtered3 = filter_ast(top3, ["Parent"], config)
    assert filtered3.module is not None
    assert {c.name for c in filtered3.module.classes} == {"Parent", "Nested"}

    # 7. Class member function parameter traversal
    cls_d = Class(name="D")
    cls_c = Class(
        name="C",
        cdecls=[
            CDecl(
                name="method_x",
                type="void",
                kind="function",
                parms=[Parm(name="p", type="D")],
            )
        ],
    )
    module4 = Module(name="TestModule", classes=[cls_c, cls_d])
    top4 = Top(module=module4)
    filtered4 = filter_ast(top4, ["C"], config)
    assert filtered4.module is not None
    assert {c.name for c in filtered4.module.classes} == {"C", "D"}

    # 8. Global CDecl function parameter traversal
    cls_f = Class(name="F")
    global_func = CDecl(
        name="func_x",
        type="void",
        kind="function",
        parms=[Parm(name="p", type="F")],
    )
    module5 = Module(name="TestModule", classes=[cls_f], cdecls=[global_func])
    top5 = Top(module=module5)
    filtered5 = filter_ast(top5, ["func_x"], config)
    assert filtered5.module is not None
    assert {c.name for c in filtered5.module.classes} == {"F"}
    assert {c.name for c in filtered5.module.cdecls} == {"func_x"}


def test_api_generate_from_xml_with_filter(tmp_path: Path) -> None:

    from swig2pyi.api import generate_from_xml

    xml_content = """<?xml version="1.0" ?>
    <top>
      <module>
        <attributelist>
          <attribute name="name" value="math"/>
        </attributelist>
        <cdecl>
          <attributelist>
            <attribute name="name" value="sin"/>
            <attribute name="sym_name" value="sin"/>
            <attribute name="kind" value="function"/>
            <attribute name="type" value="double"/>
          </attributelist>
        </cdecl>
        <cdecl>
          <attributelist>
            <attribute name="name" value="cos"/>
            <attribute name="sym_name" value="cos"/>
            <attribute name="kind" value="function"/>
            <attribute name="type" value="double"/>
          </attributelist>
        </cdecl>
      </module>
    </top>
    """
    xml_file = tmp_path / "math.xml"
    xml_file.write_text(xml_content, encoding="utf-8")
    output_file = tmp_path / "math.pyi"
    config = Config(
        module_name="math",
        includes=[],
        type_map={"double": "float"},
        smart_pointers=[],
        containers={},
        include_symbols=["sin"],
    )
    generate_from_xml(xml_file, config, output_file)
    assert output_file.exists()
    content = output_file.read_text(encoding="utf-8")
    assert "def sin" in content
    assert "def cos" not in content
