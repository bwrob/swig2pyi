import sys
from pathlib import Path
from typing import ClassVar

import pytest

from swig2pyi.cli import main


def test_cli_coverage_missing_stub(
    monkeypatch: pytest.MonkeyPatch, tmp_path: Path
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
