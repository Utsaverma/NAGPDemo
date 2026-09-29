# CI optimization demo (Session 3, Demo 18)

`timings.csv` is "the last 10 run timings" referenced in the demo
prompt. Give the agent this file plus `.github/workflows/ci.yml` (at
the repo root) and ask it to find slow/redundant stages.

What a good answer should surface, roughly in order of impact:
- `unit_and_integration_tests` is the single biggest stage (~200s) and
  bundles two different kinds of tests that could run in parallel or be
  split by speed.
- Every stage runs serially via `needs:`, even ones with no real
  dependency on each other (e.g. `lint` doesn't need to wait for tests
  to finish).
- No caching for NuGet restore, so `restore` pays the same cost every
  run.
- `e2e` is the slowest single stage (~220s) and currently blocks on
  every gate before it, including the two security stages.

The constraint to give the agent: `security-scan` and `secret-scan`
must both still run before `e2e`/merge - they cannot be dropped or made
optional to hit a faster number.
