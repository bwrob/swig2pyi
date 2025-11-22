"""Tests for the generator module."""

from pathlib import Path

import pytest

from swig_pyi.models import Class
from swig_pyi.parser import parse_swig_file
from swig_pyi.generator import generate_pyi


def test_generate_pyi_bond_class():
    """Test that the generator can create a .pyi file for the Bond class."""
    # Given
    entry_file = Path("tests/data/quantlib-1.40/quantlib.i")
    _, _, declarations = parse_swig_file(entry_file)

    bond_class = next(
        (d for d in declarations if isinstance(d, Class) and d.name == "Bond"),
        None,
    )
    assert bond_class is not None

    # Expected output for the Bond class
    expected_pyi_path = Path("tests/expected_output/bond.pyi")
    expected_pyi = expected_pyi_path.read_text()

    # When
    generated_pyi = generate_pyi([bond_class])

    # Then
    # For debugging, print the generated output
    print(generated_pyi)
    assert generated_pyi.strip() == expected_pyi.strip()


def test_generate_pyi_yield_term_structure_class():
    """Test that the generator can create a .pyi file for the YieldTermStructure class."""
    # Given
    entry_file = Path("tests/data/quantlib-1.40/quantlib.i")
    _, _, declarations = parse_swig_file(entry_file)

    yts_class = next(
        (d for d in declarations if isinstance(d, Class) and d.name == "YieldTermStructure"),
        None,
    )
    assert yts_class is not None

    # Expected output for the YieldTermStructure class
    expected_pyi_path = Path("tests/expected_output/yieldtermstructure.pyi")
    expected_pyi = expected_pyi_path.read_text()

    # When
    generated_pyi = generate_pyi([yts_class])

    # Then
    # For debugging, print the generated output
    print(generated_pyi)
    assert generated_pyi.strip() == expected_pyi.strip()
