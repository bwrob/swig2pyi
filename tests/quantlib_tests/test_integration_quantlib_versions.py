import os
import tempfile
from pathlib import Path

import pytest

from swig2pyi.core.config import Config
from swig2pyi.core.emitter import StubEmitter
from swig2pyi.core.parser import SwigXmlParser
from swig2pyi.core.runner import SwigRunner
from swig2pyi.core.type_system import TypeManager

TESTS_DIR = Path(__file__).parent.parent
DATA_DIR = TESTS_DIR / "data"
CONFIG_FILE = TESTS_DIR.parent / "src" / "swig2pyi" / "rules" / "quantlib.json"

# Find all quantlib version directories since 1.37
versions = sorted(
    [d.name for d in DATA_DIR.glob("quantlib-*") if d.is_dir()],
    key=lambda x: [int(c) for c in x.replace("quantlib-", "").split(".")],
)

# Filter by environment variable if set
test_version = os.environ.get("SWIG2PYI_TEST_VERSION")
if test_version:
    target = (
        test_version
        if test_version.startswith("quantlib-")
        else f"quantlib-{test_version}"
    )
    versions = [v for v in versions if v == target]


@pytest.mark.parametrize("version_folder", versions)
def test_quantlib_full_interface_generation(version_folder: str) -> None:
    """Verify that the full quantlib.i interface generates stubs successfully for this version."""
    version_dir = DATA_DIR / version_folder
    interface_file = version_dir / "quantlib.i"

    assert interface_file.exists(), f"quantlib.i not found in {version_dir}"
    assert CONFIG_FILE.exists()

    config = Config.from_file(CONFIG_FILE)
    # Dynamically set the includes path to point to this version's folder
    config.includes = [str(version_dir)]

    runner = SwigRunner()
    xml_fd, xml_path = tempfile.mkstemp(suffix=".xml")
    os.close(xml_fd)
    xml_path_obj = Path(xml_path)

    try:
        # Run SWIG
        runner.run(config.includes, interface_file, xml_path_obj)

        # Parse XML
        parser = SwigXmlParser()
        top = parser.parse_file(xml_path_obj)

        # Emit Python Stub
        from swig2pyi.api import collect_enums
        enums = collect_enums(top)
        tm = TypeManager(config, enums=enums)
        emitter = StubEmitter(tm)
        emitter.emit(top)

        generated_output = emitter.get_output()

        # Verify that output is not empty and contains expected module header / structure
        assert len(generated_output) > 1000
        assert "class " in generated_output

    finally:
        if xml_path_obj.exists():
            xml_path_obj.unlink()
