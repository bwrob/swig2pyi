import os
import tempfile
from pathlib import Path

from helpers import validate_stub

from swig2pyi.core.config import Config
from swig2pyi.core.emitter import StubEmitter
from swig2pyi.core.parser import SwigXmlParser
from swig2pyi.core.runner import SwigRunner
from swig2pyi.core.type_system import TypeManager


def test_handle_overloads_delegation() -> None:
    base_dir = Path(__file__).parent.parent
    interface_file = base_dir / "data" / "synthetic" / "handle_overloads.i"
    config_file = base_dir / "data" / "synthetic" / "handle_overloads.json"

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

        # Check Underlying class exists
        assert "class Underlying:" in generated_output

        # Check Underlying has overloaded foo
        assert (
            "@overload\n    def foo(\n        self,\n        x: int,\n    ) -> None: ..."
            in generated_output
        )
        assert (
            "@overload\n    def foo(\n        self,\n        s: str,\n    ) -> None: ..."
            in generated_output
        )

        # Check UnderlyingHandle inherits from Handle[Underlying] and Underlying
        assert (
            "class UnderlyingHandle(Handle[Underlying], Underlying):"
            in generated_output
        )

        # Verify the delegated foo is present in UnderlyingHandle.
        parts = generated_output.split("class UnderlyingHandle")
        assert len(parts) > 1, "UnderlyingHandle class not found in generated output"
        handle_block = parts[1]

        assert (
            "@overload\n    def foo(\n        self,\n        x: int,\n    ) -> None: ..."
            in handle_block
        )
        assert (
            "@overload\n    def foo(\n        self,\n        s: str,\n    ) -> None: ..."
            in handle_block
        )

    finally:
        if os.path.exists(xml_path):
            os.unlink(xml_path)

    # Run type checks on generated stubs using validate_stub
    fd, path = tempfile.mkstemp(suffix=".pyi")
    os.close(fd)
    path_obj = Path(path)
    try:
        path_obj.write_text(generated_output, encoding="utf-8")
        success = validate_stub(path_obj)
        assert success, "Handle overloads stub type checking failed"
    finally:
        if path_obj.exists():
            path_obj.unlink()
