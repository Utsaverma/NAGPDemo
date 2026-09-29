from typing import Optional, Protocol

from app.models import Invoice, InvoiceStatus


class InvoiceRepository(Protocol):
    def get_all(self) -> list[Invoice]: ...

    def get_by_id(self, invoice_id: str) -> Optional[Invoice]: ...

    def add(self, invoice: Invoice) -> Invoice: ...

    def update(self, invoice: Invoice) -> None: ...


class InMemoryInvoiceRepository:
    """A zero-configuration store seeded for the workshop demos."""

    def __init__(self) -> None:
        self._invoices = [
            Invoice(id="INV-1001", customer_name="Lakeside School District", amount="4250.00", status=InvoiceStatus.PENDING_APPROVAL),
            Invoice(id="INV-1002", customer_name="Hilltop Academy", amount="980.50", status=InvoiceStatus.PENDING_APPROVAL),
            Invoice(id="INV-1003", customer_name="Riverside Charter", amount="12300.00", status=InvoiceStatus.APPROVED, approved_by="demo.approver"),
            Invoice(id="INV-1004", customer_name="Oakwood Independent", amount="615.75", status=InvoiceStatus.PENDING_APPROVAL),
        ]

    def get_all(self) -> list[Invoice]:
        return self._invoices

    def get_by_id(self, invoice_id: str) -> Optional[Invoice]:
        return next((invoice for invoice in self._invoices if invoice.id == invoice_id), None)

    def add(self, invoice: Invoice) -> Invoice:
        self._invoices.append(invoice)
        return invoice

    def update(self, invoice: Invoice) -> None:
        for index, existing in enumerate(self._invoices):
            if existing.id == invoice.id:
                self._invoices[index] = invoice
                return
