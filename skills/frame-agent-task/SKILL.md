---
name: frame-agent-task
description: Discuss a task and prepare a reviewable goal document plus a copyable Goal message. Use when the user wants to clarify outcomes, acceptance, scope, or execution handoff. This skill prepares the task and stops; it does not implement the task, run experiments, activate Goals, or invoke execution.
---

# Frame Agent Task

Help the user express intent, review the intended delivery, and prepare the materials for a later execution request. Finish the framing turn after delivering those materials. Earlier broad implementation permission, a complete brief, or the user's agreement with the wording does not automatically start execution through this skill.

Read [the task contract](references/task-contract.md) to define the goal and evidence. Read [the goal handoff guide](references/goal-handoff.md) when choosing documents, saving a goal, or drafting the Goal message. Use the user's language and scale the brief to the task.

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

Lead with a concise preview of what the eventual execution will deliver, what it helps the user decide or do, and the evidence they can inspect. A short paragraph or a few bullets is enough. Describe the intended result, not a list of implementation steps. Keep it separate from the framing deliverables and from work already completed.

Discuss the necessary documents. Default to `tasks/<task-slug>/goal.md` for the goal agreement. The executor maintains `README.md` for status and `work-log.md` for actual history. Add context or a separate plan only when the task benefits from it; reuse existing project conventions.

Preview goal content in the conversation. Once the content is agreed and document preparation is authorized, save the agreed goal and any necessary supporting material. Discussion-only or no-write requests stay in the conversation. If saving is unavailable, return the full draft and proposed location, and state that no file was saved. Do not create empty progress logs merely to simulate a started task.

Prepare a copyable Goal message that explicitly invokes `execute-agent-task` and includes the concrete outcome, core evidence, key constraints, and the actual goal-document location when saved. Keep that explicit skill instruction in ordinary execution messages as well as native Goal messages. Generate it from the same agreed content. If consequential questions remain, label the document and message as draft rather than ready to launch.

## Deliver and stop

Return the concise delivery preview, the goal document or draft, a list of necessary handoff files and their actual save status, the Goal message, and any unresolved decision. Avoid duplicating the full brief in each item.

Before ending, check that the documents and message preserve the user's intent, agree on acceptance and scope, distinguish known facts from proposed checks, and contain no invented results or permissions. A ready Goal message must contain the task's actual outcome and criteria, not unfilled template fields.

End the framing turn here. Do not call `execute-agent-task`, activate a persistent Goal, or begin implementation. The user later submits an explicit execution instruction, possibly as part of activating their Goal. A response such as "the draft looks right" is not that start instruction. Once the user does explicitly start execution in a later request, use the execution workflow without requiring another framing cycle.
