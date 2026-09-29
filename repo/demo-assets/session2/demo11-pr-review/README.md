# Staging this as a pull request (Session 2, Demo 11)

`bulk_approval_router.review_branch.py` is a working draft of the bulk
approve endpoint (the feature built live in Demo 8) with five issues
planted on purpose, so the automated review has real findings instead
of a clean diff.

## To set up the demo

1. Create a branch, e.g. `git checkout -b demo/bulk-approval-review`.
2. Copy this file's contents into
   `backend/app/routers/bulk_approvals.py`
   (a new file - it doesn't replace anything).
3. Add a bare-bones `bulk_approve` method to `ApprovalService` if you
   want it to compile (not required for the review demo itself, which
   only reads the diff).
4. Commit and open the PR. Ask the agent to review it against your
   team's checklist.

## The five planted issues (for your own reference - do not read this
## list aloud before the reveal)

1. **Null handling** - `request.InvoiceIds` is iterated without a null
   check; a missing field in the request body throws a
   `NullReferenceException` instead of a 400.
2. **N+1 query** - `_repository.GetById(id)` is called once per invoice
   ID in a loop instead of a single batch fetch.
3. **Race condition** - two concurrent bulk-approve calls touching the
   same invoice ID can both read `PendingApproval` before either writes
   `Approved`, so both "succeed" and the audit trail double-counts one
   approval.
4. **Missing test** - no test file accompanies this router at all.
5. **Unclear naming** - the boolean parameter `flag` on `ProcessOne`
   doesn't say what it controls (it toggles whether a rejection reason
   is required).
