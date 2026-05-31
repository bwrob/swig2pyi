# swig2pyi

[![PyPI version](https://img.shields.io/pypi/v/swig2pyi.svg?style=flat-square)](https://pypi.org/project/swig2pyi)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/swig2pyi.svg?style=flat-square)](https://pypi.org/pypi/swig2pyi/)
[![downloads](https://static.pepy.tech/badge/swig2pyi/month)](https://pepy.tech/project/swig2pyi)
[![license](https://img.shields.io/github/license/bwrob/swig2pyi.svg)](https://github.com/bwrob/swig2pyi/blob/main/LICENSE)

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
    *   Mapping C++ enums to Python `IntEnum` and exporting enum members globally.
    *   Overloaded function/constructor resolution.
    *   Smart pointer delegation and template class wrappers.
    *   SWIG `cvar` global variables container emulation.
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

## Quick Start

`swig2pyi` operates in two modes:
1.  **Interface Mode:** Invokes SWIG under the hood to generate XML, then emits stubs.
2.  **XML Mode:** Parses a pre-generated SWIG XML file directly.

```bash
# 1. Generate from a SWIG interface .i file
uv run swig2pyi --interface path/to/interface.i --config path/to/config.json --output path/to/output.pyi

# 2. Generate from a pre-compiled XML file
uv run swig2pyi --xml path/to/swig_output.xml --config path/to/config.json --output path/to/output.pyi
```
