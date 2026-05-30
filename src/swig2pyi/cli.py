"""Command line interface for swig2pyi."""

import argparse
import sys
from pathlib import Path

from swig2pyi.api import generate_from_interface, generate_from_xml
from swig2pyi.core.config import Config
from swig2pyi.core.qa import StubCoverageChecker


def main() -> None:
    """Entry point for the swig2pyi CLI."""
    if len(sys.argv) > 1 and sys.argv[1] == "coverage":
        _run_coverage_cli()
        return

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


def _run_coverage_cli() -> None:
    parser = argparse.ArgumentParser(
        description="Check stub coverage against a runtime module."
    )
    # sys.argv[0] is swig2pyi, sys.argv[1] is coverage.
    # We parse the remaining arguments:
    parser.add_argument("cmd", choices=["coverage"])
    parser.add_argument(
        "--stub", type=Path, required=True, help="Path to the .pyi stub file"
    )
    parser.add_argument(
        "--module",
        type=str,
        required=True,
        help="Name of the importable Python module",
    )
    parser.add_argument(
        "--allowlist",
        type=Path,
        help="Path to a text file containing allowlisted symbols (one per line)",
    )

    args = parser.parse_args()

    if not args.stub.exists():
        sys.exit(1)

    allowlist_set: set[str] = set()
    if args.allowlist:
        if not args.allowlist.exists():
            sys.exit(1)
        with args.allowlist.open("r", encoding="utf-8") as f:
            allowlist_set = {
                line.strip()
                for line in f
                if line.strip() and not line.strip().startswith("#")
            }

    checker = StubCoverageChecker(allowlist=allowlist_set)
    report = checker.check(args.stub, args.module)

    if report is None:
        sys.exit(1)

    if report.allowlisted:
        pass
    if report.missing:
        for _sym in report.missing:
            pass
        sys.exit(1)
    else:
        sys.exit(0)


if __name__ == "__main__":
    main()
