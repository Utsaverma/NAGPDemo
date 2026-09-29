# AI in SDLC Workshop — Sample Repo

One repo that carries every live demo across all three workshop
sessions (30 Sep, 6 Oct, 14 Oct 2026). Stack matches a typical .NET/C#
+ Angular shop: ASP.NET Core 8 Web API, Angular 17+ front end, xUnit
tests, GitHub Actions CI.

## Setup

**Backend**
```
cd backend
dotnet restore
dotnet build
dotnet test        # OrderTotalTests.AppliesDiscountOnce fails on purpose - see Session 1, Demo 1
cd src/InvoiceApp.Api
dotnet run          # http://localhost:5000, Swagger at /swagger
```

**Frontend** — see `frontend/README.md` (ship source files only, not a
generated Angular CLI scaffold, so it doesn't drift out of date).

**Everything else** (Jira, Mermaid MCP, Playwright MCP, Spec Kit,
OpenSpec, BMAD) needs its own one-time setup in your tools — this repo
supplies the content each demo reads, not the tool installs themselves.

## Demo map

| # | Demo | Session | Files |
|---|------|---------|-------|
| 1 | One task, two agents | 1 | `backend/src/InvoiceApp.Domain/OrderTotalCalculator.cs`, `backend/tests/InvoiceApp.Tests/OrderTotalTests.cs` |
| 2 | Messy inputs → requirements summary | 1 | `demo-assets/session1/demo2-inputs/` (3 files, 2 planted conflicts) |
| 3 | AI-drafted user stories | 1 | Reuses Demo 2's output — no separate file |
| 4 | Jira MCP: stories into the backlog | 1 | `demo-assets/session1/demo4-jira/epic-PROJ-101.md` (seed into your Jira sandbox) |
| 5 | Agentic feature build: CSV download | 1 | `backend/src/InvoiceApp.Api/Controllers/InvoicesController.cs`, `frontend/src/app/invoices/` |
| 6 | Skills and hooks | 1 | `AGENTS.md` (conventions the skill should follow) |
| 7 | Subagents and MCP together | 1 | `demo-assets/session1/demo7-jira/ticket-PROJ-142.md`, same bug as Demo 1 |
| 8 | Spec Kit: bulk invoice approval | 2 | `backend/src/InvoiceApp.Api/Controllers/ApprovalsController.cs` (extend here) |
| 9 | OpenSpec: partial approval | 2 | `demo-assets/session2/demo9-openspec/current-approval-flow.md` |
| 10 | BMAD: persona agents | 2 | Same feature idea as Demos 8–9 — no separate file |
| 11 | Automated PR review | 2 | `demo-assets/session2/demo11-pr-review/` (5 planted issues + setup steps) |
| 12 | AI security analysis | 2 | `demo-assets/session2/demo12-security/` (SQLi, hardcoded secret, missing authz — never wire into `Program.cs`) |
| 13 | Generated tests and edge cases | 2 | `backend/src/InvoiceApp.Domain/DiscountCalculator.cs` (untested on purpose) |
| 14 | Playwright MCP | 2 | Running app: seeded invoices in `InMemoryInvoiceRepository.cs`, login as `demo.approver` |
| 15 | Architecture diagrams (Mermaid MCP) | 3 | Whole `backend/` — the agent reads the real code |
| 16 | Architecture decision record | 3 | `demo-assets/session3/demo16-adr/adr-template.md` |
| 17 | Log analysis and root cause | 3 | `demo-assets/session3/demo17-rca/` (logs + deploy diff) |
| 18 | CI pipeline optimization | 3 | `.github/workflows/ci.yml`, `demo-assets/session3/demo18-pipeline/timings.csv` |
| 19 | Incident response, human in the loop | 3 | `demo-assets/session3/demo19-incident/` (runbook + mock alert) |
| 20 | Quality gates and a tiny eval | 3 | `.github/workflows/ci.yml` (`lint` stage fails on purpose), `demo-assets/session3/demo20-eval/review-skill-eval-cases.json` |

## Before you present, once

- `dotnet test` locally so you've seen the Demo 1 failure yourself.
- Seed the two Jira items (Demos 4 and 7) in your sandbox.
- Set up MCP servers you plan to use: Jira, Mermaid, Playwright.
- Install Spec Kit / OpenSpec / BMAD in a clean checkout and confirm
  current command names — these projects move fast.
- Stage the Demo 11 PR branch (`demo-assets/session2/demo11-pr-review/README.md`
  has the steps) and the Demo 12 security snippet ahead of time.
- Rehearse each demo once end to end; keep a saved transcript or short
  recording as a fallback in case of network or API issues during the
  live session.

## Safety notes

- `demo-assets/session2/demo12-security/` is intentionally vulnerable
  code. It is not referenced anywhere in `Program.cs`. Never deploy
  this repo's `demo-assets/` folder, and never point a real database
  connection string at anything in it.
- Nothing in `demo-assets/` is real customer, employee, or financial
  data — all names, tickets, and figures are synthetic.
