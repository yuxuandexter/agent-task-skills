# Cache comparison notes

The user operates a local inference prototype and is deciding whether caching deserves more development effort.

Known context:

- Available saved workloads are named `repeated-prefix` and `mostly-unique`.
- Response quality must remain unchanged. Latency and peak memory both matter.
- The user has not selected a performance threshold or acceptable memory tradeoff.
- No benchmark has been run for this proposal. These notes are context, not results.
- There is no production deployment in this task.

Candidate idea: compare cache-on and cache-off using the same inputs and evaluation conditions. Cache may help one workload while harming the other. The first useful output is an evidence plan and any decision needed from the user.
