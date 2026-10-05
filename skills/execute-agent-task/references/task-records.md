# Visible task records

Use task records to let the user inspect work and let a later session resume from evidence. They are operational records, not a task scheduler or a substitute for verification.

## Choose the location

Use the project being worked on, not the installed Skill directory. Follow any existing task-record convention. If none exists and writes are permitted, use `tasks/<task-slug>/` with `goal.md`, `README.md`, and `work-log.md`. Reuse the folder containing the confirmed goal; do not create a competing goal. Choose a descriptive English kebab-case slug when a new location is needed, without requiring the user to name it. Report the path.

Inspect an existing folder before reusing it. Resume the same task there; choose a distinct slug for different work. Preserve user edits and unrelated records. Reuse existing `plan.md` / `track.md` or equivalent files instead of creating duplicate records. Recordkeeping does not expand an explicit file allowlist, override a no-save request, or bypass a project preview gate. If saving is unavailable, explain the limitation and keep a concise equivalent in the conversation.

## Goal document: the agreed target

Framing or the user prepares `goal.md` before execution. Read it at startup and preserve its outcome, acceptance, boundaries, and important context during ordinary progress updates. An equivalent existing project document can serve the same role; do not duplicate its requirements in several files.

The homepage links to the goal and identifies its agreed revision when available. If the user approves a material revision, record the decision and changed reference, then reconcile the Goal message and any host Goal before continuing affected work. Do not silently edit the goal to fit observed results. A ready label does not start execution.

An explicit start with an unavailable confirmed goal requires resolving that missing input. When saving is explicitly disallowed or unavailable, preserve the user-confirmed inline goal and state which records remain in the conversation. Do not fabricate saved documents or native Goal state.

## Task homepage: the current view

Keep `README.md` short enough to scan. It links to the goal document and shows the current state, not a second goal specification or full event history. Use the user's language. Include the current phase, next action, required user decisions, and an evidence summary mapped to the goal's acceptance conditions.

Put the status and last-updated timestamp near the top. Distinguish in progress, waiting for a decision, blocked, ready for human review, verified, and stopped with partial results as applicable. These are recorded observations, not host lifecycle commands or proof that a process is alive. Use actual time with timezone when available; never fabricate a timestamp or completion percentage.

A starting shape to adapt:

```markdown
# Task title

Status: In progress
Last updated: Actual timestamp with timezone
Current phase: The question or outcome being worked on
Next action: The next useful action and what it will establish
User decision: None, or the specific unresolved decision

## Goal reference
The confirmed goal document location and agreed revision when available.
Use that document for the outcome, acceptance, and boundaries.

## Approach and evidence
The few meaningful phases and their continuation conditions.
Separate planned checks, observed results, and remaining gaps.
Link to relevant artifacts and the work log.
```

Do not predetermine every step of exploratory work. Refresh the approach when evidence changes the route; preserve the goal and acceptance unless a change is authorized. If a user edit materially changes the task or conflicts with current instructions, resolve that specific conflict before dependent work.

## Work log: what actually happened

Add an entry after a meaningful increment: a material change, experiment, check, finding, or decision. Record a startup entry after inspection. Keep chronological entries with timestamps, preserving relevant earlier outcomes and noting what later results supersede. Correct inaccurate or sensitive entries appropriately; do not preserve an error merely to claim an immutable ledger.

Each entry should give the action and reason, relevant commands or method, observed result, evidence location, and consequence for the next step. Include working directory, inputs, version, or environment details only when they affect reproduction. Never include secrets; indicate required credentials by name without their values. Link large logs or artifacts instead of copying them into the page. Mark suggested commands as not yet run and flag side effects before suggesting reruns.

Before costly or hard-to-reverse changes, record a recovery method and its limits. Preserve pre-existing edits. Do not offer whole-file restoration or recursive directory deletion as a generic rollback. Record a scoped patch, known task-owned artifact, backup, or other recovery basis when needed; disclose if complete reversal is unavailable. Writing a recovery command never authorizes executing it.

## Keep the view trustworthy

Update the homepage and work log after meaningful increments, at phase changes or blockers, before a long operation when the user needs to know what is being attempted, and at handoff or completion. An interrupted process may leave stale records; do not continue work against a stop instruction just to update a log.

On resume, read the confirmed goal, homepage, and relevant recent entries; reconcile any accessible host Goal, then inspect the actual files, artifacts, and any process being relied on. Reuse valid evidence and recheck affected claims. Reconcile stale status and report the current phase and next action briefly before proceeding.

At completion, refresh the homepage with actual outcome, evidence, remaining human checks, and any limitations. Give the user its path. These files provide visibility while the agent works; they do not create a heartbeat, background watcher, or automatic notification system.
