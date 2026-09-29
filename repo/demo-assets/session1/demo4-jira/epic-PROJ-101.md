# Jira sandbox setup note (Session 1, Demo 4)

This demo needs a real Jira sandbox project connected through the Jira
MCP server - there's no way to fake that inside a repo. Create one epic
in your sandbox using the content below, then point the agent at it by
its real key (referred to as PROJ-101 in the deck and speaker notes).

---

**Epic: Bulk Invoice Approval (v1)**

**Description**

Finance operations approvers need to review and approve multiple
pending invoices in one action instead of one at a time. Scope for v1:

- Multi-select invoices from the pending list
- Summary screen before confirming (total amount, invoice count,
  customers involved)
- Per-item override: exclude an item, or approve a different (partial)
  amount for that item
- Two-person sign-off required when a single invoice exceeds $1,000
- Full audit trail: who approved what, when, and any overrides applied

**Comments (seed these on the epic so the demo has real discussion to read)**

> Priya (Finance Ops): Confirmed the sign-off threshold is $1,000, not
> $500 - we changed it after last week's budget review.

> Sam (Product): Email notifications are out of scope for v1 pending
> infra sign-off on send limits. In-app notification only.

> Meera (Eng): Partial approval (changing the approved amount, not just
> excluding an item) is the harder half of this - flagging for
> estimation.
