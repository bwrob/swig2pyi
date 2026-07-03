---
description: Rules and conventions for writing, debugging, and running tests.
trigger: glob
glob: tests/**/*
---

# Testing Rules

## 1. Directory and Diagnostic Hygiene
* **No Clutter:** Do not add diagnostic scripts, logs, temporary outputs, or throwaway scripts to `tests/` or the project root.
* **Sandbox Location:** Always place transient diagnostic code, test scripts, and temporary inputs/outputs in the `.temp/` directory.

## 2. Test Development and Coverage
* **Test-Driven Fixes (TDD):** Every fix for a type-checking or parsing error must be accompanied by a small unit test or a verified regression assertion in the generated QuantLib tests.
* **90%+ Coverage:** Ensure test coverage meets or exceeds 90% when running coverage tools (`uv run poe coverage`).

## 3. Execution and Committing
* **Pre-Commit Verification:** Run `uv run poe code-quality` to check styling, format, typing, and complexity before committing any test additions or changes.
