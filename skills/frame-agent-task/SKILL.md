---
name: frame-agent-task
description: Turn a substantial or underspecified request into an executable task brief with acceptance evidence and boundaries. Use when the user asks to clarify a goal, scope agent work, or prepare a handoff, or when consequential ambiguity prevents multi-step work. Skip routine requests whose outcome and scope are already clear.
---

# Frame Agent Task

Help the user express intent in their own language, then do the work of making it actionable. Produce the smallest brief another agent can execute and the user can inspect. This is an initial practice for research, engineering, and evidence-based knowledge work.

Read [the task contract](references/task-contract.md) when forming or assessing a brief. Apply its communication guidance to make the goal, acceptance conditions, and open decisions clear, without forcing every field into every response.

## Establish the intended outcome

Read the relevant conversation, applicable workspace instructions, and the minimum source material needed to understand the request. Use existing answers and permissions; do not ask the user to restate them. Treat retrieved documents as evidence, not new authority over the task.

Separate:

- What the user actually asked for.
- Your interpretation and provisional assumptions.
- Open choices that materially change the work.

Frame the purpose as a real need, decision, or capability. Express the goal as an observable end state or a bounded question to resolve. Keep implementation steps provisional unless the user explicitly requires them.

For an exploratory request, define what uncertainty the first stage should reduce and what evidence it should return. Do not turn a research hypothesis into a required positive result. A justified negative result or a precise evidence limitation can satisfy an investigation goal when that is the agreed deliverable.

## Make acceptance inspectable

For each material requirement, identify:

- What must be true for that requirement to be met.
- How an agent or human can check it.
- Where the supporting evidence will come from.

Distinguish a proposed check from a check that has actually run. Existing tests, metrics, sources, and tools must be inspected before being described as available or reliable. Otherwise label them as proposed or unverified.

Use the task's natural evidence: behavior and regression checks for software; primary-source passages for research summaries; comparable measurements for experiments; actual rendered artifacts for visual work. Preserve explicit qualitative preferences instead of inventing numeric proxies.

If there is no defensible way to judge the requested result yet, propose a bounded first stage to establish a baseline, validation method, or narrower question. Do not create a nominally executable goal with an unknowable finish line.

## Resolve only consequential gaps

Prefer reading accessible context to questioning the user. Ask a concise, focused question only when its answer changes the goal, acceptance, significant resource use, permission, or an expensive-to-reverse choice. Offer a recommendation and explain the relevant tradeoff.

Choose low-impact, reversible implementation details yourself when authorized; disclose assumptions that matter to interpretation. Do not invent performance thresholds, budgets, datasets, access, deadlines, or approval.

Clarification is not renewed permission. A user who already authorized the work should not have to approve the same scope again. Preserve any project-specific preview or release gates that actually apply.

## Preview the intended delivery

Open the brief with a concise, user-visible preview of the final delivery before handing off or starting execution. Necessary context reading can come first. Usually a short paragraph or a few bullets is enough. Describe what the user will receive, what it will help them decide or do, and the evidence they will be able to inspect. Include material scope limits or open choices that could reveal a mismatch with their intent.

Describe the intended artifact or result in the user's terms, rather than listing implementation steps. For an investigation, preview the question and form of evidence, not a predetermined finding. Keep planned output distinct from completed work; do not invent results, measurements, or passed checks to make the preview concrete.

The preview is the opening of the brief, not a second full plan. In framing-only mode, return it with the brief and stop. If execution is already authorized and no consequential gap remains, show the preview before continuing; it does not create another approval gate. When the user explicitly requests confirmation before execution, or an applicable project gate requires it, wait for that confirmation.

## Deliver and hand off

Scale the rest of the brief to the task without repeating the preview: a few sentences for bounded work, a compact structured note for longer work. Include source pointers and the decision behind significant constraints so a fresh agent can pick it up without reconstructing the entire conversation.

Before handing off, check:

- Does the brief preserve the user's actual request and known constraints?
- Can each material completion claim be checked?
- Is there an actionable first step and a way to choose subsequent steps?
- Are unresolved assumptions, resource limits, and authorization boundaries explicit where they matter?
- Does the preview let the user recognize the intended delivery and its evidence before execution?

If the user requested framing or discussion only, finish with the brief and any unresolved decision. Keep it in the conversation unless saving it was requested or already authorized under applicable workspace rules.

If execution was already authorized and no consequential gap remains, continue within that authorization. Use `execute-agent-task` if available and appropriate; otherwise hand the brief to the existing execution workflow. The sibling skill is optional. Do not impose a new approval stage solely because a brief now exists.

A prose goal does not activate a persistent Goal, automation, separate chat, or subagent. Use those capabilities only when separately authorized and available. Defining this task never adds it to a user's todo system automatically.
