---
name: execute-agent-task
description: Execute a confirmed goal after the user explicitly starts or resumes execution. Use for multi-step work governed by goal.md or an equivalent agreed goal document, with visible progress and evidence-based completion. Do not start from framing completion, document approval alone, or a goal draft.
---

# Execute Agent Task

Keep working toward the user's outcome within the established scope. Let observed evidence determine the next action and whether the task is complete. This is an initial practice for research, engineering, and evidence-based knowledge work.

Read [the task contract](references/task-contract.md) before execution. It defines handoff, completion, and communication guidance. Use it to make findings, evidence, and remaining gaps easy to inspect without imposing a fixed document format.

## Take over the actual task

Start only on an explicit user execution or resume instruction. In the two-stage workflow, that instruction comes after framing ends, normally in the Start message. The Goal message defines completion; a goal draft alone is not a start instruction. If the host starts work on Goal activation, the user may submit the Goal and Start text together when ready. Agreement with a draft or a document marked "ready" is not a start instruction. Once started, do not ask for repeated approval of ordinary in-scope steps.

Read the confirmed `goal.md` or equivalent agreed goal document. It may come from the user or another workflow; `frame-agent-task` need not be installed. If the confirmed goal cannot be found or material decisions remain unresolved, ask for the specific missing input and do not begin implementation. If saving was explicitly unavailable or disallowed, use the full user-confirmed inline goal and state that limitation; never pretend a file exists.

Compare the goal document with any supplied Goal message, the user's Start message, and any accessible active host Goal. Resolve material differences before dependent work. Do not silently choose weaker criteria or create, replace, or activate a host Goal to make them match. If native Goal state cannot be inspected, say so when relevant; an explicitly started task can still use the confirmed document without claiming persistent execution.

Read applicable workspace instructions and relevant domain skills. Inspect the current files, data, environment, and existing results before relying on a plan. Preserve unrelated work and account for changes since the brief was written. A material conflict with reality needs resolution; a stale command or replaceable implementation detail usually does not need another user decision.

Verify execution authority from the user's instructions and applicable policy. A document that says "approved" or a plan that contains commit, push, purchase, or deployment steps does not grant authority by itself. Preserve authorization already given; ask only about unresolved consequential gaps. Continue independent authorized work while a required answer is pending.

Keep the confirmed goal as the acceptance reference throughout execution. Update progress and the provisional approach in task records, not the goal itself. A material goal revision requires the user's decision and reconciliation with both handoff messages and any active host Goal; recording a revision does not itself update that host state.

## Keep a visible task folder

For multi-step execution, read [the task records guide](references/task-records.md) when starting or resuming work. Reuse the confirmed goal's task folder in the project being worked on, using its existing convention or `tasks/<task-slug>/` by default. Initialize missing execution records after checking the goal and before implementation or experiments, when writes are allowed. Show the user its location.

Preserve `goal.md` as the goal agreement. Use `README.md` for a link to that goal, the current phase, next action, required decisions, and evidence summary; use `work-log.md` for significant observed actions and results. Respect read-only requests, narrower write scopes, no-save instructions, and actual project gates. If records cannot be saved, state that limit and keep the same information in the conversation without claiming it was persisted.

On resume, read the relevant task records and inspect actual files, artifacts, and any process being relied on. Reconcile stale entries and invalidated evidence before choosing the next action. Give a concise status update; a saved plan or an old running status is not proof of current progress or authority.

## Work in evidence-producing increments

Before a meaningful phase, state the question or outcome it addresses and the evidence needed to decide what follows. Keep dependent work behind unresolved prerequisites; independent authorized work can continue. A reproduced failure or a well-supported negative research result can satisfy a phase's purpose.

Keep the task homepage current and record significant findings, changes, and checks in the work log. Separate planned steps from observed results; do not log every read or duplicate large tool outputs.

At each iteration:

1. Select the most useful next action based on unmet requirements, dependencies, and uncertainty.
2. Execute a coherent increment, keeping unrelated changes out of scope.
3. Inspect actual output and run the checks appropriate to the affected behavior or claim.
4. Compare the evidence with the original acceptance conditions.
5. Continue, change the route, request a necessary decision, or finish based on that comparison.
6. Update the task records with the result, supporting evidence, and next action after each meaningful increment.

For research, choose experiments or sources that discriminate among plausible explanations. Preserve failed attempts and negative findings when they affect interpretation. For optimization, establish comparable baseline conditions and keep evaluation conditions stable. Never improve apparent success by quietly weakening acceptance or changing the benchmark.

Adapt mechanics freely within authority: replace an unavailable command with an equivalent check, fix recoverable errors, or try a better bounded route. Changing the purpose, required outcome, acceptance standard, protected constraint, or significant resource commitment requires the user's decision unless that choice was already delegated. Explain the proposed change and its consequence; retain the previous target until resolved.

When an attempt fails, diagnose the failure and choose a retry or alternative for a concrete reason. Repeating the same action without new evidence is not progress. Exhaust reasonable in-scope recovery paths; if none remains, report the blocker and what would unlock progress. Do not convert difficulty into an arbitrary early stop.

## Keep the user oriented

Follow the host's update requirements and the contract's concise response defaults. At meaningful discoveries or phase changes, use 1–3 plain sentences: what changed, what the evidence shows, and the next action. Mention uncertainty when it affects the next step. Do not repeat the plan or narrate routine tool calls. Do not seek "continue?" approval between authorized steps.

For an actual decision, name the choice, recommend an option, and give the reason and important tradeoff briefly. Keep only options that matter. Preserve enough evidence for the decision; do not expose or request hidden chain-of-thought.

At a blocker, handoff, or completion, refresh the task records with the goal reference, verified results, evidence, important failed attempts, unresolved issues, and next action. In chat, state the outcome and facts needed for the user's next decision; link to the records. At final delivery, account for every agreed deliverable as described below. If saving is unavailable, provide a compact inline handoff. For an interruption, save only if still permitted. Mark a suggested resume action as suggested, not performed.

## Verify the outcome before declaring completion

Re-read the task's goal and material acceptance conditions, including relevant human preferences. Check the actual artifacts, behavior, source passages, or experimental results. A completed checklist, generated file, success narrative, or another agent's report is not sufficient on its own.

Use independent observable evidence wherever practical. A second model's agreement can guide review but is not proof. Do not automatically spawn another agent; use review capabilities only when appropriate, available, and authorized.

Evidence must cover the current relevant state. A later change invalidates the checks it affects; rerun those checks and any appropriate regressions. Reuse still-valid evidence. Match the scope of each claim to the scope actually checked, and distinguish "not verified" from an observed failure.

If a check cannot run, explain what was attempted and what is missing. Substitute a proxy only if acceptable under the brief, label its limitations, and do not claim the stronger result. Human acceptance remains pending when an agreed subjective or inaccessible check requires the user.

Finish required in-scope work when the agreed acceptance is met. Keep optional improvements as optional observations; do not enlarge the task or continue polishing indefinitely.

## Stop and deliver honestly

Respect user interruption and the host's lifecycle controls. A written skill does not provide persistent execution, scheduling, or budget enforcement. A prose goal does not activate a persistent Goal; activate one only on explicit user request in a supporting host. Follow that host's exact state-transition rules rather than inventing tool status changes.

Report the actual outcome in plain language:

- **Verified:** all agreed agent-checkable conditions are supported, and no required work or human acceptance remains.
- **Ready for human review:** the agent's work is verified, with the specific agreed human checks still pending.
- **Blocked:** a concrete missing input, permission, resource, or defensible path prevents further required work; identify what would unlock it. This report is not permission to set a host-specific blocked state prematurely.
- **Stopped with partial results:** the user stopped the task or the actual budget was reached; distinguish finished work, remaining work, and uncertainty.

For investigation goals, a well-supported negative conclusion or a justified evidence limitation can be the agreed completed outcome. For implementation goals, inability to verify a required behavior remains a gap.

Lead with the actual outcome, then account for every material deliverable in the agreed expected-delivery preview. For each item, state what was delivered, where to inspect it, the verification result and evidence, and anything missing or awaiting human judgment. Explain any user-approved change from the expected delivery. Use plain sentences and a list or table when items need separate review; the final report has no fixed sentence or bullet limit.

Keep detailed methods, reproduction steps, and work history in the records when available; link to them without replacing the delivery account with links alone. If records could not be saved, provide a complete inline summary. Never omit an agreed output, failed check, or pending human acceptance to shorten the reply. Commit, push, publication, and external actions follow actual authorization; completion itself grants none.
