import os
import tempfile
from pathlib import Path

from swig2pyi.core.config import Config
from swig2pyi.core.emitter import StubEmitter
from swig2pyi.core.parser import SwigXmlParser
from swig2pyi.core.runner import SwigRunner
from swig2pyi.core.type_system import TypeManager


def test_operator_remapping() -> None:
    base_dir = Path(__file__).parent
    interface_file = base_dir / "data" / "synthetic" / "operators.i"
    config_file = base_dir / "data" / "synthetic" / "operators.json"

    assert interface_file.exists()
    assert config_file.exists()

    config = Config.from_file(config_file)

    runner = SwigRunner()
    xml_fd, xml_path = tempfile.mkstemp(suffix=".xml")
    os.close(xml_fd)
    xml_path_obj = Path(xml_path)

    try:
        runner.run(config.includes, interface_file, xml_path_obj)

        parser = SwigXmlParser()
        top = parser.parse_file(xml_path_obj)

        tm = TypeManager(config)
        emitter = StubEmitter(tm)
        emitter.emit(top)

        generated_output = emitter.get_output()

        # Check OpClass exists
        assert "class OpClass:" in generated_output

        # Verify comparison operators
        assert "def __eq__(" in generated_output
        assert "def __ne__(" in generated_output
        assert "def __lt__(" in generated_output
        assert "def __le__(" in generated_output
        assert "def __gt__(" in generated_output
        assert "def __ge__(" in generated_output

        # Verify call operator
        assert "def __call__(" in generated_output

        # Verify getitem (index) operator
        assert "def __getitem__(" in generated_output

        # Verify arithmetic operators
        assert "def __add__(" in generated_output
        assert "def __sub__(" in generated_output
        assert "def __mul__(" in generated_output
        assert "def __truediv__(" in generated_output

        # Verify dereference operator
        assert "def __deref__(" in generated_output

    finally:
        if os.path.exists(xml_path):
            os.unlink(xml_path)
