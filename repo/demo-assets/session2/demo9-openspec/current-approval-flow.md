# Current approval flow (baseline for the OpenSpec demo)

Session 2, Demo 9 asks the agent to propose a change to *this* existing
behaviour - having it written down gives OpenSpec something concrete to
diff against.

## Current behaviour

- An invoice has one of these statuses: Draft, PendingApproval,
  Approved, Rejected.
- `ApprovalService.approve(invoice_id, approved_by)` sets the invoice to
  Approved for its full amount. There is no partial state.
- `ApprovalService.reject(invoice_id, approved_by, reason)` sets the
  invoice to Rejected with a reason.
- Approval is one invoice at a time. There is no bulk operation (that's
  Demo 8, via Spec Kit, on a separate code path).
- `InvoiceStatus.PARTIALLY_APPROVED` already exists in the enum as a
  placeholder but nothing sets or reads it yet.

## The change to propose in the demo

Allow an approver to approve an invoice for less than its full amount
(a "partial approval"), recording both the original and approved
amounts, and moving the invoice to `PartiallyApproved` instead of
`Approved`. This is the same "per-item override" capability Finance Ops
asked for in the Session 1 Demo 2 source material - OpenSpec should
surface that connection if the transcript is in context.
