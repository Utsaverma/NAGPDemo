# Project conventions for AI agents

This file is read by agentic coding tools at session start (rename or
symlink to CLAUDE.md if your tool expects that name). Used live in
Session 1, Demos 5-7.

## Stack

- Backend: FastAPI (`backend/app`), with domain logic in `models.py` and
  `services.py`, and pytest tests in `backend/tests`.
- Frontend: Angular 17+, standalone components, under `frontend/src/app`.

## Conventions

- **Routes** live under `backend/app/routers/`, one module per resource.
  Keep the existing `/api/<resource>` route pattern.
- **DTOs / request models** are Pydantic models in `backend/app/models.py`.
  Keep shared API and domain models there unless a model is specific to one
  route module.
- **Every new endpoint needs a test.** Tests live in `backend/tests`, one
  test class or module per unit under test, using pytest.
- **Dependency injection**: expose dependencies from
  `backend/app/dependencies.py`. Repositories use the `InvoiceRepository`
  protocol with the in-memory implementation in `backend/app/repositories.py`
  for the demo environment.
- **Angular services** call the API base URL defined in
  `InvoiceService` (`API_BASE`). New API calls go through a service,
  never straight from a component.
- Run `pytest` from `backend/` before considering backend work done. Run
  `ng test` from `frontend/` for frontend work.

## What NOT to do in this repo

- Do not commit real credentials, tokens, or customer data. Everything
  under `demo-assets/` is synthetic.
- Do not touch `demo-assets/session2/demo12-security/` outside of the
  security-review demo - it contains intentionally vulnerable code that
  must never be wired into `app/main.py`.
