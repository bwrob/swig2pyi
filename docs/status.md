# Project Status - Swig2Pyi Refactor

**Date:** May 18, 2026
**Status:** In Progress - Architecture Refactoring. Transitioning to SQLModel/SQLite for XML parsing to resolve memory exhaustion and complex AST resolution issues.

## Achievements

### 1. Proof of Concept Complete
The core concept of generating Python stubs from SWIG XML is validated. Previous in-memory AST approaches successfully mapped basic QuantLib patterns.

### 2. Temporary SQLite Parser Trialed
A raw SQLite SAX streaming parser was prototyped and verified to reduce RAM usage and allow relational querying for C++ templates and inheritance tracking.

## Current Focus: SQLModel Architecture

We are currently rewriting the parser layer to use `sqlmodel`. This solves the memory constraints of `pydantic-xml` while retaining type-safe models for AST traversal.

## Roadmap

This roadmap outlines the prioritized steps for further development.

1.  **Refactoring (Current):**
    *   Design the `sqlmodel` schema.
    *   Implement SAX streamer to populate the DB.
    *   Write queries to rebuild the AST for the `StubEmitter`.

2.  **Enhancements (Next):**
    *   **Docstrings:** Extract and emit docstrings from SWIG comments into the `.pyi` files for improved code clarity.
    *   **Properties:** Detect and correctly emit public member variables as properties in the generated stubs.

3.  **Refinement:**
    *   Ensure all small unit tests pass against the new parser.
    *   Address `ruff` warnings in generated code (e.g. unused TypeVars) to ensure clean validation runs.