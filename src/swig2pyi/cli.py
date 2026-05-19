"""Command line interface for swig2pyi."""

import argparse
import sys
from pathlib import Path

from swig2pyi.api import generate_from_interface, generate_from_xml
from swig2pyi.core.config import Config


def main() -> None:
    """Entry point for the swig2pyi CLI."""
    parser = _setup_parser()
    args = parser.parse_args()
    config = _load_config(args.config)

    try:
        _run_generation(args, config)
    except Exception:  # noqa: BLE001
        import traceback  # noqa: PLC0415

        traceback.print_exc()
        sys.exit(1)


def _setup_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Generate .pyi stubs from SWIG interface files or XML."
    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--interface", "-i", type=Path, help="Path to the .i file")
    group.add_argument(
        "--xml", "-x", type=Path, help="Path to a pre-generated SWIG XML file"
    )
    parser.add_argument(
        "--config", type=Path, required=True, help="Path to the config.json"
    )
    parser.add_argument(
        "--output", "-o", type=Path, required=True, help="Output .pyi file path"
    )
    parser.add_argument(
        "--swig-path", type=str, default="swig", help="Path to swig executable"
    )
    parser.add_argument(
        "--validate", "-v", action="store_true", help="Run QA validation"
    )
    return parser


def _load_config(path: Path) -> Config:
    if not path.exists():
        sys.exit(1)
    try:
        return Config.from_file(path)
    except Exception:  # noqa: BLE001
        sys.exit(1)


def _run_generation(args: argparse.Namespace, config: Config) -> None:
    if args.interface:
        if not args.interface.exists():
            sys.exit(1)
        generate_from_interface(
            args.interface,
            config,
            args.output,
            args.swig_path,
            validate=args.validate,
        )
    elif args.xml:
        if not args.xml.exists():
            sys.exit(1)
        generate_from_xml(args.xml, config, args.output, validate=args.validate)


if __name__ == "__main__":
    main()
