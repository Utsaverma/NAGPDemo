# AI in SDLC Workshop — Sample Repo

One repo that carries every live demo across all three workshop
sessions (30 Sep, 6 Oct, 14 Oct 2026). Stack matches a typical Python
+ Angular shop: FastAPI, Angular 17+ front end, pytest tests, and GitHub
Actions CI.

## Setup

**Backend**
```
cd backend
python -m venv .venv
source .venv/bin/activate  # Windows PowerShell: .venv\Scripts\Activate.ps1
pip install -r requirements.txt
pytest                 # TestOrderTotalCalculator.test_applies_discount_once fails on purpose - see Session 1, Demo 1
uvicorn app.main:app --reload --port 5000  # http://localhost:5000, Swagger UI at /swagger
```

**Frontend** — see `frontend/README.md` (ship source files only, not a
generated Angular CLI scaffold, so it doesn't drift out of date).

**Everything else** (Jira, Mermaid MCP, Playwright MCP, Spec Kit,
OpenSpec, BMAD) needs its own one-time setup in your tools — this repo
supplies the content each demo reads, not the tool installs themselves.

## Facilitator quick start

You do not need to run every demo. Pick the 2–4 rows that match the
conversation you want to have, open only the listed files, and use the
smallest prompt in the map below. The desired outcome is an understandable
decision, finding, or working change — not a long autonomous coding session.

For code-changing demos, work on a throwaway branch or reset the demo change
afterwards. Several files intentionally contain a bug, an incomplete TODO, or
an insecure example; those are teaching material, not regressions to fix in
the baseline.

## Demo map and minimum showcase

| # | Demo | Minimum effort | What a good 3–5 minute showcase proves | Files / setup |
|---|------|----------------|------------------------------------------|---------------|
| 1 | One task, two agents | Run `pytest tests/test_order_total.py -q`. Give one agent the failing test and another `OrderTotalCalculator`; ask both to diagnose the failure. | Both agents trace the `SAVE10` issue to the running-total discount and propose a one-time subtotal discount. | `backend/app/services.py`, `backend/tests/test_order_total.py` |
| 2 | Messy inputs → requirements summary | Add the three input files to chat and ask: `Summarize the agreed requirements, open questions, and conflicts. Cite the source for each conflict.` | A concise requirements summary that notices the $500/$1,000 conflict and the notification/partial-approval uncertainty. | `demo-assets/session1/demo2-inputs/` |
| 3 | AI-drafted user stories | Reuse Demo 2's summary and ask: `Draft three implementation-ready user stories with acceptance criteria. Mark assumptions.` | Stories separate bulk approval, partial approval, audit trail, and the two-person threshold instead of hiding decisions. | Demo 2 output |
| 4 | Jira MCP: stories into the backlog | Seed the supplied epic in a Jira sandbox. Ask the agent to read it and create the three stories from Demo 3 under that epic. | The audience sees grounded backlog creation rather than manually copying tickets. | Jira MCP + `demo-assets/session1/demo4-jira/epic-PROJ-101.md` |
| 5 | Agentic feature build: CSV download | Ask: `Implement the existing CSV-export TODO, add focused tests, and show the download from the invoices page.` | A bounded end-to-end feature: route, Angular service/button, tests, and a downloadable CSV. | Running API + `backend/app/routers/invoices.py`, `frontend/src/app/invoices/` |
| 6 | Skills and hooks | Point the agent at `AGENTS.md`, then ask for a small change such as `Add a health endpoint following this repo's conventions.` | The agent reads local instructions and follows routing, dependency, and test conventions without repeated prompting. | `AGENTS.md` |
| 7 | Subagents and MCP together | Seed PROJ-142 in Jira. Give one subagent the ticket/test and another the implementation; ask a reviewer to compare their conclusions. | Parallel work stays coordinated around a real ticket and the same acceptance criteria. | Jira MCP + `demo-assets/session1/demo7-jira/ticket-PROJ-142.md` |
| 8 | Spec Kit: bulk invoice approval | Ask Spec Kit to produce a spec for `POST /api/approvals/bulk-approve`; do not implement it during the short demo. | A feature request becomes explicit request/response contracts, edge cases, and testable acceptance criteria. | Spec Kit + `backend/app/routers/approvals.py` |
| 9 | OpenSpec: partial approval | Give OpenSpec the current-flow document and ask for a change proposal for partial approval. | The proposal identifies model, status, API, UI, and migration implications before code changes begin. | OpenSpec + `demo-assets/session2/demo9-openspec/current-approval-flow.md` |
| 10 | BMAD: persona agents | Ask product, architecture, and QA personas to review the bulk/partial-approval proposal and reconcile differences. | Different roles expose trade-offs: scope, state transitions, auditability, and test coverage. | BMAD + outputs from Demos 8–9 |
| 11 | Automated PR review | Follow the staging steps in its README, then ask: `Review this change for correctness, concurrency, performance, tests, and naming.` | The review finds the five intentionally planted issues with useful locations and severity. | `demo-assets/session2/demo11-pr-review/` |
| 12 | AI security analysis | Paste only the intentionally vulnerable Python sample and ask for an OWASP-oriented review. Do not run or import it. | The agent identifies SQL injection, the hardcoded credential, and missing authorization. | `demo-assets/session2/demo12-security/` |
| 13 | Generated tests and edge cases | Ask: `Before writing tests, enumerate boundary, invalid-input, rounding, and stacking cases for DiscountCalculator.` | A test plan catches the three documented quirks instead of merely generating happy-path tests. | `backend/app/services.py` (`DiscountCalculator`) |
| 14 | Playwright MCP | Start the API and Angular shell. Ask Playwright to open invoices, approve one pending item as `demo.approver`, and verify it leaves the pending list. | Browser automation verifies a user-visible workflow against seeded data. | Running app + `backend/app/repositories.py` |
| 15 | Architecture diagrams | Ask Mermaid MCP: `Read backend/app and draw the request flow from Angular through routes, services, and the in-memory repository.` | A diagram is generated from the real implementation, making component boundaries easy to discuss. | Mermaid MCP + `backend/app/` |
| 16 | Architecture decision record | Ask: `Use this template to decide how approval notifications should be delivered. Compare the listed options and recommend one.` | The agent documents a decision and consequences instead of jumping directly to implementation. | `demo-assets/session3/demo16-adr/adr-template.md` |
| 17 | Log analysis and root cause | Provide the logs and deploy diff; ask: `Build a timeline, identify the most likely root cause, and propose safe next actions.` | It connects the release timing, connection-pool exhaustion, and changed DB limits. | `demo-assets/session3/demo17-rca/` |
| 18 | CI pipeline optimization | Provide workflow and timings; ask for a faster dependency graph while keeping both security scans before e2e/merge. | The response isolates the serial bottleneck, missing dependency cache, and safe parallelization opportunities. | `.github/workflows/ci.yml`, `demo-assets/session3/demo18-pipeline/` |
| 19 | Incident response, human in the loop | Provide the alert, logs, diff, and runbook; ask for an incident update plus remediation options that need approval. | The agent triages and recommends, but does not execute a rollback or config change on its own. | `demo-assets/session3/demo19-incident/` + Demo 17 inputs |
| 20 | Quality gates and a tiny eval | Give a PR-review prompt the five JSON eval cases. Record pass/fail before and after changing the prompt. | A repeatable eval catches whether improvements preserve SQLi, secret, null, and N+1 detection without flagging clean code. | `.github/workflows/ci.yml`, `demo-assets/session3/demo20-eval/review-skill-eval-cases.json` |

## Prep only for the demos you will run

- **For code/API demos (1, 5, 7, 8, 13–15):** install backend dependencies
  and start the API using the commands above. Demo 14 also needs an Angular
  shell as described in `frontend/README.md`.
- **For Jira demos (4, 7):** seed only the supplied epic/ticket in a sandbox.
- **For tool-specific demos (4, 8–10, 14–15):** install and test just the MCP
  server or framework you plan to show; their command names can change.
- **For review/security demos (11–12):** stage the review branch only when you
  are ready, and never execute or wire in the security sample.
- **For resilience demos (16–20):** no running app is required; open the
  listed synthetic inputs and keep the prompt focused on the stated outcome.
- Rehearse the few demos you selected once. Keep a saved transcript or short
  recording as a fallback for external-tool or network failures.

## Safety notes

- `demo-assets/session2/demo12-security/` is intentionally vulnerable
  code. It is not referenced anywhere in `backend/app/main.py`. Never deploy
  this repo's `demo-assets/` folder, and never point a real database
  connection string at anything in it.
- Nothing in `demo-assets/` is real customer, employee, or financial
  data — all names, tickets, and figures are synthetic.
