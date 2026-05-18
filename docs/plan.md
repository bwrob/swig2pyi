# SQLModel Parsing Architecture Plan

## 1. Problem Statement
The current XML parser reads the entire SWIG XML output into memory and uses a deeply nested object model (`pydantic-xml`). For large libraries like QuantLib, the XML file exceeds 2GB, causing severe memory bloat and making it difficult to resolve relational context (e.g. knowing if a nested function is inside a class template instantiation or an ignored scope).

## 2. The Solution
Implement a **streaming SAX parser** (`xml.etree.ElementTree.iterparse`) that reads the XML lazily and immediately inserts nodes into a **temporary SQLite database** using **`sqlmodel`**.

This provides:
1. **Low Memory Footprint:** Elements are cleared from memory immediately after insertion.
2. **Relational Resolution:** Finding all methods of a class, or all items of an enum, becomes a simple SQL query.
3. **Type Safety:** `sqlmodel` bridges the gap between the declarative models previously used in Pydantic and the relational requirements of SQLite.

## 3. Database Design (SQLModel Schema)

We will define several `SQLModel` entities to represent the SWIG XML nodes:

*   **`Node`**: The base table for major XML tags (`class`, `cdecl`, `template`, `enum`, `constructor`, `destructor`).
    *   `id`: Primary key.
    *   `parent_id`: Foreign key referencing the parent `Node` (e.g. the class this method belongs to).
    *   `tag`: The XML tag (e.g., `'class'`, `'cdecl'`).
    *   `name`: The target language name of the symbol.
    *   `kind`: SWIG kind (`'function'`, `'variable'`, `'class'`, `'struct'`).
    *   `type`: C++ type string (for functions/variables).
    *   `decl`: C++ declaration string.
    *   `feature_ignore`: Boolean flag to skip emitting this node.
*   **`Parm`**: Parameters for constructors and functions (`cdecl`).
    *   `id`: Primary Key.
    *   `node_id`: Foreign key to `Node`.
    *   `name`: Parameter name.
    *   `type`: Parameter type.
    *   `idx`: Order index.
*   **`EnumItem`**: Items within an enumeration.
    *   `id`: Primary Key.
    *   `node_id`: Foreign key to `Node` (where `tag == 'enum'`).
    *   `name`: Item name.
    *   `value`: Enum value.
*   **`BaseClass`**: Inheritance relationships.
    *   `id`: Primary Key.
    *   `node_id`: Foreign key to `Node` (where `tag == 'class'`).
    *   `name`: Base class name.

## 4. Execution Tasks

### Task 1: Environment & Dependencies
- [ ] Remove `pydantic-xml` from `pyproject.toml`.
- [ ] Add `sqlmodel` to `pyproject.toml`.
- [ ] Run `uv sync` to update the environment.

### Task 2: Implement SQLModel Schema (`src/swig2pyi/core/schema.py`)
- [ ] Define `Node`, `Parm`, `EnumItem`, and `BaseClass` as SQLModel classes.
- [ ] Configure the engine creation logic (using an in-memory or temporary file SQLite database).

### Task 3: Implement SAX Streamer (`src/swig2pyi/core/parser.py`)
- [ ] Refactor `SwigXmlParser` to use `iterparse`.
- [ ] Maintain a stack of active `Node` IDs to correctly assign `parent_id`.
- [ ] As `event == 'end'` is encountered, create the appropriate SQLModel instances and `session.add()` them.
- [ ] Call `elem.clear()` to free memory.
- [ ] Call `session.commit()` in batches to maintain performance.

### Task 4: Rebuild AST from DB (`src/swig2pyi/core/parser.py`)
- [ ] Implement `_build_ast_from_db` to execute SQLModel queries.
- [ ] Map the SQLModel objects back into the intermediate representation (`Module`, `Class`, `CDecl`, etc.) expected by the `StubEmitter`.
- [ ] Ensure queries filter out `feature_ignore == True`.
- [ ] Specifically filter `cdecl` elements that are children of uninstantiated `template` tags (handling SWIG's template nesting artifacts).

### Task 5: Testing & Validation
- [ ] Update `tests/test_parser.py` to use the new DB backend.
- [ ] Ensure the full QuantLib integration test passes.
- [ ] Verify that smaller edge-case files (like `RelinkableQuoteHandle` and missing enums) correctly propagate through the SQL queries.
