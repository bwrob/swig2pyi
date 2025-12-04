import os
import sys
import tempfile
import time
from pathlib import Path

# Ensure the project root is in the path to find swig2pyi modules
sys.path.insert(0, str(Path(__file__).parent))

from src.swig2pyi.core.config import Config
from src.swig2pyi.core.emitter import StubEmitter
from src.swig2pyi.core.parser import SwigXmlParser
from src.swig2pyi.core.runner import SwigRunner
from src.swig2pyi.core.type_system import TypeManager


def run_full_test() -> None:
    base_dir = Path(__file__).parent / "tests"
    # Point to the FULL quantlib.i
    interface_file = base_dir / "data" / "quantlib-1.40" / "quantlib.i"
    config_file = base_dir.parent / "src" / "swig2pyi" / "rules" / "quantlib.json"
    output_dir = base_dir / "expected_output" / "QuantLib"
    output_dir.mkdir(parents=True, exist_ok=True)
    output_file = output_dir / "__init__.pyi"

    assert interface_file.exists(), f"Interface file not found: {interface_file}"
    assert config_file.exists(), f"Config file not found: {config_file}"

    config = Config.from_file(config_file)

    time.time()

    runner = SwigRunner()
    xml_fd, xml_path = tempfile.mkstemp(suffix=".xml")
    os.close(xml_fd)
    xml_path_obj = Path(xml_path)

    try:
        runner.run(config.includes, interface_file, xml_path_obj)
        time.time()

        parser = SwigXmlParser()
        top = parser.parse_file(xml_path_obj)
        time.time()

        tm = TypeManager(config)
        emitter = StubEmitter(tm)
        emitter.emit(top)

        time.time()

        generated_output = emitter.get_output()

        with open(output_file, "w") as f:
            f.write(generated_output)

    except Exception:
        import traceback
        traceback.print_exc()
    finally:
        # Keep XML for inspection if needed, or comment out to delete
        if os.path.exists(xml_path):
            # os.unlink(xml_path)
            pass

if __name__ == "__main__":
    run_full_test()
