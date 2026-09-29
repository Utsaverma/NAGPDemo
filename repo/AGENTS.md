# Project conventions for AI agents

This file is read by agentic coding tools at session start (rename or
symlink to CLAUDE.md if your tool expects that name). Used live in
Session 1, Demos 5-7.

## Stack

- Backend: ASP.NET Core 8 Web API (`backend/src/InvoiceApp.Api`), domain
  logic in `backend/src/InvoiceApp.Domain`, tests in
  `backend/tests/InvoiceApp.Tests` (xUnit).
- Frontend: Angular 17+, standalone components, under `frontend/src/app`.

## Conventions

- **Controllers** live under `Controllers/`, one per resource, named
  `<Resource>Controller`. Route pattern: `api/[controller]`.
- **DTOs / request records** are declared inline in the controller as
  C# `record` types (see `ApprovalsController.ApproveRequest`) unless
  shared across controllers, in which case they move to
  `InvoiceApp.Domain`.
- **Every new endpoint needs a test.** Tests live in
  `InvoiceApp.Tests`, one test class per class under test, named
  `<ClassUnderTest>Tests`.
- **Dependency injection**: register new services in `Program.cs`.
  Repositories are interfaces in `InvoiceApp.Domain`
  (`I<Name>Repository`) with an in-memory implementation in
  `InvoiceApp.Api` for the demo environment.
- **Angular services** call the API base URL defined in
  `InvoiceService` (`API_BASE`). New API calls go through a service,
  never straight from a component.
- Run `dotnet test` from `backend/` before considering backend work
  done. Run `ng test` from `frontend/` for frontend work.

## What NOT to do in this repo

- Do not commit real credentials, tokens, or customer data. Everything
  under `demo-assets/` is synthetic.
- Do not touch `demo-assets/session2/demo12-security/` outside of the
  security-review demo - it contains intentionally vulnerable code that
  must never be wired into `Program.cs`.
