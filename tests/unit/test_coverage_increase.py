# pyright: reportPrivateUsage=false
# pyright: reportAttributeAccessIssue=false
# pyright: reportUnknownVariableType=false
# pyright: reportUnknownArgumentType=false
# pyright: reportUnknownParameterType=false
# pyright: reportMissingParameterType=false
# pyright: reportUnknownMemberType=false
# pyright: reportUnknownLambdaType=false
import argparse
import os
import shutil
import sys
from pathlib import Path
from typing import Any

import pytest

from swig2pyi.api import generate_from_interface, generate_from_xml
from swig2pyi.cli import _load_config, _run_generation, main
from swig2pyi.core.config import Config
from swig2pyi.core.emitter import StubEmitter
from swig2pyi.core.parser import Class, Module, Top
from swig2pyi.core.qa import CoverageReport, StubCoverageChecker
from swig2pyi.core.runner import SwigRunner
from swig2pyi.core.type_system import TypeManager, _collect_enums


def test_collect_enums_edge_cases() -> None:
    # 1. No module in top
    assert _collect_enums(Top(module=None)) == set()

    # 2. Module with sub-classes and enums
    from swig2pyi.core.parser import Enum

    sub_sub_cls = Class(name="SubSub", enums=[Enum(name="NestedEnum", items=[])])
    sub_cls = Class(name="Sub", classes=[sub_sub_cls])
    cls = Class(
        name="Parent", classes=[sub_cls], enums=[Enum(name="ClassEnum", items=[])]
    )
    module = Module(name="Test", classes=[cls], enums=[Enum(name="ModEnum", items=[])])
    res = _collect_enums(Top(module=module))
    assert "ModEnum" in res
    assert "ClassEnum" in res
    assert "NestedEnum" in res


def test_api_generate_from_xml(tmp_path: Path) -> None:
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
          <parmlist>
            <parm>
              <attributelist>
                <attribute name="name" value="x"/>
                <attribute name="type" value="double"/>
              </attributelist>
            </parm>
          </parmlist>
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
        rename_operators=True,
    )
    generate_from_xml(xml_file, config, output_file)
    assert output_file.exists()
    content = output_file.read_text(encoding="utf-8")
    assert "def sin(" in content


def test_api_generate_from_interface(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    interface_file = tmp_path / "math.i"
    interface_file.write_text("int add(int a, int b);\n", encoding="utf-8")
    output_file = tmp_path / "math.pyi"
    config = Config(
        module_name="math",
        includes=[],
        type_map={"int": "int"},
        smart_pointers=[],
        containers={},
        rename_operators=True,
    )

    # Mock SwigRunner.run
    def mock_run(
        self: SwigRunner,
        includes: list[str],
        interface_file: Path,
        output_xml: Path,
        module_name: str = "swig2pyi_wrapper",
    ) -> Path:
        _ = self, includes, interface_file, module_name
        xml_content = """<?xml version="1.0" ?>
        <top>
          <module>
            <attributelist>
              <attribute name="name" value="math"/>
            </attributelist>
            <cdecl>
              <attributelist>
                <attribute name="name" value="add"/>
                <attribute name="sym_name" value="add"/>
                <attribute name="kind" value="function"/>
                <attribute name="type" value="int"/>
              </attributelist>
            </cdecl>
          </module>
        </top>
        """
        output_xml.write_text(xml_content, encoding="utf-8")
        return output_xml

    monkeypatch.setattr(SwigRunner, "run", mock_run)
    generate_from_interface(interface_file, config, output_file)
    assert output_file.exists()
    content = output_file.read_text(encoding="utf-8")
    assert "def add(" in content


def test_cli_load_config_nonexistent(tmp_path: Path) -> None:
    with pytest.raises(SystemExit) as exc_info:
        _load_config(tmp_path / "nonexistent.json")
    assert exc_info.value.code == 1


def test_cli_load_config_invalid(tmp_path: Path) -> None:
    invalid_file = tmp_path / "invalid.json"
    invalid_file.write_text("{invalid json", encoding="utf-8")
    with pytest.raises(SystemExit) as exc_info:
        _load_config(invalid_file)
    assert exc_info.value.code == 1


def test_cli_run_generation_edge_cases(tmp_path: Path) -> None:
    config = Config(
        module_name="Test",
        includes=[],
        type_map={},
        smart_pointers=[],
        containers={},
    )

    # Nonexistent interface
    args = argparse.Namespace(
        interface=tmp_path / "nonexistent.i",
        xml=None,
        config=None,
        output=None,
        swig_path=None,
        validate=None,
    )
    with pytest.raises(SystemExit) as exc_info:
        _run_generation(args, config)
    assert exc_info.value.code == 1

    # Nonexistent XML
    args = argparse.Namespace(
        interface=None,
        xml=tmp_path / "nonexistent.xml",
        config=None,
        output=None,
        swig_path=None,
        validate=None,
    )
    with pytest.raises(SystemExit) as exc_info:
        _run_generation(args, config)
    assert exc_info.value.code == 1


def test_cli_main_exception_handling(
    monkeypatch: pytest.MonkeyPatch, tmp_path: Path
) -> None:
    # Cause _run_generation to raise ValueError
    def mock_run_generation(*args: Any, **kwargs: Any) -> None:
        _ = args, kwargs
        msg = "Unexpected error during generation"
        raise ValueError(msg)

    monkeypatch.setattr("swig2pyi.cli._run_generation", mock_run_generation)

    # Mock _load_config to return a dummy config
    def mock_load_config(_path: Path) -> Config:
        return Config(
            module_name="Test",
            includes=[],
            type_map={},
            smart_pointers=[],
            containers={},
        )

    monkeypatch.setattr("swig2pyi.cli._load_config", mock_load_config)

    monkeypatch.setattr(
        sys,
        "argv",
        [
            "swig2pyi",
            "-i",
            str(tmp_path / "dummy.i"),
            "--config",
            str(tmp_path / "config.json"),
            "-o",
            str(tmp_path / "output.pyi"),
        ],
    )

    with pytest.raises(SystemExit) as exc_info:
        main()
    assert exc_info.value.code == 1


def test_runner_unresolved_exe() -> None:
    runner = SwigRunner(swig_path="nonexistent_swig_executable_path")
    with pytest.raises(FileNotFoundError):
        runner.run(
            includes=[], interface_file=Path("dummy.i"), output_xml=Path("dummy.xml")
        )


def test_runner_execute_failures(tmp_path: Path) -> None:
    runner = SwigRunner()
    # 1. SWIG execution failed (OSError)
    with pytest.raises(RuntimeError) as exc_info:
        runner._execute(["/nonexistent/path/to/swig"], {}, tmp_path / "out.xml")
    assert "SWIG execution failed" in str(exc_info.value)

    # 2. SWIG failed (subprocess failure) - use python -c 'sys.exit(1)' for cross-platform
    with pytest.raises(RuntimeError) as exc_info:
        runner._execute(
            [sys.executable, "-c", "import sys; sys.exit(1)"],
            {},
            tmp_path / "out.xml",
        )
    assert "SWIG failed" in str(exc_info.value)

    # 3. SWIG succeeded but did not produce output file - python -c 'pass'
    with pytest.raises(RuntimeError) as exc_info:
        runner._execute(
            [sys.executable, "-c", "pass"],
            {},
            tmp_path / "out.xml",
        )
    assert "SWIG did not produce output file" in str(exc_info.value)


# Deleted test_qa_validator_missing_executables and test_qa_validator_failed_executions


def test_coverage_report_edge_cases() -> None:
    report = CoverageReport(runtime_symbol_count=0, stub_symbol_count=0)
    assert report.coverage_pct == 100.0


def test_stub_coverage_checker_allowlist(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    stub_file = tmp_path / "test.pyi"
    stub_file.write_text("import os\nx: int\npass\n", encoding="utf-8")

    # Live module mock
    import types

    mock_mod = types.ModuleType("mock_mod")
    mock_mod.x = 1
    mock_mod.y = 2

    checker = StubCoverageChecker(allowlist={"y"})

    # Mock _try_import
    def mock_import_module(name: str) -> types.ModuleType:
        _ = name
        return mock_mod

    monkeypatch.setattr("swig2pyi.core.qa.importlib.import_module", mock_import_module)

    report = checker.check(stub_file, "mock_mod")
    assert report is not None
    assert report.runtime_symbol_count == 2
    assert "y" in report.allowlisted
    assert "y" not in report.missing


def test_runner_caching(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    runner = SwigRunner()

    # Mock SwigRunner._execute to just write a dummy file
    def mock_execute(
        self: SwigRunner,
        cmd: list[str],
        env: dict[str, str],
        output_xml: Path,
    ) -> Path:
        _ = self, cmd, env
        output_xml.write_text("<dummy/>", encoding="utf-8")
        return output_xml

    monkeypatch.setattr(SwigRunner, "_execute", mock_execute)

    # First run (cache miss)
    interface_file = tmp_path / "test.i"
    interface_file.write_text("int f();", encoding="utf-8")
    out_xml = tmp_path / "out.xml"
    runner.run(
        includes=[str(tmp_path)], interface_file=interface_file, output_xml=out_xml
    )

    # Second run (cache hit)
    out_xml_2 = tmp_path / "out_2.xml"
    runner.run(
        includes=[str(tmp_path)], interface_file=interface_file, output_xml=out_xml_2
    )
    assert out_xml_2.exists()


# Deleted test_qa_validator_success


def test_cli_coverage_with_allowlist(
    monkeypatch: pytest.MonkeyPatch, tmp_path: Path
) -> None:
    stub_file = tmp_path / "math.pyi"
    stub_file.write_text("x: int\n", encoding="utf-8")
    allowlist_file = tmp_path / "allowlist.txt"
    allowlist_file.write_text("y\n", encoding="utf-8")

    monkeypatch.setattr(
        sys,
        "argv",
        [
            "swig2pyi",
            "coverage",
            "--stub",
            str(stub_file),
            "--module",
            "math",
            "--allowlist",
            str(allowlist_file),
        ],
    )

    # Mock Checker to verify allowlist is passed
    class MockChecker:
        def __init__(self, allowlist: set[str] | None = None) -> None:
            assert allowlist == {"y"}

        def check(self, _stub: Path, _module: str) -> CoverageReport:
            _ = _stub, _module
            return CoverageReport(runtime_symbol_count=1, stub_symbol_count=1)

    monkeypatch.setattr("swig2pyi.cli.StubCoverageChecker", MockChecker)

    with pytest.raises(SystemExit) as exc_info:
        main()
    assert exc_info.value.code == 0


def test_cli_main_success_xml(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    xml_content = """<?xml version="1.0" ?>
    <top>
      <module>
        <attributelist>
          <attribute name="name" value="math"/>
        </attributelist>
      </module>
    </top>
    """
    xml_file = tmp_path / "math.xml"
    xml_file.write_text(xml_content, encoding="utf-8")
    config_file = tmp_path / "config.json"
    config_file.write_text(
        '{"module_name": "math", "includes": [], "type_map": {}, "smart_pointers": [], "containers": {}}',
        encoding="utf-8",
    )
    output_file = tmp_path / "math.pyi"

    monkeypatch.setattr(
        sys,
        "argv",
        [
            "swig2pyi",
            "-x",
            str(xml_file),
            "--config",
            str(config_file),
            "-o",
            str(output_file),
        ],
    )

    main()
    assert output_file.exists()


# --- Additional Coverage Tests ---


def test_naming_manager_edge_cases() -> None:
    from swig2pyi.core.naming import NameManager

    nm = NameManager(rename_operators=True)
    # 1. Unsupported operator (mapped == name) -> returns None
    assert nm.get_python_name("operator!") is None

    # 2. Non-operator variable/function returning None when rename_operators is False
    nm_no_op = NameManager(rename_operators=False)
    assert nm_no_op.get_python_name("operator+") is None


def test_parser_xml_edge_cases() -> None:
    from swig2pyi.core.parser import SwigXmlParser

    parser = SwigXmlParser()

    # 1. insert tag under module containing section="python" and code attribute
    xml_code = """<?xml version="1.0" ?>
    <top>
      <module>
        <attributelist>
          <attribute name="name" value="math"/>
        </attributelist>
        <insert>
          <attributelist>
            <attribute name="section" value="python"/>
            <attribute name="code" value="import sys"/>
          </attributelist>
        </insert>
      </module>
    </top>
    """
    top = parser.parse_string(xml_code)
    assert top.module is not None
    assert len(top.module.python_code) == 1
    assert top.module.python_code[0] == "import sys"

    # 2. Nested classes inside class
    xml_nested = """<?xml version="1.0" ?>
    <top>
      <module>
        <class>
          <attributelist>
            <attribute name="name" value="Outer"/>
          </attributelist>
          <class>
            <attributelist>
              <attribute name="name" value="Inner"/>
            </attributelist>
          </class>
        </class>
      </module>
    </top>
    """
    top_nested = parser.parse_string(xml_nested)
    assert top_nested.module is not None
    assert top_nested.module.classes[0].classes[0].name == "Inner"

    # 3. Class with direct baselist child (rather than under attributelist)
    xml_base = """<?xml version="1.0" ?>
    <top>
      <module>
        <class>
          <attributelist>
            <attribute name="name" value="Derived"/>
          </attributelist>
          <baselist>
            <base name="Base"/>
          </baselist>
        </class>
      </module>
    </top>
    """
    top_base = parser.parse_string(xml_base)
    assert top_base.module is not None
    assert top_base.module.classes[0].bases == ["Base"]


def test_qa_coverage_report_properties() -> None:
    # CoverageReport uncovered_count and coverage_pct
    report = CoverageReport(
        runtime_symbol_count=10,
        stub_symbol_count=5,
        missing=["a", "b"],
        allowlisted=["c"],
    )
    assert report.uncovered_count == 2
    assert report.coverage_pct == 80.0


def test_qa_checker_import_failures(capsys: pytest.CaptureFixture[str]) -> None:
    checker = StubCoverageChecker()
    # 1. Non-existent module -> returns None
    assert checker.check(Path("dummy.pyi"), "non_existent_module_foo_bar") is None
    captured = capsys.readouterr()
    assert (
        "Warning: Could not import module non_existent_module_foo_bar" in captured.err
    )


def test_qa_checker_non_native_filtering(tmp_path: Path) -> None:
    stub_content = """
class A:
    pass
"""
    stub_file = tmp_path / "test_non_native.pyi"
    stub_file.write_text(stub_content, encoding="utf-8")

    import collections
    import types

    mock_mod = types.ModuleType("real_module")

    class A:
        pass

    A.__module__ = "real_module"
    mock_mod.A = A
    mock_mod.deque = collections.deque

    checker = StubCoverageChecker()
    checker._try_import = lambda name: mock_mod

    report = checker.check(stub_file, "real_module")
    assert report is not None
    # collections.deque should be filtered out because it is from "collections" and not "real_module"
    assert report.runtime_symbol_count == 1
    assert "deque" not in report.missing
    assert "deque" not in report.allowlisted


def test_qa_checker_ast_nodes(tmp_path: Path) -> None:
    # 2. Check parsing of ClassDef, FunctionDef, AsyncFunctionDef, Assign (node.targets) in checker
    stub_content = """
class A:
    pass

def f() -> None:
    pass

async def g() -> None:
    pass

x = 1
y = z = 2
"""
    stub_file = tmp_path / "test.pyi"
    stub_file.write_text(stub_content, encoding="utf-8")

    # live module mock
    import types

    mock_mod = types.ModuleType("mock_mod")
    mock_mod.A = type("A", (), {})
    mock_mod.f = lambda: None
    mock_mod.g = lambda: None
    mock_mod.x = 1
    mock_mod.y = 2
    mock_mod.z = 2

    checker = StubCoverageChecker()
    # Mock try_import
    checker._try_import = lambda name: mock_mod

    report = checker.check(stub_file, "mock_mod")
    assert report is not None
    assert report.missing == []
    assert report.coverage_pct == 100.0


# Deleted test_qa_validator_oserror and test_qa_validator_failed_typecheck


def test_runner_execute_success(tmp_path: Path) -> None:
    # Execute sh/bash command that creates output_xml to cover line 200
    runner = SwigRunner()
    output_xml = tmp_path / "out.xml"

    # We execute python script that writes to sys.argv[1]
    cmd = [
        sys.executable,
        "-c",
        "import sys; open(sys.argv[1], 'w').write('<xml/>')",
        str(output_xml),
    ]
    res_path = runner._execute(cmd, {}, output_xml)
    assert res_path == output_xml
    assert output_xml.exists()
    assert output_xml.read_text() == "<xml/>"


def test_runner_windows_suffix(monkeypatch: pytest.MonkeyPatch) -> None:
    # Resolving swig.exe with .exe on Windows
    import swig2pyi.core.runner

    runner = SwigRunner()
    monkeypatch.setattr(
        swig2pyi.core.runner,
        "swig",
        type("MockSwig", (), {"BIN_DIR": "/dummy", "SWIG_LIB_ENV": {}}),
    )
    monkeypatch.setattr(swig2pyi.core.runner, "_SWIG_MODULE_AVAILABLE", True)
    runner.use_module = True
    monkeypatch.setattr(
        swig2pyi.core.runner,
        "os",
        type("MockOS", (), {"name": "nt", "environ": os.environ}),
    )

    # Mock Path.exists to return False so suffix .exe is appended
    # Since we are on Linux/Unix, Path.exists is defined in pathlib._local.Path (or similar) or monkeypatched safely
    orig_exists = Path.exists

    def mock_exists(self, *args, **kwargs):
        if "swig" in str(self) or "dummy" in str(self):
            return False
        return orig_exists(self, *args, **kwargs)

    monkeypatch.setattr(Path, "exists", mock_exists)

    exe = runner._get_swig_exe()
    assert exe.suffix == ".exe"

    # Also test build_command with suffix on Windows
    cmd, _env = runner._build_command(
        [], Path("out.xml"), Path("dummy.cpp"), Path("outdir")
    )
    assert cmd[0].endswith(".exe")


# Deleted cache/dependency runner tests


def test_runner_build_command_shutil_which_fail(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    runner = SwigRunner(swig_path="nonexistent_swig_path")
    runner.use_module = False

    # Mock shutil.which to return None
    monkeypatch.setattr(shutil, "which", lambda x: None)

    with pytest.raises(FileNotFoundError):
        runner._build_command([], Path("out.xml"), Path("dummy.cpp"), Path("outdir"))


def test_signature_formatter_missing_types() -> None:
    from swig2pyi.core.parser import Parm

    type_manager = TypeManager(
        Config(
            module_name="Test",
            includes=[],
            type_map={},
            smart_pointers=[],
            containers={},
        )
    )
    emitter = StubEmitter(type_manager)
    # 1. Parameter without type (should default to Any)
    parms = [Parm(name="arg", type=None)]
    parts = emitter.format_params(parms)
    assert parts[0] == "arg: Any"
    assert "Any" in type_manager.needed_imports

    # 2. Return without type (should default to Any)
    assert emitter._get_return_type(None) == "Any"

    # 3. Return void resolved with mock void return to cover lines 75-76
    # (Since to_python already handles void -> None, we test the redundant safety check by mocking)
    with pytest.MonkeyPatch().context() as m:
        m.setattr(type_manager, "to_python", lambda *a, **kw: "void")
        assert emitter._get_return_type("some_void") == "None"


def test_type_manager_uncovered_paths() -> None:
    type_manager = TypeManager(
        Config(
            module_name="Test",
            includes=[],
            type_map={},
            smart_pointers=[],
            containers={},
        )
    )
    # 1. normalize_type with module prefix stripping
    type_manager.config.module_name = "QuantLib"
    assert type_manager.normalize_type("QuantLib::MyClass") == "MyClass"

    # 2. _to_python_parameter resolving through parameter_relaxation
    type_manager.config.parameter_relaxation = {"Real": "Sequence[float]"}
    assert (
        type_manager.to_python("QuantLib::Real", is_parameter=True) == "Sequence[float]"
    )

    # 3. collections.abc import recording
    type_manager.record_imports("collections.abc.Iterable")
    assert "collections.abc" in type_manager.needed_imports

    # 4. typing. import recording
    type_manager.record_imports("typing.Any")
    assert "typing" in type_manager.needed_imports

    # 5. _make_parameter_type with tuple, Union, Optional nested parameter translation
    assert (
        type_manager._make_parameter_type("tuple[list[int], float]")
        == "tuple[Sequence[int], float]"
    )
    assert (
        type_manager._make_parameter_type("Union[list[int], list[float]]")
        == "Union[Sequence[int], Sequence[float]]"
    )
    assert (
        type_manager._make_parameter_type("Optional[list[int]]")
        == "Optional[Sequence[int]]"
    )

    # 6. _resolve_typedefs with cleaned namespaced typemap lookup
    # Let's map "MyModule::Real" -> "float" and module_name is MyModule
    type_manager.config.module_name = "MyModule"
    type_manager.config.type_map = {"MyModule::Real": "float"}
    type_manager._type_map = {"MyModule::Real": "float"}
    assert type_manager._resolve_typedefs("Real") == "float"

    # 7. template_arg_counts custom count config check
    type_manager.config.template_arg_counts = {"custom_tmpl": 1}
    assert type_manager._get_template_arg_limit("custom_tmpl") == 1

    # 8. unmatched bracket returning -1
    assert type_manager._get_matching_bracket_index("std::vector<int", 11) == -1
    assert type_manager._find_matching_paren_index("std::vector(int") == -1

    # 9. _resolve_scopes stripping module name and returning scopes
    type_manager.config.module_name = "MyMod"
    # Scopes: MyMod::SubMod::Class -> SubMod::Class
    assert type_manager._resolve_scopes("MyMod::SubMod::Class") == "SubMod.Class"
    # Scopes: MyMod::Class -> Class
    assert type_manager._resolve_scopes("MyMod::Class") == "Class"


def test_cli_coverage_options(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    # 1. Allowlist does not exist exit
    stub_file = tmp_path / "math.pyi"
    stub_file.write_text("x: int\n", encoding="utf-8")
    monkeypatch.setattr(
        sys,
        "argv",
        [
            "swig2pyi",
            "coverage",
            "--stub",
            str(stub_file),
            "--module",
            "math",
            "--allowlist",
            str(tmp_path / "nonexistent.txt"),
        ],
    )
    with pytest.raises(SystemExit) as exc_info:
        main()
    assert exc_info.value.code == 1

    # 2. Stub does not exist exit
    monkeypatch.setattr(
        sys,
        "argv",
        [
            "swig2pyi",
            "coverage",
            "--stub",
            str(tmp_path / "nonexistent.pyi"),
            "--module",
            "math",
        ],
    )
    with pytest.raises(SystemExit) as exc_info:
        main()
    assert exc_info.value.code == 1

    # 3. Coverage report returns None because module doesn't exist
    stub_file.write_text("x: int\n", encoding="utf-8")
    monkeypatch.setattr(
        sys,
        "argv",
        [
            "swig2pyi",
            "coverage",
            "--stub",
            str(stub_file),
            "--module",
            "nonexistent_module_foo_bar_baz",
        ],
    )
    with pytest.raises(SystemExit) as exc_info:
        main()
    assert exc_info.value.code == 1

    # 4. Coverage missing symbols exits with 1
    # Live module mock
    import types

    mock_mod = types.ModuleType("mock_mod")
    mock_mod.x = 1
    mock_mod.y = 2  # missing

    monkeypatch.setattr(
        sys,
        "argv",
        [
            "swig2pyi",
            "coverage",
            "--stub",
            str(stub_file),
            "--module",
            "mock_mod",
        ],
    )

    def mock_import(name):
        return mock_mod

    monkeypatch.setattr("swig2pyi.core.qa.importlib.import_module", mock_import)

    with pytest.raises(SystemExit) as exc_info:
        main()
    assert exc_info.value.code == 1


def test_runner_import_swig_failure() -> None:
    import sys
    from unittest.mock import patch

    # Force reload of swig2pyi.core.runner with mocked import failure for swig
    with patch.dict(sys.modules, {"swig": None}):
        if "swig2pyi.core.runner" in sys.modules:
            del sys.modules["swig2pyi.core.runner"]

        import swig2pyi.core.runner as runner_mod

        assert not runner_mod._SWIG_MODULE_AVAILABLE
        assert runner_mod.swig is None

    # Clean up and restore actual runner
    if "swig2pyi.core.runner" in sys.modules:
        del sys.modules["swig2pyi.core.runner"]


def test_emitter_extra_coverage(monkeypatch: pytest.MonkeyPatch) -> None:
    from swig2pyi.core.parser import CDecl, Enum, Parm

    # 1. Test docstring empty/whitespace and multi-line
    config = Config(
        module_name="Test",
        includes=[],
        type_map={},
        smart_pointers=[],
        containers={},
        extra_code=["import typing.Any", "import collections.abc", "class IntEnum:"],
        skip_functions=["skipped_func"],
    )
    tm = TypeManager(config)
    emitter = StubEmitter(tm)
    emitter.emit(Top(module=Module(name="Test")))

    # Docstring empty/whitespace
    emitter._write_docstring("  \n  ")
    # Multi-line docstring
    emitter._write_docstring("Line 1\nLine 2")

    output = emitter.get_output()
    assert '"""Line 1' in output
    assert "import collections.abc" in output

    # 2. _collect_class_methods cycle
    # Class A inherits from B, B from A
    class_a = Class(name="A", kind="class", bases=["B"])
    class_b = Class(name="B", kind="class", bases=["A"])
    # Cycle should not infinite loop
    visited = set()
    name_to_class = {"A": class_a, "B": class_b}
    emitter._cpp_to_py_class_names = {"A": "A", "B": "B"}
    assert emitter._collect_class_methods("A", name_to_class, visited) == []

    # 3. _emit_python_code function/class definitions
    module = Module(
        name="Test",
        python_code=[
            "import os\nfrom datetime import date\ndef my_py_func(a: int, b: str='default', *args, **kwargs) -> bool: pass\n",
            "MY_CONST = 42\nMY_ANN_CONST: float = 3.14\n",
            "class MyPyClass(BaseClass):\n  def method(self: MyPyClass) -> None: pass\n  CLASS_VAR = 'hello'\n  CLASS_ANN_VAR: int = 123\n",
            "class EmptyPyClass: pass\n",
            "invalid python syntax...",
        ],
    )
    top = Top(module=module)
    emitter.emit(top)
    output2 = emitter.get_output()
    assert "import os" in output2
    assert "from datetime import date" in output2
    assert (
        "def my_py_func(a: int, b: str = ..., *args, **kwargs) -> bool: ..." in output2
    )
    assert "MY_CONST: Any" in output2
    assert "MY_ANN_CONST: float" in output2
    assert "class MyPyClass(BaseClass):" in output2
    assert "def method(self: MyPyClass) -> None: ..." in output2
    assert "CLASS_VAR: Any" in output2
    assert "CLASS_ANN_VAR: int" in output2
    assert "class EmptyPyClass:" in output2

    # 4. skip function config
    func_skipped = CDecl(name="skipped_func", kind="function", type="void")
    func_skipped_operator = CDecl(name="operator!", kind="function", type="void")
    func_ok = CDecl(name="ok_func", kind="function", type="void")
    module_funcs = Module(
        name="Test", cdecls=[func_skipped, func_skipped_operator, func_ok]
    )
    emitter = StubEmitter(tm)
    emitter.emit(Top(module=module_funcs))
    output3 = emitter.get_output()
    assert "def ok_func" in output3
    assert "def skipped_func" not in output3
    assert "def operator" not in output3

    # 5. _resolve_var_type with None type, void to None
    emitter = StubEmitter(tm)
    assert emitter._resolve_var_type(None) == "Any"
    assert emitter._resolve_var_type("void") == "None"

    # 6. visit_enum empty enum
    enum_empty = Enum(name="EmptyEnum", items=[])
    emitter = StubEmitter(tm)
    emitter.visit_enum(enum_empty)
    assert "class EmptyEnum(IntEnum):\n    pass" in emitter.get_output()

    # 7. std:: class skipped
    class_std = Class(name="std::vector", kind="class")
    class_ok = Class(name="MyClass", kind="class")
    module_classes = Module(name="Test", classes=[class_std, class_ok])
    emitter = StubEmitter(tm)
    emitter.emit(Top(module=module_classes))
    output4 = emitter.get_output()
    assert "class MyClass" in output4
    assert "class std::vector" not in output4

    # 9. __getitem__ returning void/None iterator Any
    op_getitem = CDecl(
        name="operator[]",
        kind="function",
        type="void",
        parms=[Parm(name="idx", type="int")],
    )
    class_getitem = Class(name="GetClass", kind="class", cdecls=[op_getitem])
    config_op = Config(
        module_name="Test",
        includes=[],
        type_map={},
        smart_pointers=[],
        containers={},
        rename_operators=True,
    )
    tm_op = TypeManager(config_op)
    emitter = StubEmitter(tm_op)
    emitter.emit(Top(module=Module(name="Test", classes=[class_getitem])))
    output6 = emitter.get_output()
    assert "def __iter__(self) -> Iterator[Any]: ..." in output6

    # 10. destructor continue in _group_methods
    dtor = CDecl(name="~GetClass", kind="function", type="void")
    class_dtor = Class(name="DtorClass", kind="class", cdecls=[dtor])
    emitter = StubEmitter(tm)
    emitter.emit(Top(module=Module(name="Test", classes=[class_dtor])))
    output7 = emitter.get_output()
    assert "def ~GetClass" not in output7


def test_runner_build_command_shutil_which_success(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    runner = SwigRunner(swig_path="valid_swig_path")
    runner.use_module = False
    monkeypatch.setattr(shutil, "which", lambda x: "/usr/bin/swig")
    cmd, _env = runner._build_command(
        [], Path("out.xml"), Path("dummy.cpp"), Path("outdir")
    )
    assert cmd[0] == "valid_swig_path"


def test_type_system_normalize_type_prefix() -> None:
    config = Config(
        module_name="Test",
        includes=[],
        type_map={},
        smart_pointers=[],
        containers={},
    )
    tm = TypeManager(config)
    assert tm.normalize_type("Test::MyClass") == "MyClass"
    assert tm.normalize_type("Test.MyClass") == "MyClass"


def test_type_system_clean_template_inner() -> None:
    config = Config(
        module_name="Test",
        includes=[],
        type_map={},
        smart_pointers=[],
        containers={},
    )
    tm = TypeManager(config)
    assert tm._clean_template_inner("(A) + (B)") == "(A) + (B)"
    assert tm._clean_template_inner("((A))") == "A"


def test_type_system_find_matching_paren_index() -> None:
    config = Config(
        module_name="Test",
        includes=[],
        type_map={},
        smart_pointers=[],
        containers={},
    )
    tm = TypeManager(config)
    assert tm._find_matching_paren_index("(abc)") == 4
    assert tm._find_matching_paren_index("abc") == -1


def test_emitter_delegate_handle_methods() -> None:
    from swig2pyi.core.parser import CDecl, Class, Module, Top

    config = Config(
        module_name="Test",
        includes=[],
        type_map={},
        smart_pointers=[],
        containers={},
        delegate_templates=["Handle"],
    )
    tm = TypeManager(config)

    method_ok = CDecl(name="ok_func", kind="function", type="void")
    method_skipped = CDecl(name="operator!", kind="function", type="void")
    method_already_there = CDecl(name="already_there", kind="function", type="void")

    target_class = Class(
        name="MyTarget",
        kind="class",
        cpp_type="MyTarget",
        cdecls=[method_ok, method_skipped, method_already_there],
    )

    handle_method = CDecl(name="already_there", kind="function", type="void")
    handle_class = Class(
        name="MyHandle",
        kind="class",
        cpp_type="Handle<MyTarget>",
        cdecls=[handle_method],
    )

    module = Module(name="Test", classes=[target_class, handle_class])

    emitter = StubEmitter(tm)
    emitter.emit(Top(module=module))
    output = emitter.get_output()
    assert "class MyHandle:" in output
    assert "def ok_func" in output


def test_emitter_pythoncode_func_overrides_and_privates() -> None:
    from swig2pyi.core.parser import Module, Top

    config = Config(
        module_name="Test",
        includes=[],
        type_map={},
        smart_pointers=[],
        containers={},
        pythoncode_signatures={"my_py_func": "(a: int, b: int = ...) -> None"},
    )
    tm = TypeManager(config)
    emitter = StubEmitter(tm)

    module = Module(
        name="Test",
        python_code=[
            "def my_py_func(a, b=1): pass\n",
            "def _private_func(): pass\n",
            "class _PrivateClass: pass\n",
        ],
    )
    emitter.emit(Top(module=module))
    output = emitter.get_output()
    assert "def my_py_func(a: int, b: int = ...) -> None:" in output
    assert "_private_func" not in output
    assert "_PrivateClass" not in output


def test_emitter_misc_uncovered_paths(monkeypatch: pytest.MonkeyPatch) -> None:
    from swig2pyi.core.parser import CDecl, Class, Module, Top

    # 1. config with typemap mapping custom type to "void"
    config_void = Config(
        module_name="Test",
        includes=[],
        type_map={"my_void": "void"},
        smart_pointers=[],
        containers={},
    )
    tm_void = TypeManager(config_void)
    emitter_void = StubEmitter(tm_void)

    # 2. _resolve_var_type with "my_void" returning "None" (covers line 331 of emitter.py)
    assert emitter_void._resolve_var_type("my_void") == "None"

    # 3. _collect_class_methods non-existent base (covers line 161 of emitter.py)
    class_a = Class(name="A", kind="class", bases=["C"])
    visited = set()
    name_to_class = {"A": class_a}
    emitter_void._cpp_to_py_class_names = {"A": "A", "C": "C"}
    assert emitter_void._collect_class_methods("A", name_to_class, visited) == []

    # 4. _emit_module_functions destructor and variable name skipped and getters/setors property defaults
    func_destructor = CDecl(name="~my_func", kind="function", type="void")
    var_skipped = CDecl(name="operator+", kind="variable", type="int")
    var_ok = CDecl(name="my_global_var", kind="variable", type="int")
    module = Module(name="Test", cdecls=[func_destructor, var_skipped, var_ok])
    emitter_void.emit(Top(module=module))
    output = emitter_void.get_output()
    assert "~my_func" not in output
    assert "operator+" not in output
    assert "my_global_var: int" in output
    assert "class cvar_class:" in output
    assert "cvar: cvar_class" in output

    # 7. should_skip_method with rename_operators=True and unmapped operator (covers line 671 of emitter.py)
    config_op = Config(
        module_name="Test",
        includes=[],
        type_map={},
        smart_pointers=[],
        containers={},
        rename_operators=True,
    )
    tm_op = TypeManager(config_op)
    emitter_op = StubEmitter(tm_op)
    op_unmapped = CDecl(name="operator!", kind="function", type="void")
    assert emitter_op.should_skip_method(op_unmapped) is True
