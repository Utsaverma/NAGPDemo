# Frontend setup note

This folder ships only the source files that matter for the workshop demos
(components, service, templates) - not a full Angular CLI scaffold, so we
don't hand out a generated `angular.json`/`package.json` pair that drifts out
of date with whatever CLI version you have installed.

To run it:

1. `ng new invoice-app --routing --style=css --skip-git` in an empty folder
   (or reuse your own Angular 17+ shell).
2. Copy everything under `frontend/src/app/` into the generated project's
   `src/app/`, replacing the default files.
3. Point `InvoiceService` at your API's base URL if it isn't
   `http://localhost:5000`.
4. `ng serve` and open `http://localhost:4200`.

Nothing here talks to a real backend session/auth system - `demo.approver`
is a hardcoded test user for the Playwright demo (Session 2, Demo 14).
