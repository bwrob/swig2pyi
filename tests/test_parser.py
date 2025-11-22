"""Tests for the parser module."""

from pathlib import Path

from swig_pyi.models import Class
from swig_pyi.parser import (
    _parse_parameter_type_and_name,
    get_included_files,
    parse_declarations,
    parse_module_name,
    parse_swig_file,  # Added parse_swig_file
    resolve_includes,
)


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


def test_parse_declarations() -> None:
    """Test that the parser can correctly parse class and function declarations."""
    # Given
    swig_file = Path("tests/data/quantlib-1.40/bondfunctions.i")
    content = swig_file.read_text()

    # When
    declarations = parse_declarations(content)

    # Then
    assert len(declarations) == 1
    assert isinstance(declarations[0], Class)
    assert declarations[0].name == "BondFunctions"
    assert len(declarations[0].methods) > 0
    assert declarations[0].methods[0].name == "startDate"
    assert declarations[0].methods[0].return_type == "Date"

    # Test a method with a default parameter
    is_tradable_method = next(
        (m for m in declarations[0].methods if m.name == "isTradable"), None
    )
    assert is_tradable_method is not None
    assert len(is_tradable_method.parameters) == 2
    assert is_tradable_method.parameters[0].name == "bond"
    assert is_tradable_method.parameters[0].type == "const Bond&"
    assert is_tradable_method.parameters[1].name == "settlementDate"
    assert is_tradable_method.parameters[1].type == "Date"
    assert is_tradable_method.parameters[1].default_value == "Date()"


def test_parse_parameter_type_and_name_unnamed() -> None:
    """Test _parse_parameter_type_and_name with an unnamed parameter."""
    # Given
    param_str = "int"

    # When
    param_type, param_name = _parse_parameter_type_and_name(param_str)

    # Then
    assert param_type == "int"
    assert param_name is None


def test_parse_parameter_type_and_name_complex_type() -> None:
    """Test _parse_parameter_type_and_name with a complex type."""
    # Given
    param_str = "const std::string& name"

    # When
    param_type, param_name = _parse_parameter_type_and_name(param_str)

    # Then
    assert param_type == "const std::string&"
    assert param_name == "name"


def test_parse_parameter_type_and_name_template_type() -> None:
    """Test _parse_parameter_type_and_name with a template type."""
    # Given
    param_str = "std::vector<int> myVec"

    # When
    param_type, param_name = _parse_parameter_type_and_name(param_str)

    # Then
    assert param_type == "std::vector<int>"
    assert param_name == "myVec"


def test_parse_swig_file() -> None:
    """Test the main parse_swig_file function."""
    # Given
    entry_file = Path("tests/data/quantlib-1.40/quantlib.i")

    # When
    module_name, swig_files, declarations = parse_swig_file(entry_file)

    # Then
    assert module_name == "QuantLib"
    assert len(swig_files) > 1  # Should include quantlib.i and its includes
    assert len(declarations) > 1  # Should include classes and functions from all files

    # Verify a known class is present
    bond_functions_class = next(
        (d for d in declarations if isinstance(d, Class) and d.name == "BondFunctions"),
        None,
    )
    assert bond_functions_class is not None
    assert isinstance(bond_functions_class, Class)
    assert bond_functions_class.name == "BondFunctions"
    assert len(bond_functions_class.methods) > 0
