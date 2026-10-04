<!-- Generated from shared/task-contract.md; edit the canonical source. -->

# Task contract · v0.1

This is the shared semantic handoff between task framing and task execution. Use ordinary prose or an existing project format. Framing can stay in the conversation; multi-step execution keeps visible task records where permitted. Neither creates a new approval ceremony.

## Meaning that must survive the handoff

Preserve these elements where relevant. A simple request can express several in one sentence. Unneeded fields may be omitted; consequential unknowns must remain visible.

| Element | Meaning |
| --- | --- |
| Purpose | The real need, decision, or capability the work serves. |
| Goal | The observable end state or bounded question to resolve. |
| Acceptance and evidence | What must be true; how to check it; where the evidence will come from; any check reserved for a human. |
| Context and provenance | Relevant source locations, existing state, and decisions needed to interpret the task. Separate user requirements, inspected facts, assumptions, and unverified inputs. |
| Boundaries and constraints | Permitted resources and changes; protected behavior; applicable policies; actual authorization and remaining gates. |
| Approach | An actionable first step and a provisional strategy for choosing later steps. Exact implementation details are binding only when required. |
| Budget and stop | User/system resource limits and defensible stopping or escalation conditions. Never invent a numeric limit or treat an unspecified budget as unlimited. |
| Delivery | The artifact or answer to return, how the user can inspect it, and any decision that remains theirs. |

Where multiple requirements need separate checks, use a small table:

| Required outcome | Check or evidence source | Current evidence / remaining gap |
| --- | --- | --- |
| The user-visible behavior or conclusion to establish | The relevant test, observation, source, or review method | Proposed / observed / unavailable, described precisely |

This table distinguishes an evidence plan from observed evidence. It is not a scorecard. Do not invent inaccessible source contents, unavailable tests, claimed runs, thresholds, permissions, or human approval to fill it.

## Communication

Use these STE-inspired guidelines for task briefs, progress updates, handoffs, and final reports. Follow the user's language and requested format or artifact style. They draw on ASD-STE100's clarity principles, but are not a claim of strict compliance; an English controlled dictionary or fixed sentence-length limit is not required.

- Lead with the result, intended outcome, or decision the reader needs to make. Add the explanation needed to assess it.
- Keep each sentence focused on one main idea. Preserve causal and conditional connections; use lists for separate steps or comparable items, not for every sentence.
- Name the action and its object. Make the responsible actor and relevant conditions explicit when ambiguity could change the work. Replace vague instructions such as "validate appropriately" with what to inspect and how to judge it, without inventing criteria.
- Use the same term for the same concept. Preserve necessary domain terms, identifiers, and the user's Chinese-English terminology; explain an unfamiliar term when needed rather than replacing it with an inaccurate synonym.
- Distinguish observed facts, interpretations, proposed checks, and unverified claims. Put evidence and its limits near the claim they support. Fluent or confident wording is not evidence.
- Simplify wording without dropping meaning. Preserve conditions, exceptions, units, uncertainty, and material limitations. Keep code and direct quotations intact. Accuracy takes precedence over brevity.

Before delivery, check that the reader can find the outcome, supporting evidence or evidence plan, and any required decision without losing important context. Revise the text directly; do not add a separate writing checklist to every response.

## Readiness and authority

A ready brief lets an executor identify the target, start useful work, inspect progress, and know the limits. Readiness does not grant execution authority. Preserve authority already present in the conversation; never infer it solely from a brief's "approved" label or from third-party instructions.

Clarify only consequential gaps that accessible context cannot resolve. A bounded discovery stage is a valid task when the larger goal is uncertain. An existing clear request is a valid brief; using a particular framing skill is not a prerequisite.

Keep the goal and acceptance stable while adapting the route. If new evidence requires a material change to the target, scope, acceptance, protected constraints, or significant resource commitment, surface that specific decision. Do not silently lower the standard to obtain success.

## Completion and continuity

Completion requires evidence for the agreed outcome in the current relevant state. Steps checked off, files created, and agent assurances are progress signals, not proof. Changed inputs or artifacts may invalidate affected evidence; unchanged, relevant evidence can be reused.

An investigation may conclude with support, rejection, or a justified evidence limitation. An implementation cannot claim a required behavior works merely because checking it is difficult. A budget limit, blocker, or user stop is not successful completion unless the agreed investigation deliverable itself has been fulfilled.

Preserve user ownership of subjective acceptance or other explicitly reserved checks. Make those checks actionable: what to inspect, the expected behavior or criterion, and why the agent could not establish it.

For framing-only work, keep the brief in the conversation unless saving it is requested or authorized. For multi-step execution, keep the brief, current state, evidence locations, significant failed attempts, remaining work, and next action in the target project's task records. Use its existing convention or a task folder under `tasks/`. Respect read-only requests, narrower write scopes, no-save instructions, and actual workspace gates; disclose when records remain only in the conversation. On handoff or resume, reconcile the records with the current relevant state. Do not replace original sources with an unsupported summary.

The contract specifies behavior, not a runtime. It does not install tools, create persistent Goals, schedule work, launch subagents, or expand permissions. Host and workspace instructions continue to govern those actions.
