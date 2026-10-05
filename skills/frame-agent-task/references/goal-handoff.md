# Prepare a goal handoff

Use the task contract for semantic requirements. This guide defines the materials to leave for the user and a later executor. Preparing or saving a goal is not activation of a host Goal.

## Choose only useful documents

Use the target project's existing convention, or `tasks/<task-slug>/goal.md`. Keep the agreed outcome, acceptance, boundaries, and important context in this goal document. A short, complete goal is preferable to a large spec. Label draft goals honestly; a readiness label never grants execution authority.

The executor creates or updates `README.md` for current progress and `work-log.md` for observed history. These records link to the goal instead of maintaining duplicate acceptance definitions. A separate `context.md` is useful for substantial background; a `plan.md` is useful for a complex approach. Neither is mandatory.

Before writing, verify actual preparation authorization and workspace rules. A user who has already agreed to the content and asked for handoff files need not approve ordinary filenames again. Preserve existing files and user edits. If only discussion is authorized, show the draft in chat without creating a task folder.

## Goal document shape

Use the smallest complete form in the user's language. A short task can use these bullets rather than a section for every field:

```markdown
# Task title

- Purpose: The need or decision this work serves.
- Goal: The observable outcome.
- Expected delivery: Each material item, what it contains or does, and its intended form or location when known.
- Acceptance: What must be true, how to check it, and evidence sources.
- Scope: Allowed changes, protected behavior, and authority limits.
- Stop: Actual resource limits, completion, and required user decisions.
- Context: Necessary sources, assumptions, and consequential open questions.
```

Connect each expected deliverable to its acceptance checks and evidence. Distinguish inspected facts from planned checks and reserved human checks. Expand a field or add a table when several items need separate review. Keep all material criteria. The final framing reply must also explain all material expected outputs; a document link alone is not a delivery preview.

Reuse known answers. Do not add numeric thresholds or budgets just to fill a section. Keep implementation steps tentative; the executor can develop and revise the approach within the agreed target. Identify the agreed revision when available so a later executor can detect a material change.

## Generate the Goal message

Prepare the message at the requested handoff, not in every discussion reply. Return one compact, copyable block. Use short sentences; do not explain each line or repeat the full goal around it. Begin by explicitly selecting `execute-agent-task`, whether the user will submit a native Goal or an ordinary execution prompt. Summarize the core outcome, verification surface, essential constraints, and goal location. It must make sense beyond "finish the file": a path alone is not an auditable completion condition.

A pattern to fill with the actual agreed details:

```text
Use execute-agent-task to deliver [specific outcome].
The agreed task is in [actual goal document location].
Completion requires [core checks and evidence], while preserving [key constraints].
Work within [actual boundaries and relevant limits].
Keep progress and evidence in the task records.
If a material change to the goal, acceptance, or boundaries is needed, raise that decision first.
```

For a ready message, replace all pattern fields with real content; omit unneeded clauses instead of inventing values. If the document has not been saved, provide the goal text inline or label the proposed path as unsaved. If key decisions remain, label the message as draft and identify those decisions.

The goal document is the detailed agreement; the message is its launch summary. Regenerate the message after material goal revisions. Never silently change either one to resolve a disagreement between them.

## Leave activation to the user

Do not submit the message, create a Goal, or execute its instructions during framing. Explain that the user sends it later when ready to start. For Codex, activating `/goal` can start work immediately because its text is also the first prompt. Include the execute skill instruction in that submitted message; do not promise that an active Goal will wait for a separate follow-up.

If the user uses a host that separates saved goal settings from starting work, provide a separate execution prompt as requested. For hosts without persistent Goals, the same confirmed document and explicit execution prompt can guide a normal task, but do not claim persistent continuation. The user controls when execution starts in every case.
