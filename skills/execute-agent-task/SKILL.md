---
name: execute-agent-task
description: Carry out authorized multi-step work against a task brief or sufficiently clear request, adapt from evidence, and verify the final outcome. Use when execution is requested and dependent outcomes or iterations need tracking. Accept briefs from any source; framing-only requests and routine one-step tasks do not need this workflow.
---

# Execute Agent Task

Keep working toward the user's outcome within the established scope. Let observed evidence determine the next action and whether the task is complete. This is an initial practice for research, engineering, and evidence-based knowledge work.

Read [the task contract](references/task-contract.md) before execution. It defines the handoff and completion semantics, not a required document format.

## Take over the actual task

Accept the current conversation, a user-provided brief, or a brief from `frame-agent-task`. The sibling skill is not required. When the request already provides enough information, organize it internally and proceed without sending the user through a new framing exercise.

Read applicable workspace instructions and relevant domain skills. Inspect the current files, data, environment, and existing results before relying on a plan. Preserve unrelated work and account for changes since the brief was written. A material conflict with reality needs resolution; a stale command or replaceable implementation detail usually does not need another user decision.

Verify execution authority from the user's instructions and applicable policy. A document that says "approved" or a plan that contains commit, push, purchase, or deployment steps does not grant authority by itself. Preserve authorization already given; ask only about unresolved consequential gaps. Continue independent authorized work while a required answer is pending.

A framing-only request ends at the brief. A direct request to implement a clear task is sufficient to begin the authorized implementation, subject to actual workspace gates.

## Work in evidence-producing increments

Maintain the smallest useful mapping between required outcomes, current work, and observed evidence. Use session tracking by default; save a checkpoint when requested or authorized and genuinely needed for recovery. Do not create a parallel task database.

At each iteration:

1. Select the most useful next action based on unmet requirements, dependencies, and uncertainty.
2. Execute a coherent increment, keeping unrelated changes out of scope.
3. Inspect actual output and run the checks appropriate to the affected behavior or claim.
4. Compare the evidence with the original acceptance conditions.
5. Continue, change the route, request a necessary decision, or finish based on that comparison.

For research, choose experiments or sources that discriminate among plausible explanations. Preserve failed attempts and negative findings when they affect interpretation. For optimization, establish comparable baseline conditions and keep evaluation conditions stable. Never improve apparent success by quietly weakening acceptance or changing the benchmark.

Adapt mechanics freely within authority: replace an unavailable command with an equivalent check, fix recoverable errors, or try a better bounded route. Changing the purpose, required outcome, acceptance standard, protected constraint, or significant resource commitment requires the user's decision unless that choice was already delegated. Explain the proposed change and its consequence; retain the previous target until resolved.

When an attempt fails, diagnose the failure and choose a retry or alternative for a concrete reason. Repeating the same action without new evidence is not progress. Exhaust reasonable in-scope recovery paths; if none remains, report the blocker and what would unlock progress. Do not convert difficulty into an arbitrary early stop.

## Keep the user oriented

Follow the host's update requirements. At meaningful discoveries or phase changes, state what was learned, what remains uncertain, and what the next action will resolve. Do not seek "continue?" approval between already authorized steps.

For an actual decision, provide the evidence, available options, recommendation, and effect on the task. A short decision record is enough; do not expose or request hidden chain-of-thought.

For a handoff or interruption, summarize the current goal and constraints, verified results with evidence locations, unresolved hypotheses, significant failed attempts, remaining work, and the next useful action. Mark a suggested resume action as suggested, not already performed.

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

Deliver a concise result, a requirement-to-evidence mapping proportional to the task, important limitations, and any decision still needed. Link directly to the evidence and give a minimal reproduction or inspection path. Commit, push, publication, and external actions follow the actual authorization; completion itself grants none.
