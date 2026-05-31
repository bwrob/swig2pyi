import os
import tempfile
from pathlib import Path

from swig2pyi.core.config import Config
from swig2pyi.core.emitter import StubEmitter
from swig2pyi.core.parser import SwigXmlParser
from swig2pyi.core.qa import QAValidator
from swig2pyi.core.runner import SwigRunner
from swig2pyi.core.type_system import TypeManager


def test_synthetic_generation() -> None:
    base_dir = Path(__file__).parent.parent
    interface_file = base_dir / "data" / "synthetic" / "synthetic.i"
    config_file = base_dir / "data" / "synthetic" / "synthetic.json"

    assert interface_file.exists()
    assert config_file.exists()

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

        # Check Enum
        assert "class Color(IntEnum):" in generated_output
        assert "RED = 1" in generated_output
        assert "GREEN = 2" in generated_output
        assert "BLUE = 3" in generated_output

        # Check BaseClass
        assert "class BaseClass:" in generated_output
        # Check default arguments
        assert "def doSomething(" in generated_output

        # Check DerivedClass
        assert "class DerivedClass(BaseClass):" in generated_output
        assert "class Status(IntEnum):" in generated_output
        assert "def __add__(" in generated_output

        # Check SmartPtr delegation
        assert (
            "class DerivedClassPtr(SmartPtr[DerivedClass], DerivedClass):"
            in generated_output
        )
        # Methods delegated from DerivedClass:
        assert "def value(self) -> int: ..." in generated_output
        assert "def setValue(" in generated_output

    finally:
        if os.path.exists(xml_path):
            os.unlink(xml_path)

    # Run type checks on generated stubs using QAValidator
    qa = QAValidator()
    fd, path = tempfile.mkstemp(suffix=".pyi")
    os.close(fd)
    path_obj = Path(path)
    try:
        path_obj.write_text(generated_output, encoding="utf-8")
        success, message = qa.run_type_check(path_obj)
        assert success, f"Synthetic stub type checking failed: {message}"
    finally:
        if path_obj.exists():
            path_obj.unlink()
