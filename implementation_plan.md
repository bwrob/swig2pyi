# Implementation Plan: Focused Synthetic Tests & PyPI Packaging Readiness

This plan introduces focused synthetic test cases targeting operator mapping, vector/typedef sequence parameter relaxation, and handle method delegation overloads, alongside packaging preparation for PyPI publishing.

## User Review Required

> [!IMPORTANT]
> The test cases will use lightweight, isolated `.i` files in `tests/data/synthetic/` to ensure fast execution (<1s total for all new tests) and clean isolation of edge cases.
> Packaging changes include configuring setuptools build backend and specifying rules JSON files as package-data.

## Proposed Changes

### Component A: Operator Remapping Tests
We will verify that C++ operators map to Python dunder methods.

#### [NEW] [operators.i](file:///home/bwrob/dev/swig2pyi/tests/data/synthetic/operators.i)
A SWIG interface exposing a class `OpClass` with operators:
* `operator==`, `operator!=`
* `operator<`, `operator<=`, `operator>`, `operator>=`
* `operator()`
* `operator[]` (read and write)
* `operator+`, `operator-`, `operator*`, `operator/`
* `operator+=`

#### [NEW] [operators.json](file:///home/bwrob/dev/swig2pyi/tests/data/synthetic/operators.json)
JSON config for operators test.

#### [NEW] [test_integration_operators.py](file:///home/bwrob/dev/swig2pyi/tests/test_integration_operators.py)
Integration test checking that stubs contain correct Python dunder signatures (`__eq__`, `__ne__`, `__lt__`, `__le__`, `__gt__`, `__ge__`, `__call__`, `__getitem__`, `__setitem__`, `__add__`, `__sub__`, `__mul__`, `__truediv__`, `__iadd__`).

---

### Component B: Vector and Typedef Parameter Relaxation Tests
We will verify standard list methods and constructors are added to vector types, and parameter types allow Sequence conversions.

#### [NEW] [vector_typedefs.i](file:///home/bwrob/dev/swig2pyi/tests/data/synthetic/vector_typedefs.i)
A SWIG interface exposing:
* `std::vector<double>` and a typedef `RealVector`
* A class `Maths` with a method taking `RealVector` and `std::vector<std::vector<double>>` (matrix)
* A method returning `RealVector`

#### [NEW] [vector_typedefs.json](file:///home/bwrob/dev/swig2pyi/tests/data/synthetic/vector_typedefs.json)
JSON config for vector/typedef test.

#### [NEW] [test_integration_vectors.py](file:///home/bwrob/dev/swig2pyi/tests/test_integration_vectors.py)
Integration test verifying:
* `RealVector` constructor overloads (`Iterable`, `size`, `size, value`) and standard methods (`push_back`, `resize`, `size`, `empty`, `clear`).
* Parameter types allow `Union[RealVector, Sequence[float]]`.

---

### Component C: Handle Method Overloads Delegation Tests [COMPLETED]
We have verified that handle proxy classes delegate all overloaded methods from the underlying class.

#### [NEW] [handle_overloads.i](file:///home/bwrob/dev/swig2pyi/tests/data/synthetic/handle_overloads.i)
A SWIG interface exposing:
* Class `Underlying` with overloaded methods `foo(int)` and `foo(std::string)`.
* Template `Handle<T>` proxy class delegating to `Underlying`.
* Instantiation `UnderlyingHandle` using `%template`.

#### [NEW] [handle_overloads.json](file:///home/bwrob/dev/swig2pyi/tests/data/synthetic/handle_overloads.json)
JSON config for handle overloads test.

#### [NEW] [test_integration_handle_overloads.py](file:///home/bwrob/dev/swig2pyi/tests/test_integration_handle_overloads.py)
Integration test verifying that `UnderlyingHandle` contains both overloaded signatures of `foo`.

---

### Component D: Clean up and Packaging Preparation (PyPI Readiness)
Configure the package metadata and package data to include configuration JSON files in the build.

#### [MODIFY] [pyproject.toml](file:///home/bwrob/dev/swig2pyi/pyproject.toml)
* Define a standard setuptools build backend.
* Explicitly configure package data to include `src/swig2pyi/rules/*.json` in the built distribution wheel.

---

### Component E: Thermonuclear Code Quality Review
We will install the thermonuclear code review skill and execute an architectural review on the core package logic.

#### [NEW] [SKILL.md](file:///home/bwrob/dev/swig2pyi/.agents/skills/thermonuclear/SKILL.md)
* Define the strict, adversarial code quality audit skill.

#### [RUN] Architectural Review
* Execute the thermonuclear code quality review skill on `src/swig2pyi/core/` to audit abstraction quality, look for simplification opportunities ("code judo"), and identify potential refactorings.

---

## Verification Plan

### Automated Tests
* Run lightweight tests:
  ```bash
  uv run poe test
  ```
* Run test coverage:
  ```bash
  uv run poe coverage
  ```
* Run code quality checks:
  ```bash
  uv run poe code-quality
  ```

### Manual Verification
* Run `uv build` and inspect the generated wheel contents to ensure `swig2pyi/rules/quantlib.json` and `swig2pyi/rules/gdal_osr.json` are packaged.
