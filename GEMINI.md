# swig2pyi Project Instructions

## Workflow rules

- Commit often.
- Run `uv run poe code-quality` before each commit.

## Workspace Conventions

- **Debugging:** Always create debug scripts, throwaway test files, and temporary outputs in the `.temp/` directory. Do not clutter the root directory or the `tests/` directory with transient diagnostic code.
