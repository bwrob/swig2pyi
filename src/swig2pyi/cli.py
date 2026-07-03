"""Command line interface for swig2pyi."""

import sys
from pathlib import Path
from types import SimpleNamespace
from typing import Any

import typer

from swig2pyi.api import (
    Config,
    CoverageReport,
    StubCoverageChecker,
    generate_from_interface,
    generate_from_xml,
)

app = typer.Typer(
    help="Generate .pyi stubs from SWIG interface files or XML.",
    no_args_is_help=True,
)


@app.callback(invoke_without_command=True)
def main_callback(
    ctx: typer.Context,
    interface: Path = typer.Option(
        None, "--interface", "-i", help="Path to the .i file"
    ),
    xml: Path = typer.Option(
        None, "--xml", "-x", help="Path to a pre-generated SWIG XML file"
    ),
    config: Path = typer.Option(None, "--config", help="Path to the config.json"),
    output: Path = typer.Option(None, "--output", "-o", help="Output .pyi file path"),
    swig_path: str = typer.Option(
        "swig", "--swig-path", help="Path to swig executable"
    ),
    filter_file: Path = typer.Option(
        None,
        "--filter-file",
        help="Path to a file containing a list of symbols to include",
    ),
) -> None:
    """Generate .pyi stubs from SWIG interface files or XML."""
    if ctx.invoked_subcommand is not None:
        return

    _validate_inputs(interface, xml, config, output)

    if not config or not output:
        return

    cfg = _load_config(config)

    # Load filter file if provided
    if filter_file:
        symbols = _parse_filter_file(filter_file)
        cfg.include_symbols.extend(symbols)

    args = SimpleNamespace(
        interface=interface,
        xml=xml,
        config=config,
        output=output,
        swig_path=swig_path,
    )

    try:
        _run_generation(args, cfg)
    except RuntimeError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}", file=sys.stderr)
        sys.exit(1)


def _validate_inputs(
    interface: Path | None, xml: Path | None, config: Path | None, output: Path | None
) -> None:
    if not interface and not xml:
        print("Error: Must specify either --interface or --xml", file=sys.stderr)
        sys.exit(1)
    if interface and xml:
        print("Error: Cannot specify both --interface and --xml", file=sys.stderr)
        sys.exit(1)

    if not config:
        print("Error: Missing option '--config'", file=sys.stderr)
        sys.exit(1)
    if not output:
        print("Error: Missing option '--output'", file=sys.stderr)
        sys.exit(1)


def _parse_filter_file(filter_file: Path) -> list[str]:
    if not filter_file.exists():
        print(f"Error: Filter file not found: {filter_file}", file=sys.stderr)
        sys.exit(1)
    symbols: list[str] = []
    with filter_file.open("r", encoding="utf-8") as f:
        for raw_line in f:
            line = raw_line.strip()
            if line and not line.startswith("#"):
                symbols.append(line)
    return symbols


def _run_generation(args: Any, config: Config) -> None:
    """Run stub generation (retained for test compatibility)."""
    interface = getattr(args, "interface", None)
    xml = getattr(args, "xml", None)
    output = getattr(args, "output", None)
    swig_path = getattr(args, "swig_path", "swig")

    if interface:
        interface_path = Path(interface)
        if not interface_path.exists():
            print(f"Error: Interface file not found: {interface_path}", file=sys.stderr)
            sys.exit(1)
        if not output:
            sys.exit(1)
        generate_from_interface(interface_path, config, Path(output), swig_path)
    elif xml:
        xml_path = Path(xml)
        if not xml_path.exists():
            print(f"Error: XML file not found: {xml_path}", file=sys.stderr)
            sys.exit(1)
        if not output:
            sys.exit(1)
        generate_from_xml(xml_path, config, Path(output))


def _load_config(path: Path) -> Config:
    if not path.exists():
        print(f"Error: Config file not found: {path}", file=sys.stderr)
        sys.exit(1)
    try:
        return Config.from_file(path)
    except Exception as e:
        print(f"Error: Failed to load config from {path}: {e}", file=sys.stderr)
        sys.exit(1)


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


@app.command("coverage")
def coverage(
    stub: Path = typer.Option(..., "--stub", help="Path to the .pyi stub file"),
    module: str = typer.Option(
        ..., "--module", help="Name of the importable Python module"
    ),
    allowlist: Path = typer.Option(
        None,
        "--allowlist",
        help="Path to a text file containing allowlisted symbols (one per line)",
    ),
) -> None:
    """Check stub coverage against a runtime module."""
    if not stub.exists():
        print(f"Error: Stub file not found: {stub}", file=sys.stderr)
        sys.exit(1)

    allowlist_set = _load_allowlist(allowlist)
    checker = StubCoverageChecker(allowlist=allowlist_set)
    report = checker.check(stub, module)

    _print_coverage_report(report, module)


def main() -> None:
    """Entry point for the swig2pyi CLI."""
    is_generation = (
        "coverage" not in sys.argv and "--help" not in sys.argv and "-h" not in sys.argv
    )

    try:
        app()
    except SystemExit as e:
        if e.code == 0 and is_generation:
            return
        raise


if __name__ == "__main__":
    main()
