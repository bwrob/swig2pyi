# Testing Strategy: SQLModel Parser Refactor

This document outlines the Test-Driven Development (TDD) and Context-Driven Development strategy for refactoring the SWIG XML parser to use `sqlmodel` and an embedded SQLite database.

## 1. Context-Driven Modeling (Schema)
Before touching parsing logic, we will define the domain context (the SQLModel schema).
- **Tests:** `tests/test_schema.py`
- **Goal:** Verify that SQLModel definitions correctly capture the required fields (tag, name, type, kind) and relationships (Node -> Parms, Node -> Enums).
- **TDD Flow:** Write tests that instantiate these models and verify their properties and DB creation. Run tests (they will fail). Implement `src/swig2pyi/core/schema.py`.

## 2. Component Integration: Streaming Parser
Once the schema exists, we test the XML ingestion pipeline.
- **Tests:** `tests/test_parser_stream.py`
- **Goal:** Feed tiny, controlled XML snippets (string or temp file) into the `iterparse` loop and assert that the correct rows are inserted into the SQLite DB.
- **TDD Flow:** Write tests for parsing a `<class>` with a `<cdecl>`. Assert the DB has two rows linked by `parent_id`. Implement `_stream_to_db`.

## 3. Component Integration: AST Rebuilder
After the DB is populated, we must extract the AST.
- **Tests:** `tests/test_parser_ast.py`
- **Goal:** Pre-populate a test SQLite DB with `sqlmodel` instances. Call `_build_ast_from_db`. Assert the resulting Pydantic AST matches expectations.
- **TDD Flow:** Create test fixtures for DB state. Write tests asserting the AST hierarchy. Implement `_build_ast_from_db`.

## 4. End-to-End Validation
- **Tests:** `tests/test_integration_quantlib_mini.py`, existing `tests/test_parser_*.py`.
- **Goal:** Ensure the full pipeline (Runner -> Parser -> Emitter) continues to produce exact `.pyi` stubs.
