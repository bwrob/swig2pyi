# pyright: reportPrivateUsage=false
# pyright: reportAttributeAccessIssue=false
import argparse
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Any

import pytest

from swig2pyi.api import collect_enums, generate_from_interface, generate_from_xml
from swig2pyi.cli import _load_config, _run_generation, main
from swig2pyi.core.config import Config
from swig2pyi.core.parser import Class, Module, Top
from swig2pyi.core.qa import CoverageReport, QAValidator, StubCoverageChecker
from swig2pyi.core.runner import SwigRunner


def test_collect_enums_edge_cases() -> None:
    # 1. No module in top
    assert collect_enums(Top(module=None)) == set()

    # 2. Module with sub-classes
    sub_sub_cls = Class(name="SubSub", enums=[])
    sub_cls = Class(name="Sub", classes=[sub_sub_cls])
    cls = Class(name="Parent", classes=[sub_cls])
    module = Module(name="Test", classes=[cls])
    assert collect_enums(Top(module=module)) == set()


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
    generate_from_xml(xml_file, config, output_file, validate=True)
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
    generate_from_interface(interface_file, config, output_file, validate=True)
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


def test_runner_hash_directory_files_edge_cases() -> None:
    runner = SwigRunner()
    import hashlib

    hasher = hashlib.sha256()
    # Nonexistent directory
    runner._hash_directory_files(hasher, Path("nonexistent_dir"))
    # Directory that is a file
    with tempfile.NamedTemporaryFile() as tmp:
        runner._hash_directory_files(hasher, Path(tmp.name))


def test_runner_execute_failures(tmp_path: Path) -> None:
    runner = SwigRunner()
    # 1. SWIG execution failed (OSError)
    with pytest.raises(RuntimeError) as exc_info:
        runner._execute(["/nonexistent/path/to/swig"], {}, tmp_path / "out.xml")
    assert "SWIG execution failed" in str(exc_info.value)

    # 2. SWIG failed (subprocess failure)
    with pytest.raises(RuntimeError) as exc_info:
        runner._execute(["false"], {}, tmp_path / "out.xml")
    assert "SWIG failed" in str(exc_info.value)

    # 3. SWIG succeeded but did not produce output file
    with pytest.raises(RuntimeError) as exc_info:
        runner._execute(["true"], {}, tmp_path / "out.xml")
    assert "SWIG did not produce output file" in str(exc_info.value)


def test_qa_validator_missing_executables(
    monkeypatch: pytest.MonkeyPatch, tmp_path: Path
) -> None:
    validator = QAValidator()
    monkeypatch.setattr(validator, "ruff_path", None)
    monkeypatch.setattr(validator, "pyright_path", None)

    # run_formatting
    success, msg = validator.run_formatting(tmp_path / "dummy.pyi")
    assert not success
    assert "Ruff executable not found" in msg

    # run_type_check
    success, msg = validator.run_type_check(tmp_path / "dummy.pyi")
    assert not success
    assert "Pyright executable not found" in msg

    # validate
    assert not validator.validate(tmp_path / "dummy.pyi")


def test_qa_validator_failed_executions(
    monkeypatch: pytest.MonkeyPatch, tmp_path: Path
) -> None:
    validator = QAValidator()
    dummy_file = tmp_path / "dummy.pyi"
    dummy_file.write_text("invalid syntax ...", encoding="utf-8")

    # Mock subprocess.run to raise CalledProcessError
    def mock_run(*args: Any, **kwargs: Any) -> subprocess.CompletedProcess[bytes]:
        _ = args, kwargs
        raise subprocess.CalledProcessError(
            1, cmd=["ruff"], stderr=b"Mocked Ruff error"
        )

    monkeypatch.setattr(subprocess, "run", mock_run)
    success, msg = validator.run_formatting(dummy_file)
    assert not success
    assert "Ruff failed" in msg


def test_coverage_report_edge_cases() -> None:
    report = CoverageReport(runtime_symbol_count=0, stub_symbol_count=0)
    assert report.coverage_pct == 100.0


def test_stub_coverage_checker_allowlist(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    stub_file = tmp_path / "test.pyi"
    stub_file.write_text("x: int\n", encoding="utf-8")

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
    runner.run(includes=[], interface_file=interface_file, output_xml=out_xml)

    # Second run (cache hit)
    out_xml_2 = tmp_path / "out_2.xml"
    runner.run(includes=[], interface_file=interface_file, output_xml=out_xml_2)
    assert out_xml_2.exists()


def test_qa_validator_success(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    validator = QAValidator()
    monkeypatch.setattr(validator, "ruff_path", "ruff")
    monkeypatch.setattr(validator, "pyright_path", "pyright")

    class MockResult:
        returncode: int = 0
        stdout: str = "Type checking passed."
        stderr: bytes = b""

    # Mock subprocess.run to return code 0
    def mock_run(
        *args: Any,
        **kwargs: Any,
    ) -> MockResult:
        _ = args, kwargs
        return MockResult()

    monkeypatch.setattr(subprocess, "run", mock_run)

    dummy_file = tmp_path / "dummy.pyi"
    dummy_file.write_text("def f(): ...", encoding="utf-8")

    assert validator.validate(dummy_file)


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
