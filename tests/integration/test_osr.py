import ast
import os
import tempfile
from pathlib import Path

from helpers import validate_stub

from swig2pyi.core.config import Config
from swig2pyi.core.emitter import StubEmitter
from swig2pyi.core.parser import SwigXmlParser
from swig2pyi.core.type_system import TypeManager


def test_osr_integration() -> None:
    base_dir = Path(__file__).parent.parent
    xml_file = base_dir / "data" / "osr" / "osr.xml"
    config_file = base_dir.parent / "src" / "swig2pyi" / "rules" / "gdal_osr.json"

    assert xml_file.exists()
    assert config_file.exists()

    config = Config.from_file(config_file)

    # Parse XML
    parser = SwigXmlParser()
    top = parser.parse_file(xml_file)

    # Emit stubs
    tm = TypeManager(config)
    emitter = StubEmitter(tm)
    emitter.emit(top)

    generated_output = emitter.get_output()

    # Verify that the generated code is valid python syntax
    ast.parse(generated_output)

    # Verify classes are present
    assert "class SpatialReference:" in generated_output
    assert "class CoordinateTransformation:" in generated_output

    # Verify types and mappings
    # OGRErr is mapped to int
    assert "def ImportFromEPSG(" in generated_output
    assert ") -> int: ..." in generated_output

    # retStringAndCPLFree is mapped to str
    assert "def ExportToWkt(" in generated_output
    assert ") -> str: ..." in generated_output

    # Run type checks on generated stubs using validate_stub
    fd, path = tempfile.mkstemp(suffix=".pyi")
    os.close(fd)
    path_obj = Path(path)
    try:
        path_obj.write_text(generated_output, encoding="utf-8")
        success = validate_stub(path_obj)
        assert success, "GDAL OSR stub type checking failed"
    finally:
        if path_obj.exists():
            path_obj.unlink()
