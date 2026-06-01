# Architecture

`swig2pyi` is structured as a decoupled compiler pipeline with strict architectural layers. We use [Tach](https://github.com/gauge-sh/tach) to declare and enforce boundaries between these modules, ensuring a linear, downward dependency graph with zero circular imports.

---

## The Compilation Pipeline

```mermaid
graph TD
    subgraph CLI Layer [1. CLI Layer]
        swig2pyi.main[main.py] --> swig2pyi.cli[cli.py]
    end

    subgraph API Layer [2. API Layer]
        swig2pyi.cli --> swig2pyi.api[api.py]
    end

    subgraph Core Generator Layer [3. Core Generator Layer]
        swig2pyi.api --> swig2pyi.core.emitter[emitter.py]
        swig2pyi.api --> swig2pyi.core.qa[qa.py]
    end

    subgraph Core Type Mapping Layer [4. Core Type Mapping Layer]
        swig2pyi.core.emitter --> swig2pyi.core.signature[signature.py]
        swig2pyi.core.emitter --> swig2pyi.core.type_system[type_system.py]
        swig2pyi.core.signature --> swig2pyi.core.type_system
        swig2pyi.core.signature --> swig2pyi.core.naming[naming.py]
        swig2pyi.core.emitter --> swig2pyi.core.naming
    end

    subgraph Core Parser Layer [5. Core Parser Layer]
        swig2pyi.api --> swig2pyi.core.parser[parser.py]
        swig2pyi.api --> swig2pyi.core.runner[runner.py]
        swig2pyi.api --> swig2pyi.core.config[config.py]
        swig2pyi.core.parser --> swig2pyi.core.ast_models[ast_models.py]
        swig2pyi.core.emitter --> swig2pyi.core.ast_models
        swig2pyi.core.signature --> swig2pyi.core.ast_models
        swig2pyi.core.type_system --> swig2pyi.core.config
        swig2pyi.core.qa --> swig2pyi.core.config
    end
```

---

## Architectural Layers

The architecture of `swig2pyi` is divided into five logical tiers:

### 1. CLI Layer
* **Modules:** `main`, `cli`
* **Role:** Parses command-line flags, configures logs, sets up exceptions, and handles exit codes.
* **Constraints:** Must only depend on the public `api` layer. It is mathematically forbidden from importing from the `core` modules directly.

### 2. API Layer
* **Modules:** `api`
* **Role:** Orchestrates the high-level generation pipeline (e.g. `generate_from_interface`, `generate_from_xml`), wraps temporary XML generation, and exposes public API entrypoints.
* **Constraints:** Acts as the gateway between the CLI interface and compiler implementation.

### 3. Core Generator Layer
* **Modules:** `core.emitter`, `core.qa`
* **Role:**
    * **Emitter:** Traverses the parsed C++ AST representations and prints formatted Python type stub strings.
    * **QA:** Invokes external formatting/validation tools (like Ruff and Pyright) against stub outputs.
* **Constraints:** Depends on the semantic types layer to resolve individual types and parameters.

### 4. Core Type Mapping Layer
* **Modules:** `core.type_system`, `core.signature`, `core.naming`
* **Role:**
    * **Type System:** Translates C++ symbols, typedefs, smart pointers, and templates into clean Python PEP 484 type hints.
    * **Signature:** Formats function/method parameter lists, properties, and overloaded signatures.
    * **Naming:** Resolves operator remappings (like `operator==` to `__eq__`) and sanitizes Python keywords.
* **Constraints:** Depends on lower-level parser modules for base AST and configs.

### 5. Core Parser Layer
* **Modules:** `core.parser`, `core.runner`, `core.config`, `core.ast_models`
* **Role:**
    * **Parser:** Stream-parses massive SWIG XML inputs using `iterparse` into strongly typed AST elements.
    * **Runner:** Invokes the local SWIG compiler via subprocess, producing XML output. Stateless with no caching layer.
    * **Config / AST:** Defines base rules schema and target types.
* **Constraints:** Completely decoupled from generator and type resolution systems (leaf layer).
