import argparse
import sys
from pathlib import Path

from swig2pyi.api import generate_from_interface, generate_from_xml
from swig2pyi.core.config import Config


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Generate .pyi stubs from SWIG interface files or pre-generated XML."
    )
    
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--interface", "-i", type=Path, help="Path to the .i file")
    group.add_argument("--xml", "-x", type=Path, help="Path to a pre-generated SWIG XML file")
    
    parser.add_argument(
        "--config", type=Path, required=True, help="Path to the config.json"
    )
    parser.add_argument("--output", "-o", type=Path, required=True, help="Output .pyi file path")
    parser.add_argument(
        "--swig-path", type=str, default="swig", help="Path to swig executable (used only with --interface)"
    )

    args = parser.parse_args()

    if not args.config.exists():
        print(f"Error: Config file not found: {args.config}", file=sys.stderr)
        sys.exit(1)

    try:
        config = Config.from_file(args.config)
    except Exception as e:
        print(f"Error loading config: {e}", file=sys.stderr)
        sys.exit(1)

    try:
        if args.interface:
            if not args.interface.exists():
                print(f"Error: Interface file not found: {args.interface}", file=sys.stderr)
                sys.exit(1)
            generate_from_interface(args.interface, config, args.output, args.swig_path)
        elif args.xml:
            if not args.xml.exists():
                print(f"Error: XML file not found: {args.xml}", file=sys.stderr)
                sys.exit(1)
            generate_from_xml(args.xml, config, args.output)
            
        print(f"Successfully generated stub at {args.output}")

    except Exception as e:
        print(f"Error during generation: {e}", file=sys.stderr)
        # import traceback
        # traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main()
