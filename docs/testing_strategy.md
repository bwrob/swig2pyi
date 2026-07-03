# Testing Strategy

This document outlines the testing strategy, test suites, and validation workflows utilized by `swig2pyi` to ensure correctness, type-safety compliance, and performance.

---

## 1. Test Architecture

The test suite is divided into three logical tiers: Unit Tests, Integration/Synthetic Tests, and Heavy Integration Tests (QuantLib).

```mermaid
graph TD
    subgraph Unit Tests [1. Unit Tests]
        test_cli.py
        test_type_manager.py
        test_parser.py
        test_emitter.py
    end

    subgraph Integration Tests [2. Integration Tests]
        test_operators.py
        test_vectors.py
        test_swig_sections.py
        test_osr.py
    end

    subgraph Heavy Integration Tests [3. Heavy Integration Tests]
        test_integration_quantlib_mini.py
        test_integration_quantlib_full.py
        test_static_verification.py
    end

    Unit Tests --> Integration Tests --> Heavy Integration Tests
```

---

## 2. Testing Tiers

### 2.1. Unit Tests (`tests/unit/`)
Unit tests focus on isolating specific helper functions, parsing algorithms, and logic units. They run fast and require no external compilation dependencies.
*   **Parser & AST Verification:** Tests inside `test_parser.py`, `test_parser_enum.py`, and `test_parser_features.py` check if `SwigXmlParser` correctly maps C++ constructs to AST nodes.
*   **Type Resolution (`test_type_manager.py`):** Asserts template argument limiting, typedef expansion, pointer dereferencing, and namespace stripping logic.
*   **Emission (`test_emitter.py`, `test_import_tracking.py`):** Ensures that dynamic import tracking works perfectly and `StubEmitter` outputs syntactically correct Python type signatures.
*   **CLI & Diagnostics (`test_cli.py`):** Tests parameter handling, logging outputs, coverage subcommands, allowlist loading, and failure exits.

### 2.2. Integration & Synthetic Tests (`tests/integration/`)
These tests execute the full generation pipeline using small C++ interface files (`.i`) or mocked XML outputs. They verify that specific SWIG capabilities are correctly handled:
*   **Operator Mapping (`test_operators.py`):** Checks if C++ operators (`operator==`, `operator[]`) map to dunders.
*   **Sequence/Vector Parameter Relaxation (`test_vectors.py`):** Verifies that parameter signatures accepting std::vectors accept generic sequences (e.g. `Sequence[float]`).
*   **SWIG Specification Verification (`test_swig_sections.py`):** Dedicated tests covering SWIG Python sections (33.3.1 to 33.3.15).
*   **Multi-Library Portability (`test_osr.py`, `test_osr_static.py`):** Validates GDAL Spatial Reference System (OSR) interface parsing and stubs.

### 2.3. Heavy Integration Tests (`tests/quantlib_tests/`)
These tests require the QuantLib Python wrapper and verify the generated type stubs against real-world library tests.
*   **Stub Coverage (`test_static_verification.py`):** Scans the generated QuantLib stub file against the compiled runtime `QuantLib` module to find missing classes, methods, or attributes.
*   **Strict Type Verification (`test_integration_quantlib_full.py`):** Runs `basedpyright` in strict mode on 35+ real Python tests from the QuantLib test suite (e.g. `european_option.py`, `bonds.py`, `bermudan_swaption.py`), making sure the type checker detects zero errors with the generated stubs.

---

## 3. Development Workflow & Commands

Development tasks are automated via Poe tasks defined in `pyproject.toml`:

```bash
# Run lightweight unit and synthetic tests
uv run poe test

# Run heavy integration tests (requires QuantLib build/dependencies)
uv run poe test-heavy

# Measure test coverage (target: 90%+)
uv run poe coverage

# Run all quality checks (Ruff, Basedpyright, Pre-commit, Complexipy)
uv run poe code-quality
```
