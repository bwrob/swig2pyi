# swig2pyi

A tool to generate high-quality Python type stubs (`.pyi`) from SWIG interface files (`.i`) or SWIG XML outputs (`.xml`).

## Overview

`swig2pyi` parses the XML output from SWIG to extract C++ class structures, template instantiations, and type hierarchies. It then generates modern Python type hints, including support for generics, method overloads, and standard library types.

While designed to handle complex wrappers like QuantLib and GDAL (OSR), the architecture is generic and rule-driven, allowing it to adapt to any SWIG-wrapped project.

## Features

*   **Universal Pipeline:** Uses SWIG's XML output (`swig -xml`) as the source of truth, avoiding fragile regex parsing of `.i` files.
*   **Scalable Parsing:** Streams massive XML files in a single pass using `xml.etree.ElementTree.iterparse` directly into a strongly-typed Pydantic AST, minimizing memory overhead.
*   **Robust Type Mapping:** Configuration-driven rules (`json`) for C++ to Python type mappings, smart pointer resolution (`std::shared_ptr`), and templates.
*   **Advanced C++ Support:**
    *   Inheritance hierarchies, including template bases.
    *   Mapping C++ enums to Python `IntEnum`.
    *   Overloaded function/constructor resolution.
    *   Smart pointer delegation and template class wrappers.
*   **QA Integration:** Automated formatting (`ruff`) and type verification (`pyright`/`basedpyright`) on the generated stubs to ensure 100% compliance.

## Installation

This project uses `uv` for dependency management.

```bash
# Clone the repository
git clone https://github.com/bwrob/swig2pyi.git
cd swig2pyi

# Install dependencies
uv sync
```

## Usage

`swig2pyi` operates in two modes:
1.  **Interface Mode:** Invokes SWIG under the hood to generate XML, then emits stubs.
2.  **XML Mode:** Parses a pre-generated SWIG XML file directly.

### Command Line Interface

You can run the generator using the `swig2pyi` executable wrapper:

```bash
# 1. Generate from a SWIG interface .i file (requires swig executable)
uv run swig2pyi --interface path/to/interface.i --config path/to/config.json --output path/to/output.pyi

# 2. Generate from a pre-compiled XML file
uv run swig2pyi --xml path/to/swig_output.xml --config path/to/config.json --output path/to/output.pyi

# 3. Filter output to only include specific symbols and their dependencies
uv run swig2pyi --xml path/to/swig_output.xml --config path/to/config.json --output path/to/output.pyi --filter-file path/to/filter.txt
```

### Configuration

The configuration file defines the module rules. Pre-defined rules for QuantLib and GDAL are located under `src/swig2pyi/rules/`.

```json
{
    "module_name": "QuantLib",
    "includes": ["quantlib.i"],
    "type_map": {
        "Integer": "int",
        "Real": "float",
        "Size": "int"
    },
    "smart_pointers": ["std::shared_ptr", "boost::shared_ptr"],
    "containers": {
        "std::vector": "list",
        "std::map": "dict"
    },
    "rename_operators": true
}
```

## Development

The project uses `poethepoet` to manage development workflows.

```bash
# Run all code quality tools (linting, formatting, type checking, and complexity)
uv run poe code-quality

# Run unit tests
uv run poe test

# Run heavy integration tests (requires QuantLib build/dependencies)
uv run poe test-heavy

# Measure test coverage
uv run poe coverage
```

### Project Structure

*   `src/swig2pyi/core`: Core parser, type system, naming managers, emitters, and QA validators.
*   `src/swig2pyi/rules`: Pre-configured rules and type mappings for target libraries.
*   `tests`: Unit and integration test suite.
