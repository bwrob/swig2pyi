# CLI Reference

`swig2pyi` is a command line utility for generating Python type stubs and verifying stub coverage.

## Global Options

### Stub Generation

Run stub generation using the options below:

```bash
uv run swig2pyi [options]
```

#### `--interface`, `-i`
*   **Type:** `Path` (Mutually exclusive with `--xml`)
*   **Description:** Path to the SWIG interface `.i` file. Invokes the SWIG compiler under the hood to generate XML prior to emitting stubs.

#### `--xml`, `-x`
*   **Type:** `Path` (Mutually exclusive with `--interface`)
*   **Description:** Path to a pre-compiled SWIG XML file. Direct-to-memory streaming parses the XML directly.

#### `--config`
*   **Type:** `Path` (Required)
*   **Description:** Path to the `config.json` rules file.

#### `--output`, `-o`
*   **Type:** `Path` (Required)
*   **Description:** Path to the output `.pyi` type stub file to be generated.

#### `--swig-path`
*   **Type:** `str` (Default: `swig`)
*   **Description:** Path to the `swig` executable. Only used in Interface Mode.

#### `--validate`, `-v`
*   **Type:** Flag
*   **Description:** Runs QA validation (Ruff formatting checks and strict Basedpyright type check validation) against the generated stub file.

---

### Stub Coverage Check

Exposes a CLI subcommand to check stub completeness against a loaded python package.

```bash
uv run swig2pyi coverage --stub <stub.pyi> --module <name> [options]
```

#### `--stub`
*   **Type:** `Path` (Required)
*   **Description:** Path to the generated `.pyi` stub file to check.

#### `--module`
*   **Type:** `str` (Required)
*   **Description:** Name of the importable Python runtime module (e.g. `QuantLib` or `math`).

#### `--allowlist`
*   **Type:** `Path` (Optional)
*   **Description:** Path to a text file containing allowlisted symbols (one per line, comments starting with `#` are ignored) that should be skipped if missing from the stub.
