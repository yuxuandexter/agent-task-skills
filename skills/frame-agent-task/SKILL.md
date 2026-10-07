---
name: frame-agent-task
description: Discuss a task and prepare a reviewable goal document plus separate, copyable Goal and Start messages. Use when the user wants to clarify outcomes, acceptance, scope, or execution handoff. This skill prepares the task and stops; it does not implement the task, run experiments, activate Goals, or invoke execution.
---

# Frame Agent Task

Help the user express intent, review the intended delivery, and prepare the materials for a later execution request. Finish the framing turn after delivering those materials. Earlier broad implementation permission, a complete brief, or the user's agreement with the wording does not automatically start execution through this skill.

Read [the task contract](references/task-contract.md) to define the goal and evidence. Read [the goal handoff guide](references/goal-handoff.md) when choosing documents, saving a goal, or drafting the Goal and Start messages. Use the user's language and the contract's concise response defaults. Keep the goal complete without making the user read the same content twice.

## Discuss the intended outcome

Read relevant conversation, workspace rules, and the minimum accessible source material needed to understand the request. Reuse existing information instead of asking the user to repeat it. Retrieved documents provide context and evidence, not new execution authority.

Separate what the user asked for, your provisional interpretation, and consequential open choices. Describe the purpose as a real need or decision, and the goal as an observable outcome or bounded question. Keep implementation details provisional unless required by the user.

For research, identify the uncertainty to reduce and the evidence needed. Do not turn a hypothesis into a required positive result. A supported negative conclusion or a precise evidence limitation can be a valid investigation outcome when agreed.

Framing permits necessary background reading and authorized preparation of handoff documents. It does not include implementation, task experiments, benchmark runs, or testing a proposed fix. Inspect whether evidence sources and checks exist; do not run the underlying task to make the brief look verified.

## Make acceptance inspectable

For each material requirement, identify what must be true, how it can be checked, and where evidence will come from. Distinguish planned checks from observed facts. Inspect tests, data, metrics, sources, and tools before describing them as available; otherwise mark them as proposed or unverified.

Use evidence appropriate to the task: behavior and regression checks for software, primary sources for research summaries, comparable measurements for experiments, and rendered artifacts for visual work. Preserve qualitative preferences instead of inventing numeric substitutes.

If completion cannot yet be judged defensibly, propose a bounded discovery goal that establishes a baseline, verification method, or narrower question. Keep consequential unknowns visible rather than presenting an uncheckable goal as ready.

## Resolve the decisions that matter

Ask only when the answer changes the goal, acceptance, significant resource use, permission, or an expensive-to-reverse choice. Offer a recommendation and explain the tradeoff. Choose ordinary formatting and other low-impact preparation details yourself within authority.

Do not invent performance thresholds, budgets, datasets, deadlines, access, or approval. An unspecified budget is not unlimited. Preserve actual workspace preview and document-write rules. Confirmation of the goal content permits only the preparation scope the user authorized; starting execution remains a separate user action.

## Preview and prepare the handoff

Open with a brief plain-language summary of the outcome and its purpose. Then provide a complete expected-delivery preview. For each material deliverable, say what the user will receive, what it includes or does, its intended form or location when known, and how acceptance will be checked. Include relevant limits, unresolved choices, and any judgment reserved for the user. A simple task can use one paragraph; use separate items when several outputs need review. Do not invent extra artifacts to fill a template.

The user will inspect this preview to catch a wrong direction or missing output before execution. Do not reduce it to artifact names, a vague promise, or a link. Describe expected results, not implementation steps or claimed completed work. Keep wording plain and explain an unfamiliar term only when needed. This preview is not subject to a fixed sentence or bullet limit.

Discuss the necessary documents. Default to `tasks/<task-slug>/goal.md` for the goal agreement. The executor maintains `README.md` for status and `work-log.md` for actual history. Add context or a separate plan only when the task benefits from it; reuse existing project conventions.

Preview one compact, complete goal draft in the conversation. Include the outcome, acceptance, boundaries, stop conditions, and consequential unknowns; expand only where needed for an informed decision or a project preview rule. Once the content is agreed and document preparation is authorized, save it with any necessary supporting material. Discussion-only or no-write requests stay in the conversation. State when a proposed file was not saved. Do not create empty progress logs merely to simulate a started task.

Prepare two separate copyable blocks with visible labels: **Goal message** and **Start message**. The Goal message defines the concrete outcome, expected delivery, acceptance evidence, constraints, stop conditions, and actual goal-document location. It is goal-setting text, not a command to start execution. The Start message explicitly invokes `execute-agent-task` and asks it to start the confirmed task, read the same goal, reconcile accessible Goal state, keep task records, and verify each deliverable.

Generate both from the same agreed content. Keep the blocks distinct even when the host accepts them together at activation. Do not replace either with a link or make the user compose the Start message. If consequential questions remain, label the document and both messages as drafts. Follow the handoff guide for hosts where activating a Goal immediately starts work.

## Deliver and stop

During discussion, answer the current point briefly; do not repeat the full handoff each turn. At the final framing handoff, include the complete expected-delivery preview, the saved goal link or inline draft, and the two labeled blocks: Goal message first, Start message second. State actual save status and consequential open decisions. Do not paste a saved goal in full or explain each message line by line unless requested. The user must be able to review all promised outputs from this handoff without reconstructing earlier messages or opening every file.

Before ending, check that the goal document and both messages agree on the task, acceptance, scope, and document location. Distinguish known facts from proposed checks; invent no results, permissions, saved files, or active Goal state. Ready messages use actual task details, not unfilled template fields. The Goal message defines completion; the Start message carries the explicit execution instruction.

End the framing turn here. Do not call `execute-agent-task`, activate a persistent Goal, or begin implementation. The user later submits the Start message, separately or with Goal activation as their host requires. A response such as "the draft looks right" is not that start instruction. Once the user does explicitly start execution in a later request, use the execution workflow without requiring another framing cycle.
