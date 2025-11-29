import argparse
import sys
from pathlib import Path

from swig2pyi.core.config import Config
from swig2pyi.core.runner import SwigRunner
from swig2pyi.core.parser import SwigXmlParser
from swig2pyi.core.type_system import TypeManager
from swig2pyi.core.emitter import StubEmitter

def main():
    parser = argparse.ArgumentParser(description="Generate .pyi stubs from SWIG interface files.")
    parser.add_argument("interface_file", type=Path, help="Path to the .i file")
    parser.add_argument("--config", type=Path, required=True, help="Path to the config.json")
    parser.add_argument("--output", type=Path, help="Output .pyi file path")
    parser.add_argument("--swig-path", type=str, default="swig", help="Path to swig executable")
    
    args = parser.parse_args()
    
    if not args.interface_file.exists():
        print(f"Error: Interface file '{args.interface_file}' does not exist.", file=sys.stderr)
        sys.exit(1)

    if not args.config.exists():
        print(f"Error: Config file '{args.config}' does not exist.", file=sys.stderr)
        sys.exit(1)

    # Load config
    try:
        config = Config.from_file(args.config)
    except Exception as e:
        print(f"Error loading config: {e}", file=sys.stderr)
        sys.exit(1)
    
    # Run SWIG
    runner = SwigRunner(swig_path=args.swig_path)
    print(f"Running SWIG on {args.interface_file}...")
    try:
        xml_content = runner.run(config.includes, args.interface_file)
    except Exception as e:
        print(f"Error running SWIG: {e}", file=sys.stderr)
        # Fallback for testing if mock XML is provided? No, let's fail for now.
        sys.exit(1)
    
    # Parse XML
    print("Parsing XML...")
    try:
        xml_parser = SwigXmlParser()
        top = xml_parser.parse(xml_content)
    except Exception as e:
        print(f"Error parsing XML: {e}", file=sys.stderr)
        sys.exit(1)
    
    # Generate Stub
    print("Generating stubs...")
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
        print(f"Successfully wrote {out_path}")
    except Exception as e:
        print(f"Error writing output: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
