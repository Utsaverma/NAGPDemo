# Jira sandbox setup note (Session 1, Demo 7)

Same as PROJ-101 - create this as a real ticket in your Jira sandbox
so the MCP demo has something to fetch.

---

**Ticket: PROJ-142 - Fix inconsistent order total calculation**

**Description**

QA found that order totals are inconsistent when a coupon is applied
to multi-item orders. A 2-item $100 order with SAVE10 should total
$90, but we're seeing $81. Suspect the discount is being applied more
than once.

**Acceptance criteria**

- SAVE10 discounts the order subtotal by exactly 10%, applied once
  regardless of item count
- `OrderTotalTests.AppliesDiscountOnce` passes
- No regression to orders without a coupon code

This maps directly to the bug in
`backend/app/services.py` (`OrderTotalCalculator`) used in Session
1, Demo 1 - Demo 7 reuses the same bug so the subagent + MCP demo can
reference a real ticket while a reviewer subagent checks the fix.
