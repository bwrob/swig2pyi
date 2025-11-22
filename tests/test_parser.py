"""Tests for the parser module."""

from pathlib import Path

from swig_pyi.parser import parse_module_name


def test_parse_module_name() -> None:
    """Test that the parser can correctly extract the module name."""
    # Given
    swig_file = Path("tests/data/quantlib-1.40/quantlib.i")

    # When
    module_name = parse_module_name(swig_file)

    # Then
    assert module_name == "QuantLib"
