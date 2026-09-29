from app.repositories import InMemoryInvoiceRepository
from app.services import ApprovalService


invoice_repository = InMemoryInvoiceRepository()
approval_service = ApprovalService(invoice_repository)


def get_invoice_repository() -> InMemoryInvoiceRepository:
    return invoice_repository


def get_approval_service() -> ApprovalService:
    return approval_service
