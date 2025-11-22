"""Tests for the parser module."""

from pathlib import Path

from swig_pyi.parser import get_included_files, parse_module_name, resolve_includes


def test_parse_module_name() -> None:
    """Test that the parser can correctly extract the module name."""
    # Given
    swig_file = Path("tests/data/quantlib-1.40/quantlib.i")

    # When
    module_name = parse_module_name(swig_file)

    # Then
    assert module_name == "QuantLib"


def test_get_included_files() -> None:
    """Test that the parser can correctly extract the included files."""
    # Given
    swig_file = Path("tests/data/quantlib-1.40/quantlib.i")
    content = swig_file.read_text()

    # When
    included_files = get_included_files(content)

    # Then
    assert included_files == ["exception.i", "stl.i", "ql.i"]


def test_resolve_includes() -> None:
    """Test that the parser can recursively resolve all included files."""
    # Given
    entry_file = Path("tests/data/quantlib-1.40/quantlib.i")

    # When
    swig_files = resolve_includes(entry_file)
    swig_file_paths = {f.path.name for f in swig_files}

    # Then
    assert "quantlib.i" in swig_file_paths
    assert "ql.i" in swig_file_paths
    assert "common.i" in swig_file_paths
    assert "bonds.i" in swig_file_paths
    assert "options.i" in swig_file_paths
    # The following files are not in the test data, so they should not be in the result.
    # We are testing that the parser does not fail when a file is not found.
    assert "exception.i" not in swig_file_paths
    assert "stl.i" not in swig_file_paths
