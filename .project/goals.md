# Top-Level Project Goals

The primary goals for the `swig2pyi` project:

## 1. High-Fidelity Type Stub Generation
* **Target:** Automatically generate accurate, complete, PEP 484 compliant `.pyi` type stubs for complex SWIG-wrapped C++ libraries, with a primary focus on QuantLib.
* **Accuracy:** Resolve C++ templates to Python generics, map operators to dunder methods, relax sequence parameters, and delegate overloads for handle proxy classes.

## 2. High-Performance direct-to-memory XML Pipeline
* **Efficiency:** Parse SWIG XML schemas cleanly and lazily using standard `xml.etree.ElementTree` directly to the Pydantic AST. Bypasses intermediate SQLite database compilation and ORM validation, minimizing memory footprint and CPU overhead.

## 3. Strict Verification & Code Quality
* **Zero Errors:** Validate generated stubs using `basedpyright` in strict mode against target test suites, achieving a complete clean pass.
* **Testing:** Maintain high test coverage (90%+) via pytest and strict code complexity limits (under 10 cyclomatic complexity per function).

## 4. PyPI Package Publishing
* **Release:** Package and distribute `swig2pyi` on PyPI as a presentable, universal command-line utility and library for SWIG developers.
