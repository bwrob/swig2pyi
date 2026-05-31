import os
import tempfile
from pathlib import Path

from swig2pyi.core.config import Config
from swig2pyi.core.emitter import StubEmitter
from swig2pyi.core.parser import SwigXmlParser
from swig2pyi.core.qa import QAValidator
from swig2pyi.core.runner import SwigRunner
from swig2pyi.core.type_system import TypeManager


def test_vector_and_typedef_relaxation() -> None:
    base_dir = Path(__file__).parent.parent
    interface_file = base_dir / "data" / "synthetic" / "vector_typedefs.i"
    config_file = base_dir / "data" / "synthetic" / "vector_typedefs.json"

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

        # 1. Verify DoubleVector has standard list base and constructor overloads
        assert "class DoubleVector(list[float]):" in generated_output
        assert "def __init__(self) -> None: ..." in generated_output
        assert (
            "def __init__(self, iterable: Iterable[float] = ...) -> None: ..."
            in generated_output
        )
        assert "def __init__(self, size: int) -> None: ..." in generated_output
        assert (
            "def __init__(self, size: int, value: float) -> None: ..."
            in generated_output
        )

        # 2. Verify standard vector methods are injected
        assert "def push_back(self, x: float) -> None: ..." in generated_output
        assert "def resize(self, n: int) -> None: ..." in generated_output
        assert "def size(self) -> int: ..." in generated_output
        assert "def empty(self) -> bool: ..." in generated_output
        assert "def clear(self) -> None: ..." in generated_output

        # 3. Verify parameter relaxation on sum and sum_relaxed
        # sum takes std::vector<double> -> DoubleVector, should allow Sequence[float]
        assert (
            "def sum(\n        self,\n        v: Union[DoubleVector, Sequence[float]],\n    ) -> float: ..."
            in generated_output
        )

        # sum_relaxed takes RealVector (typedef to std::vector<double>) -> DoubleVector, should allow Sequence[float]
        assert (
            "def sum_relaxed(\n        self,\n        v: Union[DoubleVector, Sequence[float]],\n    ) -> float: ..."
            in generated_output
        )

        # 4. Verify Matrix parameter relaxation to Sequence[Sequence[float]]
        assert (
            "def sum_matrix(\n        self,\n        m: Union[DoubleVectorVector, Sequence[Sequence[float]]],\n    ) -> float: ..."
            in generated_output
        )

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
        assert success, f"Vectors stub type checking failed: {message}"
    finally:
        if path_obj.exists():
            path_obj.unlink()
