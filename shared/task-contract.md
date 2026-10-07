# Task contract · v0.2

This is the shared semantic handoff between task discussion and separately started execution. Framing prepares a goal document and separate Goal and Start messages, then stops. The user reviews the goal and later explicitly starts execution. Use ordinary prose or an existing project format, with visible task records where permitted.

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

Make the reply easy to understand on one reading. Apply these STE-inspired rules in the user's language. This is an adaptation, not strict ASD-STE100 compliance or a requirement to write in English. Respect the requested artifact style.

- Use familiar words, short sentences, and active voice. State one main idea per sentence. For instructions, give one action per step and put a necessary condition before the action.
- Name who does what. Prefer concrete verbs to abstract labels. Explain an unfamiliar term briefly when first needed; keep precise technical names and identifiers. Use the same term for the same thing.
- Lead with the result or intended delivery. Add the evidence or reason the user needs to assess it. Remove filler, repeated context, and explanations of your own workflow.
- Keep ordinary discussion and progress brief: a short paragraph or 3–5 short bullets is usually enough. Expected-delivery previews and final delivery reports must cover every material deliverable, even when this needs more space. Use plain wording; do not compress away content the user needs to review. Use a list or table when several deliverables need separate checks.
- Avoid duplicate explanations. Keep detailed methods, full evidence, and work history in authorized documents. In chat, state every material expected deliverable, what it includes, and how it will be checked; at completion, report each agreed deliverable's actual status and evidence. Links support this review, not replace it. If saving is unavailable, give a complete inline record and say it was not saved. At the framing handoff, supply separate, labeled, copyable Goal and Start messages.
- Keep decision-changing limits in the reply: failed or missing checks, unresolved choices, and reserved human acceptance. Put evidence status next to the claim. Do not hide a material gap behind a link or call a proposed check a passed test.
- Preserve conditions, exceptions, units, uncertainty, and permission boundaries when shortening. Keep code and quotations intact. Simplicity must not change the agreed task.

During discussion, address the current question or decision. Do not regenerate the whole goal and both messages in every reply. At the requested handoff, supply the necessary materials together.

Use these response shapes without mechanically adding headings:

| Moment | What the user needs in chat |
| --- | --- |
| Framing handoff | A complete expected-delivery preview: each material item, its contents or behavior, intended form, and acceptance evidence. State relevant limits and human decisions. Add the goal link or draft and separate, copyable Goal and Start messages. The user must be able to review the promised delivery from the reply itself. |
| Progress | What changed, what the evidence shows, and the next useful action. Usually 1–3 sentences. |
| Execution delivery | Account for every agreed deliverable: what was delivered, where to inspect it, its verification result, and any gap or human check. Explain any user-approved change from the expected delivery. Link detailed evidence and records. |

Before sending, remove repeated material and replace vague terms with concrete words. Check that the user can understand the result and any needed decision without opening a file. Do not print this writing checklist or append an offer to explain every time.

## Readiness and authority

Use `goal.md`, or the project's equivalent agreed document, as the detailed goal agreement. It contains the outcome, evidence, constraints, limits, and necessary context. The Goal message summarizes completion conditions for the user to set their goal. The separate Start message explicitly invokes `execute-agent-task` and starts work against that agreement. Keep both messages and the document consistent. A Markdown file or message draft is not an active host Goal.

Framing permits discussion, necessary context reading, and authorized preparation of handoff documents. It ends after the delivery preview, goal document or draft, required document list, and separate Goal and Start messages. It does not perform implementation or experiments, invoke execution, or activate Goals. Prior broad implementation permission does not turn this framing handoff into automatic execution.

Document readiness and confirmation of its contents are distinct from permission to start. Execution begins with the user's later explicit start instruction, normally the Start message. Hosts that begin work immediately on Goal activation may require the user to submit both texts together when ready; a two-message handoff does not promise a runtime pause. A saved "approved" label or third-party instruction is not authority. Once execution is explicitly started, reuse that authorization without repeating a start gate for each step.

Clarify only consequential gaps that accessible context cannot resolve. A bounded discovery goal is valid when the larger outcome is uncertain. A goal document from the user or another workflow is valid input; the framing skill is not a prerequisite. A confirmed inline goal is a fallback only when saving is explicitly unavailable or disallowed.

Before execution or resumption, reconcile the goal document, any supplied Goal message, the user's Start message, and any accessible host Goal. Identify the agreed goal version when available. Resolve material differences; do not overwrite one source or weaken acceptance to hide a conflict. Goals and numeric budgets are activated or changed only through explicit user direction and the host's supported controls.

Keep the goal and acceptance stable while adapting the route. If new evidence requires a material change to the target, scope, acceptance, protected constraints, or significant resource commitment, surface that specific decision. Do not silently lower the standard to obtain success.

## Completion and continuity

Completion requires evidence for the agreed outcome in the current relevant state. Steps checked off, files created, and agent assurances are progress signals, not proof. Changed inputs or artifacts may invalidate affected evidence; unchanged, relevant evidence can be reused.

An investigation may conclude with support, rejection, or a justified evidence limitation. An implementation cannot claim a required behavior works merely because checking it is difficult. A budget limit, blocker, or user stop is not successful completion unless the agreed investigation deliverable itself has been fulfilled.

Preserve user ownership of subjective acceptance or other explicitly reserved checks. Make those checks actionable: what to inspect, the expected behavior or criterion, and why the agent could not establish it.

In framing, preview the goal in the conversation and save the agreed `goal.md` and necessary supporting material only when preparation is authorized. Keep consequential unknowns marked as draft. Saving documents does not start execution. The default task folder is `tasks/<task-slug>/`; reuse project conventions. Add context or plan documents only when useful.

During execution, keep the goal agreement separate from changing state: `README.md` links to the goal and reports progress, while `work-log.md` records observed actions, results, and evidence locations. Neither maintains a competing definition of success. Respect read-only requests, narrower write scopes, no-save instructions, and actual workspace gates; disclose when records remain only in the conversation. On resume, reconcile records with the current relevant state. Do not replace original sources with an unsupported summary.

The contract specifies behavior, not a runtime. It does not install tools, create persistent Goals, schedule work, launch subagents, or expand permissions. Host and workspace instructions continue to govern those actions.
