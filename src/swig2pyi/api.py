"""Public API for swig2pyi."""

import os
import tempfile
from pathlib import Path

from swig2pyi.core.ast_models import Class, Top
from swig2pyi.core.config import Config
from swig2pyi.core.emitter import StubEmitter
from swig2pyi.core.parser import SwigXmlParser
from swig2pyi.core.qa import QAValidator
from swig2pyi.core.runner import SwigRunner
from swig2pyi.core.type_system import TypeManager


def collect_enums(top: Top) -> set[str]:
    """Collect all enum names from the AST recursively."""
    enums: set[str] = set()
    if not top.module:
        return enums

    # Module-level enums
    for enum in top.module.enums:
        name = enum.name.split("::")[-1]
        enums.add(name)

    # Class-level enums
    def visit_class(cls: Class, prefix: str = "") -> None:
        cls_name = cls.name.split("::")[-1]
        current_prefix = f"{prefix}{cls_name}." if prefix else f"{cls_name}."
        for enum in cls.enums:
            enum_name = enum.name.split("::")[-1]
            enums.add(current_prefix + enum_name)
            enums.add(enum_name)
        for sub_cls in cls.classes:
            visit_class(sub_cls, current_prefix)

    for cls in top.module.classes:
        visit_class(cls)

    return enums


def generate_from_interface(
    interface_file: Path,
    config: Config,
    output_file: Path,
    swig_path: str = "swig",
    *,
    validate: bool = False,
) -> None:
    """Generate a Python stub (.pyi) file from a SWIG interface (.i) file.

    Args:
        interface_file: Path to the SWIG interface file.
        config: Configuration object.
        output_file: Path to write the generated stub to.
        swig_path: Path to the swig executable.
        validate: Whether to run QA validation (Ruff/Pyright) on the output.

    """
    runner = SwigRunner(swig_path=swig_path)
    xml_fd, xml_path = tempfile.mkstemp(suffix=".xml")
    os.close(xml_fd)
    xml_path_obj = Path(xml_path)

    try:
        runner.run(
            config.includes,
            interface_file,
            xml_path_obj,
            module_name=config.module_name,
        )
        generate_from_xml(xml_path_obj, config, output_file, validate=validate)
    finally:
        if xml_path_obj.exists():
            xml_path_obj.unlink()


def generate_from_xml(
    xml_file: Path,
    config: Config,
    output_file: Path,
    *,
    validate: bool = False,
) -> None:
    """Generate a Python stub (.pyi) file from a pre-generated SWIG XML file.

    Args:
        xml_file: Path to the SWIG XML file.
        config: Configuration object.
        output_file: Path to write the generated stub to.
        validate: Whether to run QA validation (Ruff/Pyright) on the output.

    """
    parser = SwigXmlParser()
    top = parser.parse_file(xml_file)

    enums = collect_enums(top)
    tm = TypeManager(config, enums=enums)
    emitter = StubEmitter(tm)
    emitter.emit(top)

    output_content = emitter.get_output()

    output_file.parent.mkdir(parents=True, exist_ok=True)

    output_file.write_text(output_content)

    if validate:
        qa = QAValidator()
        qa.validate(output_file)
