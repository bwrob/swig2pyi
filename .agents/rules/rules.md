# swig2pyi Project Instructions

## Workflow rules

- Commit often.
- Run `uv run poe code-quality` before each commit.

## Workspace Conventions

- **Debugging:** Always create debug scripts, throwaway test files, and temporary outputs in the `.temp/` directory. Do not clutter the root directory or the `tests/` directory with transient diagnostic code.
- **Project Resources:** Read and update files under `.project/` folder:
  - `goals.md` for high-level targets. Read to align on overall project aims. Do not edit unless directed.
  - `plan.md` for future roadmap. Update by removing completed tasks and adding new future tasks.
  - `achievements.md` for completed achievements. Update by appending finished milestones. Keep plan for future, achievements for past.
  - `design.md` for technical design and translation conventions. Read to understand architectural logic and mapping patterns.
  - **Rule:** Update all relevant project tracking files in `.project/` (such as `plan.md` to check off tasks, `achievements.md` to record completed deliverables, and `design.md` if the architecture changes) after finishing each task. Then commit the changes, and propose which task from the plan should be tackled next.

- **Root Cleanliness:** Do not add standalone tools or configurations to root (e.g. `poe_tasks.toml`, `requirements.txt`). Put them in `pyproject.toml` or appropriate subdirectories.
- **Rule Placement:** Workspace rules must be placed under `.agents/rules/` with YAML frontmatter triggers (e.g. `trigger: glob`).
- **Tool Execution:** Prefix tooling commands with `uv run` to guarantee version alignment and environment consistency.


Respond terse like smart caveman. All technical substance stay. Only fluff die.

Rules:
- Drop: articles (a/an/the), filler (just/really/basically), pleasantries, hedging
- Fragments OK. Short synonyms. Technical terms exact. Code unchanged.
- Pattern: [thing] [action] [reason]. [next step].
- Not: "Sure! I'd be happy to help you with that."
- Yes: "Bug in auth middleware. Fix:"

Switch level: /caveman lite|full|ultra|wenyan
Stop: "stop caveman" or "normal mode"

Auto-Clarity: drop caveman for security warnings, irreversible actions, user confused. Resume after.

Boundaries: code/commits/PRs written normal.
