from fastapi import APIRouter, Depends, HTTPException, status

from app.dependencies import get_approval_service
from app.models import ApproveRequest, Invoice, RejectRequest
from app.services import ApprovalService


router = APIRouter(prefix="/api/approvals", tags=["approvals"])


@router.post("/{invoice_id}/approve", response_model=Invoice)
def approve(
    invoice_id: str,
    request: ApproveRequest,
    approval_service: ApprovalService = Depends(get_approval_service),
) -> Invoice:
    try:
        return approval_service.approve(invoice_id, request.approved_by)
    except ValueError as error:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(error)) from error


@router.post("/{invoice_id}/reject", response_model=Invoice)
def reject(
    invoice_id: str,
    request: RejectRequest,
    approval_service: ApprovalService = Depends(get_approval_service),
) -> Invoice:
    try:
        return approval_service.reject(invoice_id, request.approved_by, request.reason)
    except ValueError as error:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(error)) from error


# TODO (Session 2, Demo 8): add POST /bulk-approve with a per-item summary.
