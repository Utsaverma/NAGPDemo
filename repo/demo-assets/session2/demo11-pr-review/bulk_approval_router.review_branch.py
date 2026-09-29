from typing import Optional

from fastapi import APIRouter
from pydantic import BaseModel

from app.models import InvoiceStatus
from app.repositories import InvoiceRepository
from app.services import ApprovalService


router = APIRouter(prefix="/api/approvals", tags=["approvals"])


class BulkApproveRequest(BaseModel):
    invoice_ids: Optional[list[str]] = None
    approved_by: str


class BulkApproveResult(BaseModel):
    invoice_id: str
    success: bool
    error: Optional[str] = None


def bulk_approve(
    request: BulkApproveRequest,
    repository: InvoiceRepository,
    approval_service: ApprovalService,
) -> list[BulkApproveResult]:
    results: list[BulkApproveResult] = []

    # Issue 1: no null check on request.invoice_ids - a request body
    # missing the field throws here instead of returning 400.
    for invoice_id in request.invoice_ids:
        results.append(process_one(invoice_id, request.approved_by, True, repository, approval_service))

    return results


# Issue 5: "flag" doesn't say what it does (it controls whether a
# rejection reason is required before processing).
def process_one(
    invoice_id: str,
    approved_by: str,
    flag: bool,
    repository: InvoiceRepository,
    approval_service: ApprovalService,
) -> BulkApproveResult:
    # Issue 2: N+1 - fetches one invoice at a time inside the loop
    # instead of a single batched lookup before the loop starts.
    invoice = repository.get_by_id(invoice_id)
    if invoice is None:
        return BulkApproveResult(invoice_id=invoice_id, success=False, error="Not found")

    # Issue 3: read-then-write with no lock/version check - two
    # concurrent bulk-approve calls touching the same invoice ID can
    # both pass this check before either call writes back.
    if invoice.status != InvoiceStatus.PENDING_APPROVAL:
        return BulkApproveResult(invoice_id=invoice_id, success=False, error="Not pending")

    approved = approval_service.approve(invoice_id, approved_by)
    return BulkApproveResult(invoice_id=approved.id, success=True)


# Issue 4: no bulk-approval-router test accompanies this PR.
