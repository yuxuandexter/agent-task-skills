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

## Return two messages

At the final handoff, return two separately labeled, copyable blocks in this order. Use short, plain sentences and actual agreed details. Do not merge them or merely tell the user to write a start prompt.

### Goal message — define the goal

Give the outcome, expected delivery, core acceptance evidence, important boundaries, stop conditions, and goal-document location. Keep it about what completion means; do not include an immediate start command or an execute-skill invocation. A path alone is not a completion condition.

Pattern:

```text
Desired outcome and delivery: [specific outcome and material deliverables].
Completion requires: [core checks and evidence].
Constraints and stop conditions: [actual boundaries, limits, and decisions requiring user input].
Agreed goal: [actual accessible goal document location].
```

### Start message — begin execution

Explicitly select `execute-agent-task` and start the concrete task against the same confirmed goal. Include the actual goal path or accessible reference so the executor can find it without guessing. Do not invent a claim that a native Goal has already been set.

Pattern:

```text
Use execute-agent-task to start [concrete task] now.
Read the confirmed goal at [actual accessible goal document location].
Compare it with any supplied Goal message and accessible active host Goal; resolve material conflicts before dependent work.
Work within the agreed boundaries and keep progress and evidence in [actual task record location].
Verify and report each agreed deliverable, with evidence and remaining gaps.
```

The Start message carries the execution instruction; it need not repeat the full goal. For another agent or session, make sure the goal and skill are accessible. If no file was saved because saving was unavailable or disallowed, state that fact, supply the complete goal inline, and make clear that the user must include that confirmed text with the Start message. Never present an unsaved path as an existing file.

Replace all pattern fields in ready messages. Omit irrelevant clauses instead of inventing budgets, permissions, or files. If consequential choices remain, label the goal and both messages as drafts and name the unresolved decision. Do not present a draft Start message as ready to use.

Keep the goal document and both messages consistent after material revisions. Regenerate affected text; do not quietly change acceptance to resolve a conflict.

## Leave submission and activation to the user

Framing ends after preparing the handoff. Do not submit either message, create a Goal, or execute the Start message while drafting it.

When the host supports saving a goal without starting work, the user can set the Goal with the first message and later send the Start message. For a host without persistent Goals, the confirmed goal and Start message can guide an ordinary task without promising persistent continuation.

Some hosts start work as soon as a Goal is activated. In Codex `/goal`, the goal text can be both the first prompt and the completion criteria. Explain this briefly when relevant; two text blocks do not create a runtime pause. Use a supported non-running setup state only if it actually exists. Otherwise, advise keeping both messages as drafts until ready, then supplying the Goal and Start text together at activation. Still return the two distinct blocks, and do not imply the Goal message alone will wait for a later Start message.
