# pyright: reportUnknownVariableType=false
# pyright: reportUnknownArgumentType=false
# pyright: reportUnknownParameterType=false
# pyright: reportMissingParameterType=false
# pyright: reportUnknownMemberType=false
# pyright: reportUnknownLambdaType=false
import sys
from pathlib import Path
from typing import ClassVar, NoReturn

import pytest

from swig2pyi.cli import main


def test_cli_coverage_missing_stub(
    monkeypatch: pytest.MonkeyPatch, tmp_path: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    stub_file = tmp_path / "nonexistent.pyi"
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
        ],
    )

    with pytest.raises(SystemExit) as exc_info:
        main()

    assert exc_info.value.code == 1
    captured = capsys.readouterr()
    assert "Error: Stub file not found" in captured.err


def test_cli_load_config_nonexistent(
    monkeypatch: pytest.MonkeyPatch, tmp_path: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    nonexistent_config = tmp_path / "missing.json"
    interface_file = tmp_path / "file.i"
    interface_file.write_text("// swig", encoding="utf-8")
    output_file = tmp_path / "out.pyi"

    monkeypatch.setattr(
        sys,
        "argv",
        [
            "swig2pyi",
            "--interface",
            str(interface_file),
            "--config",
            str(nonexistent_config),
            "--output",
            str(output_file),
        ],
    )
    with pytest.raises(SystemExit) as exc_info:
        main()
    assert exc_info.value.code == 1

    captured = capsys.readouterr()
    assert "Error: Config file not found" in captured.err


def test_cli_load_config_invalid(
    monkeypatch: pytest.MonkeyPatch, tmp_path: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    invalid_config = tmp_path / "invalid.json"
    invalid_config.write_text("invalid json content {", encoding="utf-8")
    interface_file = tmp_path / "file.i"
    interface_file.write_text("// swig", encoding="utf-8")
    output_file = tmp_path / "out.pyi"

    monkeypatch.setattr(
        sys,
        "argv",
        [
            "swig2pyi",
            "--interface",
            str(interface_file),
            "--config",
            str(invalid_config),
            "--output",
            str(output_file),
        ],
    )
    with pytest.raises(SystemExit) as exc_info:
        main()
    assert exc_info.value.code == 1

    captured = capsys.readouterr()
    assert "Error: Failed to load config from" in captured.err


def test_cli_coverage_success(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    stub_file = tmp_path / "math.pyi"
    stub_file.write_text("def sin(x: float) -> float: ...\n", encoding="utf-8")

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
        ],
    )

    class MockCoverageReport:
        runtime_symbol_count = 1
        stub_symbol_count = 1
        coverage_pct = 100.0
        allowlisted: ClassVar[list[str]] = []
        missing: ClassVar[list[str]] = []

    class MockChecker:
        def __init__(self, allowlist: set[str] | None = None) -> None:
            pass

        def check(self, _stub: Path, _module: str) -> MockCoverageReport:
            return MockCoverageReport()

    monkeypatch.setattr("swig2pyi.cli.StubCoverageChecker", MockChecker)

    with pytest.raises(SystemExit) as exc_info:
        main()

    assert exc_info.value.code == 0


def test_cli_coverage_with_allowlist(
    monkeypatch: pytest.MonkeyPatch, tmp_path: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    stub_file = tmp_path / "math.pyi"
    stub_file.write_text("def sin(x: float) -> float: ...\n", encoding="utf-8")
    allowlist_file = tmp_path / "allowlist.txt"
    allowlist_file.write_text("# comment\nallowlisted_sym\n", encoding="utf-8")

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

    class MockCoverageReport:
        runtime_symbol_count = 2
        stub_symbol_count = 1
        coverage_pct = 50.0
        allowlisted: ClassVar[list[str]] = ["allowlisted_sym"]
        missing: ClassVar[list[str]] = ["missing_sym"]

    class MockChecker:
        def __init__(self, allowlist: set[str] | None = None) -> None:
            assert allowlist is not None
            assert "allowlisted_sym" in allowlist

        def check(self, _stub: Path, _module: str) -> MockCoverageReport:
            return MockCoverageReport()

    monkeypatch.setattr("swig2pyi.cli.StubCoverageChecker", MockChecker)

    with pytest.raises(SystemExit) as exc_info:
        main()

    assert exc_info.value.code == 1
    captured = capsys.readouterr()
    assert "missing_sym" in captured.err
    assert "allowlisted_sym" in captured.out


def test_cli_coverage_nonexistent_allowlist(
    monkeypatch: pytest.MonkeyPatch, tmp_path: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    stub_file = tmp_path / "math.pyi"
    stub_file.write_text("def sin(x: float) -> float: ...\n", encoding="utf-8")
    nonexistent_allowlist = tmp_path / "missing.txt"

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
            str(nonexistent_allowlist),
        ],
    )

    with pytest.raises(SystemExit) as exc_info:
        main()

    assert exc_info.value.code == 1
    captured = capsys.readouterr()
    assert "Error: Allowlist file not found" in captured.err


def test_cli_generation_interface(
    monkeypatch: pytest.MonkeyPatch, tmp_path: Path
) -> None:
    config_file = tmp_path / "config.json"
    config_file.write_text(
        '{"module_name": "Test", "includes": [], "type_map": {}, "smart_pointers": [], "containers": {}}',
        encoding="utf-8",
    )
    interface_file = tmp_path / "file.i"
    interface_file.write_text("// swig interface\n", encoding="utf-8")
    output_file = tmp_path / "out.pyi"

    monkeypatch.setattr(
        sys,
        "argv",
        [
            "swig2pyi",
            "--interface",
            str(interface_file),
            "--config",
            str(config_file),
            "--output",
            str(output_file),
        ],
    )

    called = []

    def mock_generate_from_interface(interface, config, output, swig_path) -> None:
        called.append(True)

    monkeypatch.setattr(
        "swig2pyi.cli.generate_from_interface", mock_generate_from_interface
    )

    main()
    assert called == [True]


def test_cli_generation_interface_nonexistent(
    monkeypatch: pytest.MonkeyPatch, tmp_path: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    config_file = tmp_path / "config.json"
    config_file.write_text(
        '{"module_name": "Test", "includes": [], "type_map": {}, "smart_pointers": [], "containers": {}}',
        encoding="utf-8",
    )
    nonexistent_interface = tmp_path / "missing.i"
    output_file = tmp_path / "out.pyi"

    monkeypatch.setattr(
        sys,
        "argv",
        [
            "swig2pyi",
            "--interface",
            str(nonexistent_interface),
            "--config",
            str(config_file),
            "--output",
            str(output_file),
        ],
    )

    with pytest.raises(SystemExit) as exc_info:
        main()

    assert exc_info.value.code == 1
    captured = capsys.readouterr()
    assert "Error: Interface file not found" in captured.err


def test_cli_generation_runtime_error(
    monkeypatch: pytest.MonkeyPatch, tmp_path: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    config_file = tmp_path / "config.json"
    config_file.write_text(
        '{"module_name": "Test", "includes": [], "type_map": {}, "smart_pointers": [], "containers": {}}',
        encoding="utf-8",
    )
    interface_file = tmp_path / "file.i"
    interface_file.write_text("// swig interface\n", encoding="utf-8")
    output_file = tmp_path / "out.pyi"

    monkeypatch.setattr(
        sys,
        "argv",
        [
            "swig2pyi",
            "--interface",
            str(interface_file),
            "--config",
            str(config_file),
            "--output",
            str(output_file),
        ],
    )

    def mock_run_generation(args, config) -> NoReturn:
        msg = "QA validation failed for the generated stub."
        raise RuntimeError(msg)

    monkeypatch.setattr("swig2pyi.cli._run_generation", mock_run_generation)

    with pytest.raises(SystemExit) as exc_info:
        main()

    assert exc_info.value.code == 1
    captured = capsys.readouterr()
    assert "Error: QA validation failed for the generated stub." in captured.err
    # Traceback should not be printed
    assert "Traceback" not in captured.err


def test_cli_generation_exception(
    monkeypatch: pytest.MonkeyPatch, tmp_path: Path
) -> None:
    config_file = tmp_path / "config.json"
    config_file.write_text(
        '{"module_name": "Test", "includes": [], "type_map": {}, "smart_pointers": [], "containers": {}}',
        encoding="utf-8",
    )
    interface_file = tmp_path / "file.i"
    interface_file.write_text("// swig interface\n", encoding="utf-8")
    output_file = tmp_path / "out.pyi"

    monkeypatch.setattr(
        sys,
        "argv",
        [
            "swig2pyi",
            "--interface",
            str(interface_file),
            "--config",
            str(config_file),
            "--output",
            str(output_file),
        ],
    )

    def mock_run_generation(args, config) -> NoReturn:
        msg = "test run generation exception"
        raise ValueError(msg)

    monkeypatch.setattr("swig2pyi.cli._run_generation", mock_run_generation)

    with pytest.raises(SystemExit) as exc_info:
        main()

    assert exc_info.value.code == 1


def test_cli_main_entrypoint(monkeypatch: pytest.MonkeyPatch) -> None:
    import runpy

    monkeypatch.setattr(sys, "argv", ["swig2pyi", "--help"])
    with pytest.raises(SystemExit) as exc_info:
        runpy.run_module("swig2pyi.cli", run_name="__main__")
    assert exc_info.value.code == 0


def test_main_py_entrypoint(monkeypatch: pytest.MonkeyPatch) -> None:
    import runpy

    monkeypatch.setattr(sys, "argv", ["swig2pyi", "--help"])
    with pytest.raises(SystemExit) as exc_info:
        runpy.run_module("swig2pyi.main", run_name="__main__")
    assert exc_info.value.code == 0
