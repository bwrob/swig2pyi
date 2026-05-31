---
name: task-scheduler
description: Use when the user requests to add, plan, or schedule a new task for the project. Ensures tasks are added with consistent formatting to `.project/plan.md` and guides the agent on what questions to ask and clarify before scheduling.
---

# Task Scheduler — Project Roadmapping Discipline

Use this skill when adding new tasks to the project's roadmap in `.project/plan.md`. It enforces consistent formatting and defines the clarification questions to ask the user.

---

## 1. Questions to Ask and Clarify

Before scheduling any task, you MUST interview the user to clarify the following technical details:

1. **Component Scope:**
   * *Question:* "Which component does this task target (e.g. `parser`, `emitter`, `type_system`, `naming`, `runner`, or packaging)?"
   * *Purpose:* Ensures the task is categorized under a clear, modular boundary.

2. **Success & Verification Criteria:**
   * *Question:* "How will we verify completion? What specific tests should pass, and what strict checks (e.g. `basedpyright`, complexity limits, code-quality) apply?"
   * *Purpose:* Align with Andrej Karpathy's goal-driven execution principle.

3. **Generalization & Assumptions:**
   * *Question:* "Does this task introduce or touch any library-specific assumptions (such as QuantLib or GDAL/OSR-specific rules)? Should it be configurable?"
   * *Purpose:* Keeps `swig2pyi` as a generic, reusable library wrapper.

4. **Roadmap Categorization:**
   * *Question:* "Should this task be placed in Active Tasks (Working On), Future Tasks (Next Steps), or Package Release & Quality Tasks?"

5. **Task Prioritization:**
   * *Question:* "What is the priority level (High, Medium, Low) for this task?"
   * *Purpose:* Focuses resources on high-impact milestones first.

---

## 2. Formatting Standards

All tasks added to `.project/plan.md` must strictly follow this format:

```markdown
- [ ] **[Component / Category]: [Task Title] [Priority: High|Medium|Low]:** [Task Details explaining the goal, scope, and expected outcome].
  * **Acceptance Criteria:**
    - [ ] [Criterion 1]
    - [ ] [Criterion 2]
```

### Examples:
* **Correct:**
  ```markdown
  - [ ] **Component G: Explicit Import Tracking [Priority: High]:** Track required imports dynamically in `StubEmitter` and `TypeManager` during stub generation, removing the heuristic post-emission regex scans.
    * **Acceptance Criteria:**
      - [ ] Importer checks are executed dynamically during AST traversal.
      - [ ] All post-emission regex scans are deleted.
  ```
* **Incorrect:** `- [ ] Fix imports in emitter`

---

## 3. Workflow for Adding Tasks

1. **Clarify details** using the questions in Section 1.
2. **Draft the task entry** according to the formatting standards in Section 2.
3. **Present the drafted entry** to the user for confirmation.
4. **Append the task** to the correct section of [.project/plan.md](file:///.project/plan.md).
5. **Run validation** using `uv run poe code-quality` before staging/committing the updated file.
