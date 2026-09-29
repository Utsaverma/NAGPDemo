from fastapi import APIRouter, Depends, HTTPException, Request, Response, status

from app.dependencies import get_invoice_repository
from app.models import Invoice, InvoiceStatus
from app.repositories import InMemoryInvoiceRepository


router = APIRouter(prefix="/api/invoices", tags=["invoices"])


@router.get("", response_model=list[Invoice])
def get_all(repository: InMemoryInvoiceRepository = Depends(get_invoice_repository)) -> list[Invoice]:
    return repository.get_all()


@router.get("/{invoice_id}", response_model=Invoice)
def get_by_id(
    invoice_id: str, repository: InMemoryInvoiceRepository = Depends(get_invoice_repository)
) -> Invoice:
    invoice = repository.get_by_id(invoice_id)
    if invoice is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return invoice


@router.post("", response_model=Invoice, status_code=status.HTTP_201_CREATED)
def create(
    invoice: Invoice,
    request: Request,
    response: Response,
    repository: InMemoryInvoiceRepository = Depends(get_invoice_repository),
) -> Invoice:
    invoice.status = InvoiceStatus.PENDING_APPROVAL
    created = repository.add(invoice)
    response.headers["Location"] = str(request.url_for("get_by_id", invoice_id=created.id))
    return created


# TODO (Session 1, Demo 5): add GET /export returning all invoices as CSV.
