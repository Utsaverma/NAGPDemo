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

## Copilot-only facilitator guide

This is deliberately a **basic GitHub Copilot Chat** workshop. It uses only:

- VS Code with GitHub Copilot Chat;
- the files in this repository;
- a local terminal for the two small Python commands shown above; and
- optionally, a browser to view the local API at `/swagger`.

It does **not** need MCP servers, Jira access, Playwright, subagents, Spec Kit,
OpenSpec, BMAD, a cloud deployment, or a full Angular shell. For every demo,
open the named file(s), attach them to Copilot Chat (or select their contents),
then paste the prompt exactly as written.

### Shared 60-second setup

1. Open this repository in VS Code.
2. Ensure GitHub Copilot Chat is signed in and available.
3. Open a Copilot Chat panel.
4. For Demos 1, 5, and 14, open a terminal in `backend/` and install the Python
   dependencies once using the commands in **Setup** above.
5. For every other demo, no command needs to run. The result is a Copilot
   answer, plan, review, diagram, or draft — not a deployed feature.

### Demo 1 — Fix one small bug with Copilot

**Open:** `backend/tests/test_order_total.py` and `backend/app/services.py`.

1. In `backend/`, run `pytest tests/test_order_total.py -q`.
2. Point out that one test fails and that the failure is intentional.
3. Attach both files to Copilot Chat and paste the prompt below.
4. Review Copilot's explanation before accepting any edit.
5. If you accept the edit, run the same focused test again.

**Prompt to paste:**

```text
The SAVE10 test fails. Read the attached test and OrderTotalCalculator.
Explain the root cause in two sentences. Then propose the smallest code change
that makes SAVE10 apply once to the order subtotal. Do not change the test or
any unrelated behavior.
```

**Show:** Copilot can trace a failure from a test to one small implementation
change. Do not run the full suite; the baseline intentionally contains this
one failing workshop exercise.

### Demo 2 — Turn messy conversation into clear requirements

**Open:** all three files in `demo-assets/session1/demo2-inputs/`.

1. Attach the three files to one Copilot Chat message.
2. Paste the prompt.
3. Read the conflict section aloud before reading the rest of the answer.

**Prompt to paste:**

```text
Read the three attached discovery inputs. Give me a short requirements brief
with these headings: Agreed requirements, Open questions, and Conflicts.
For every conflict, quote the source filename and explain why it conflicts.
Do not decide a conflict for us.
```

**Show:** Copilot summarizes scattered input while keeping uncertainty visible.

### Demo 3 — Draft user stories from the summary

**Open:** the answer from Demo 2 in Copilot Chat.

1. Keep the Demo 2 conversation open.
2. Paste the prompt below.
3. Inspect that every story has acceptance criteria and a stated assumption.

**Prompt to paste:**

```text
Using only the requirements brief above, draft three user stories for the
first release. Each must include a title, user story, acceptance criteria,
non-goals, and assumptions. Keep unresolved conflicts as assumptions rather
than silently choosing a value.
```

**Show:** Copilot converts analysis into work that a team can review.

### Demo 4 — Draft Jira-ready tickets without Jira access

**Open:** `demo-assets/session1/demo4-jira/epic-PROJ-101.md` and the Demo 3
stories.

1. Attach the epic file and copy in the three stories from Demo 3.
2. Paste the prompt.
3. Copy the response into Jira later if you want; do not connect Jira live.

**Prompt to paste:**

```text
Format these three stories as Jira-ready child issues for the attached epic.
For each issue provide: summary, description, acceptance criteria, priority,
and dependencies. Keep the two-person approval threshold at $1,000 and flag
anything still unresolved as an assumption.
```

**Show:** Copilot produces consistent backlog-ready text without needing an
integration.

### Demo 5 — Plan a small feature before writing it

**Open:** `backend/app/routers/invoices.py`,
`frontend/src/app/invoice.service.ts`, and `frontend/src/app/invoices/`.

1. Attach the route, Angular service, and invoice component files.
2. Paste the prompt.
3. Review the file-by-file plan. Stop here for the lightweight demo.
4. Optional: ask Copilot to implement one planned file at a time and review
   each diff before accepting it.

**Prompt to paste:**

```text
The invoice screen has a TODO for CSV download. Do not write code yet.
Give a minimal file-by-file implementation plan that preserves current API
behavior. Include the endpoint shape, CSV columns, Angular change, and focused
tests. Call out any assumptions.
```

**Show:** Copilot scopes a change before editing code. No running frontend is
needed.

### Demo 6 — Use repository instructions as context

**Open:** `AGENTS.md` and `backend/app/routers/invoices.py`.

1. Attach both files.
2. Paste the prompt.
3. Check whether Copilot names the existing route conventions and pytest
   location before suggesting code.

**Prompt to paste:**

```text
Read AGENTS.md first. I want a small GET /health endpoint. Do not edit files.
Tell me exactly which file should contain it, what response it should return,
and which pytest file should verify it. Explain how your plan follows the
repository conventions.
```

**Show:** Good context produces a constrained, consistent answer.

### Demo 7 — Split a task into simple review roles

**Open:** `demo-assets/session1/demo7-jira/ticket-PROJ-142.md`,
`backend/tests/test_order_total.py`, and `backend/app/services.py`.

1. Attach all three files.
2. Paste the prompt.
3. Compare the three short sections in Copilot's answer.

**Prompt to paste:**

```text
Act as three reviewers in one response: QA, implementation engineer, and
code reviewer. Read the attached ticket, test, and calculator. For each role,
give one finding. Then give one agreed minimal fix plan. Do not change code.
```

**Show:** You can get multiple perspectives with one basic Copilot Chat
conversation; no subagents or Jira connection are required.

### Demo 8 — Write a lightweight API specification

**Open:** `backend/app/routers/approvals.py` and the bulk-approval requirements
from Demo 3.

1. Attach the existing route and the relevant story.
2. Paste the prompt.
3. Review the request and response examples together.

**Prompt to paste:**

```text
Draft a one-page API specification for POST /api/approvals/bulk-approve.
Include JSON request and response examples, validation rules, per-invoice
success or failure behavior, and five tests. Do not write implementation code.
```

**Show:** Clear contracts can be produced before implementation without a
special specification tool.

### Demo 9 — Plan a safe change to an existing flow

**Open:** `demo-assets/session2/demo9-openspec/current-approval-flow.md` and
`backend/app/models.py`.

1. Attach both files.
2. Paste the prompt.
3. Ask the audience which compatibility risk they would prioritize.

**Prompt to paste:**

```text
Plan a partial-approval change without writing code. List the model changes,
status changes, API changes, UI effects, compatibility risks, and tests.
Separate must-have work from later improvements.
```

**Show:** Copilot can make impact analysis explicit before editing a stable
workflow.

### Demo 10 — Compare product, architecture, and QA views

**Open:** the plans from Demos 8 and 9.

1. Paste both plans into a fresh Copilot Chat.
2. Paste the prompt.
3. Read only the final prioritized recommendation aloud.

**Prompt to paste:**

```text
Review these plans from three viewpoints: product manager, software architect,
and QA lead. Give each viewpoint two concerns. Then produce one prioritized
release plan with a reason for the ordering.
```

**Show:** Role-based thinking can be simulated in one normal Copilot response.

### Demo 11 — Review a deliberately flawed change

**Open:** `demo-assets/session2/demo11-pr-review/bulk_approval_router.review_branch.py`.

1. Attach the file; do not copy it into the running app.
2. Paste the prompt.
3. Compare Copilot's findings with the five planted issues in that folder's
   README after the audience has guessed.

**Prompt to paste:**

```text
Review this Python change as if it were a pull request. Report only actionable
findings. For each, give severity (critical/high/medium/low), the relevant
code, impact, and a concise recommendation. Check null handling, performance,
concurrency, tests, and naming.
```

**Show:** Copilot can provide a repeatable first-pass code review in the IDE.

### Demo 12 — Review security without running risky code

**Open:** `demo-assets/session2/demo12-security/vulnerable_invoice_repository.py`.

1. Attach the file only. Never run, import, or copy it into `backend/app`.
2. Paste the prompt.
3. Reveal the expected three findings from the folder README afterward.

**Prompt to paste:**

```text
Perform a security review of this file. Do not execute it. For each finding,
name the weakness, severity, exploit path, and a safe remediation. Focus on
input handling, secrets, database access, and authorization.
```

**Show:** Security review is useful even when no code is executed.

### Demo 13 — Ask for test ideas before generated tests

**Open:** the `DiscountCalculator` class in `backend/app/services.py`.

1. Select only the `DiscountCalculator` class.
2. Ask Copilot the prompt.
3. Turn the best five cases into tests only if time permits.

**Prompt to paste:**

```text
Before writing tests, list edge cases for this calculator under these headings:
boundaries, invalid values, rounding, and stacked discounts. Identify any
likely defects from the current logic and propose the five highest-value tests.
```

**Show:** The useful Copilot step is test design, not blindly accepting a large
generated test file.

### Demo 14 — Smoke-test the API manually

**Open:** `backend/app/routers/invoices.py` and `backend/app/routers/approvals.py`.

1. In `backend/`, start the API: `uvicorn app.main:app --reload --port 5000`.
2. Open `http://localhost:5000/swagger` in a browser.
3. Use Swagger's **Try it out** to call `GET /api/invoices`.
4. Attach the two route files to Copilot and paste the prompt.

**Prompt to paste:**

```text
Read these two FastAPI route files. Give me a three-step manual smoke test in
Swagger: list invoices, approve one pending invoice as demo.approver, and
verify the changed invoice. Include the exact request bodies.
```

**Show:** Copilot helps create a practical manual test; no Playwright or
Angular app is needed.

### Demo 15 — Create a diagram as text

**Open:** `backend/app/main.py`, `backend/app/routers/approvals.py`,
`backend/app/services.py`, and `backend/app/repositories.py`.

1. Attach the four files.
2. Paste the prompt.
3. Copy the returned Mermaid code into any Mermaid preview later, or simply
   read the flow from the text.

**Prompt to paste:**

```text
Create Mermaid flowchart code for the approval request path. Show Angular as
the caller, then FastAPI route, dependency, ApprovalService, repository, and
response. Use only components present in the attached files.
```

**Show:** A diagram can be drafted with normal Copilot Chat; no Mermaid server
is required.

### Demo 16 — Draft a decision record

**Open:** `demo-assets/session3/demo16-adr/adr-template.md`.

1. Attach the template.
2. Paste the prompt.
3. Ask the audience whether they agree with the trade-off.

**Prompt to paste:**

```text
Fill this ADR template for a decision about sending a notification after an
invoice is approved. Compare transactional outbox, direct publish, and polling
against reliability, duplicate sends, implementation effort, and operations.
Make one recommendation.
```

**Show:** Copilot provides a decision draft that humans can challenge.

### Demo 17 — Analyze an incident from supplied evidence

**Open:** `demo-assets/session3/demo17-rca/app-logs.txt` and
`demo-assets/session3/demo17-rca/deploy-diff.patch`.

1. Attach both files.
2. Paste the prompt.
3. Verify that the answer connects the change in configuration with the first
   failures in the log timeline.

**Prompt to paste:**

```text
Create a short root-cause analysis from these logs and deploy diff. Include a
timeline, most likely cause with evidence, one alternative hypothesis,
immediate safe mitigations, and one prevention action. Do not assume facts not
in the files.
```

**Show:** Copilot can turn raw operational evidence into a reviewable RCA.

### Demo 18 — Improve a pipeline on paper

**Open:** `.github/workflows/ci.yml` and
`demo-assets/session3/demo18-pipeline/timings.csv`.

1. Attach both files.
2. Paste the prompt.
3. Ask Copilot to explain its first two changes in plain language.

**Prompt to paste:**

```text
Analyze this workflow and its timing data. Propose the smallest safe CI plan
to reduce wall-clock time. Keep security-scan and secret-scan mandatory before
e2e and merge. Identify which jobs can run in parallel and where dependency
caching helps. Do not edit the workflow.
```

**Show:** Copilot makes a performance plan while respecting explicit quality
constraints.

### Demo 19 — Practice incident communication with human approval

**Open:** all files in `demo-assets/session3/demo19-incident/` plus the two
Demo 17 files.

1. Attach the alert, runbook, logs, and deploy diff.
2. Paste the prompt.
3. Highlight the section labelled **Needs human approval**.

**Prompt to paste:**

```text
Act as an incident coordinator. Based only on these inputs, draft a concise
stakeholder update, current hypothesis, evidence, and next actions. Separate
actions we can investigate from actions that need explicit human approval.
Do not recommend executing a rollback or configuration change automatically.
```

**Show:** Copilot can support a responder without taking production actions.

### Demo 20 — Evaluate a review prompt manually

**Open:** `demo-assets/session3/demo20-eval/review-skill-eval-cases.json`.

1. Attach the JSON file.
2. Paste the prompt.
3. Read the five pass/fail rows; no evaluation framework is needed.

**Prompt to paste:**

```text
Read this fixed evaluation set. For each case, state the file to inspect, the
finding a code review should produce, and the expected severity. Return a
five-row checklist with columns: case, expected finding, severity, and pass
condition. Do not change the cases or inspect unrelated files.
```

**Show:** A small fixed checklist is enough to make Copilot review quality
measurable over time.

## Presentation tips

- Run only 3–4 demos in one session; Demo 1, 2, 5, 11, 12, 14, 17, and 19
  form a practical starter set.
- Let Copilot generate an answer, then pause to ask the audience what they
  would verify before accepting it. The review conversation is the demo.
- For code-changing exercises, use a throwaway branch or reject the edit after
  discussing it. The intentionally failing/insecure files are workshop
  fixtures, not changes to keep.
- Keep prompts short, attach only the named files, and avoid asking Copilot to
  scan the whole repository. This makes every showcase fast and predictable.

## Safety notes

- `demo-assets/session2/demo12-security/` is intentionally vulnerable
  code. It is not referenced anywhere in `backend/app/main.py`. Never deploy
  this repo's `demo-assets/` folder, and never point a real database
  connection string at anything in it.
- Nothing in `demo-assets/` is real customer, employee, or financial
  data — all names, tickets, and figures are synthetic.
