"""SWIG to Python Interface Generator."""

from swig2pyi.api import (
    Config,
    CoverageReport,
    StubCoverageChecker,
    generate_from_interface,
    generate_from_xml,
)

__all__ = [
    "Config",
    "CoverageReport",
    "StubCoverageChecker",
    "generate_from_interface",
    "generate_from_xml",
]
