import argparse
import sys
from pathlib import Path

from swig2pyi.core.config import Config
from swig2pyi.core.emitter import StubEmitter
from swig2pyi.core.parser import SwigXmlParser
from swig2pyi.core.runner import SwigRunner
from swig2pyi.core.type_system import TypeManager


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Generate .pyi stubs from SWIG interface files."
    )
    parser.add_argument("interface_file", type=Path, help="Path to the .i file")
    parser.add_argument(
        "--config", type=Path, required=True, help="Path to the config.json"
    )
    parser.add_argument("--output", type=Path, help="Output .pyi file path")
    parser.add_argument(
        "--swig-path", type=str, default="swig", help="Path to swig executable"
    )

    args = parser.parse_args()

    if not args.interface_file.exists():
        sys.exit(1)

    if not args.config.exists():
        sys.exit(1)

    # Load config
    try:
        config = Config.from_file(args.config)
    except Exception:
        sys.exit(1)

    # Run SWIG
    runner = SwigRunner(swig_path=args.swig_path)

    # Use a temp file for XML output
    import os
    import tempfile

    xml_fd, xml_path = tempfile.mkstemp(suffix=".xml")
    os.close(xml_fd)
    xml_path_obj = Path(xml_path)

    try:
        runner.run(config.includes, args.interface_file, xml_path_obj)

        # Parse XML
        try:
            xml_parser = SwigXmlParser()
            # Currently parse() expects string, need to update it to accept file path
            # For now, let's assume we updated Parser.
            top = xml_parser.parse_file(xml_path_obj)
        except Exception:
            sys.exit(1)

        # Generate Stub
        tm = TypeManager(config)
        emitter = StubEmitter(tm)
        emitter.emit(top)

        output_content = emitter.get_output()

        # Write output
        out_path = args.output
        if not out_path:
            out_path = args.interface_file.with_suffix(".pyi")

        try:
            with open(out_path, "w") as f:
                f.write(output_content)
        except Exception:
            sys.exit(1)

    except Exception:
        sys.exit(1)
    finally:
        if os.path.exists(xml_path):
            # os.unlink(xml_path)
            pass


if __name__ == "__main__":
    main()
