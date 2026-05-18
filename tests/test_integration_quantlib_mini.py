import os
import tempfile
from pathlib import Path

from swig2pyi.core.config import Config
from swig2pyi.core.emitter import StubEmitter
from swig2pyi.core.parser import SwigXmlParser
from swig2pyi.core.runner import SwigRunner
from swig2pyi.core.type_system import TypeManager


def test_quantlib_mini_generation() -> None:
    base_dir = Path(__file__).parent
    interface_file = base_dir / "data" / "quantlib-1.40" / "quantlib_mini.i"
    config_file = base_dir.parent / "src" / "swig2pyi" / "rules" / "quantlib.json"
    expected_output_file = base_dir / "expected_output" / "quantlib_mini.pyi"

    assert interface_file.exists()
    assert config_file.exists()
    assert expected_output_file.exists()

    config = Config.from_file(config_file)

    # Run SWIG to get XML
    runner = SwigRunner()
    xml_fd, xml_path = tempfile.mkstemp(suffix=".xml")
    os.close(xml_fd)
    xml_path_obj = Path(xml_path)

    try:
        runner.run(config.includes, interface_file, xml_path_obj)

        # Parse
        parser = SwigXmlParser()
        top = parser.parse_file(xml_path_obj)

        # Emit
        tm = TypeManager(config)
        emitter = StubEmitter(tm)
        emitter.emit(top)

        generated_output = emitter.get_output()

        # Compare with expected
        with open(expected_output_file) as f:
            expected_output = f.read()

        # Normalize line endings just in case
        assert generated_output.strip() == expected_output.strip()

    finally:
        if os.path.exists(xml_path):
            os.unlink(xml_path)