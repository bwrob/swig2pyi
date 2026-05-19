# swig2pyi

A tool to generate high-quality Python type stubs (`.pyi`) from SWIG interface files (`.i`).

## Overview

`swig2pyi` parses the XML output from SWIG to understand the C++ class structure, template instantiations, and type hierarchy. It then generates modern Python 3 type hints, including support for generics, overloads, and standard library types.

It is specifically designed to handle complex libraries like QuantLib, but the architecture is generic enough for other SWIG-wrapped projects.

## Features

*   **Universal Pipeline:** Uses SWIG's XML output (`swig -xml`) as the source of truth, avoiding fragile regex parsing of `.i` files.
*   **Scalable Parsing:** Streams massive XML files into a temporary SQLite database using `sqlmodel`, minimizing RAM usage and allowing complex type resolution via SQL queries.
*   **Robust Type Mapping:** Configuration-driven mapping (`json`) for C++ to Python types, including smart pointers (`std::shared_ptr`) and containers (`std::vector`).
*   **Advanced C++ Support:**
    *   Correctly handles C++ inheritance, including template inheritance (e.g., `Handle<T>`).
    *   Maps C++ enums to Python `IntEnum`.
    *   Resolves overloaded functions and constructors.
*   **QA Integration:** Built-in support for running `ruff` (formatting/linting) and `pyright` (type checking) on the generated stubs.

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

`swig2pyi` can run in two modes:
1.  **Interface Mode:** Runs SWIG to generate XML, then parses it.
2.  **XML Mode:** Parses a pre-generated SWIG XML file.

### Command Line Interface

```bash
# 1. Generate from .i file (requires swig executable)
uv run python -m swig2pyi.main --interface path/to/interface.i --config path/to/config.json --output path/to/output.pyi

# 2. Generate from existing XML file
uv run python -m swig2pyi.main --xml path/to/swig_output.xml --config path/to/config.json --output path/to/output.pyi

# 3. Enable QA Validation (runs ruff & pyright on output)
uv run python -m swig2pyi.main --interface path/to/interface.i --config path/to/config.json --output path/to/output.pyi --validate
```

### Configuration

The configuration file (`config.json`) defines how types are mapped. See `src/swig2pyi/rules/quantlib.json` for a comprehensive example.

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

### Running Tests

```bash
# Run all tests
uv run pytest

# Run specific test
uv run pytest tests/test_parser_enum.py
```

### Project Structure

*   `src/swig2pyi/core`: Core logic (Parser, Emitter, TypeSystem, Runner, QA).
*   `src/swig2pyi/rules`: Default configuration rules.
*   `tests`: Unit and integration tests.
