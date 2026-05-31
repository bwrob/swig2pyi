"""Command line interface for swig2pyi."""

import argparse
import sys
from pathlib import Path

from swig2pyi.api import (
    Config,
    CoverageReport,
    StubCoverageChecker,
    generate_from_interface,
    generate_from_xml,
)


def main() -> None:
    """Entry point for the swig2pyi CLI."""
    if len(sys.argv) > 1 and sys.argv[1] == "coverage":
        _run_coverage_cli()

    parser = _setup_parser()
    args = parser.parse_args()
    config = _load_config(args.config)

    try:
        _run_generation(args, config)
    except RuntimeError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
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
        print(f"Error: Config file not found: {path}", file=sys.stderr)
        sys.exit(1)
    try:
        return Config.from_file(path)
    except Exception as e:  # noqa: BLE001
        print(f"Error: Failed to load config from {path}: {e}", file=sys.stderr)
        sys.exit(1)


def _run_generation(args: argparse.Namespace, config: Config) -> None:
    if args.interface:
        if not args.interface.exists():
            print(f"Error: Interface file not found: {args.interface}", file=sys.stderr)
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
            print(f"Error: XML file not found: {args.xml}", file=sys.stderr)
            sys.exit(1)
        generate_from_xml(args.xml, config, args.output, validate=args.validate)


def _load_allowlist(path: Path | None) -> set[str]:
    """Parse allowlist file and return its set of symbols."""
    if not path:
        return set()
    if not path.exists():
        print(f"Error: Allowlist file not found: {path}", file=sys.stderr)
        sys.exit(1)
    with path.open("r", encoding="utf-8") as f:
        return {
            line.strip()
            for line in f
            if line.strip() and not line.strip().startswith("#")
        }


def _print_coverage_report(report: CoverageReport | None, module_name: str) -> None:
    """Print stub coverage diagnostics and handle exit codes."""
    if report is None:
        print(
            f"Error: Coverage check failed. Could not import module: {module_name}",
            file=sys.stderr,
        )
        sys.exit(1)

    print(f"Stub coverage check for module {module_name}:")
    print(f"  Runtime symbols: {report.runtime_symbol_count}")
    print(f"  Stub symbols: {report.stub_symbol_count}")
    print(f"  Coverage: {report.coverage_pct:.2f}%")

    if report.allowlisted:
        print(f"  Allowlisted missing symbols ({len(report.allowlisted)}):")
        for sym in report.allowlisted:
            print(f"    - {sym}")

    if report.missing:
        print(f"  Missing symbols ({len(report.missing)}):", file=sys.stderr)
        for sym in report.missing:
            print(f"    - {sym}", file=sys.stderr)
        sys.exit(1)
    else:
        sys.exit(0)


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
        print(f"Error: Stub file not found: {args.stub}", file=sys.stderr)
        sys.exit(1)

    allowlist_set = _load_allowlist(args.allowlist)
    checker = StubCoverageChecker(allowlist=allowlist_set)
    report = checker.check(args.stub, args.module)

    _print_coverage_report(report, args.module)


if __name__ == "__main__":
    main()
