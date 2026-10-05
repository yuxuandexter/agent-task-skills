# Fix completed latency summary

## Purpose
Make the summary report the mean latency of successful requests without contamination from other request states.

## Goal and delivery
Fix `mean_completed_latency(rows)` in `latency_summary.py`, add relevant regression coverage, and provide the observed verification results. Keep the work local.

## Acceptance and evidence
- Only rows whose `status` is exactly `ok` contribute to the average. A mixed-status regression must include non-ok rows with durations so the check detects contamination.
- Empty input or input with no successful rows raises `ValueError`.
- Preserve the public function name, signature, and correct all-successful-input behavior.
- Run the relevant Python unit tests after the change and report actual results. Tests do not establish performance improvements.
- Preserve `user-notes.txt` and this goal document byte for byte.

## Scope and boundaries
Allowed changes: `latency_summary.py`, related tests, and this task folder's execution records. No commit, push, deployment, external service access, or persistent Goal activation.

## Resources and stop conditions
Use local inspection and tests. No numeric budget was specified. Finish when the conditions above have evidence; raise any necessary material change to the goal or boundaries first.

## Agreement
This is the confirmed target supplied with the isolated execution trial. The trial user's separate start instruction authorizes execution; this label alone does not.
