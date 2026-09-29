from decimal import Decimal
from typing import Optional

from app.models import Invoice, InvoiceStatus, Order
from app.repositories import InvoiceRepository


class ApprovalService:
    """Current flow: approve or reject one full invoice at a time."""

    def __init__(self, repository: InvoiceRepository) -> None:
        self._repository = repository

    def approve(self, invoice_id: str, approved_by: str) -> Invoice:
        invoice = self._get_invoice(invoice_id)
        invoice.status = InvoiceStatus.APPROVED
        invoice.approved_by = approved_by
        self._repository.update(invoice)
        return invoice

    def reject(self, invoice_id: str, approved_by: str, reason: str) -> Invoice:
        invoice = self._get_invoice(invoice_id)
        invoice.status = InvoiceStatus.REJECTED
        invoice.approved_by = approved_by
        invoice.decision_note = reason
        self._repository.update(invoice)
        return invoice

    def _get_invoice(self, invoice_id: str) -> Invoice:
        invoice = self._repository.get_by_id(invoice_id)
        if invoice is None:
            raise ValueError(f"Invoice {invoice_id} not found.")
        return invoice


class DiscountCalculator:
    """Deliberately preserves the quirks used in Session 2, Demo 13."""

    def quantity_discount(self, quantity: int) -> Decimal:
        if quantity >= 100:
            return Decimal("0.15")
        if quantity >= 50:
            return Decimal("0.10")
        if quantity >= 10:
            return Decimal("0.05")
        return Decimal("0")

    def loyalty_discount(self, years_as_customer: int) -> Decimal:
        return min(Decimal(years_as_customer) * Decimal("0.01"), Decimal("0.10"))

    def combined_discount(
        self, quantity: int, years_as_customer: int, customer_type: Optional[str]
    ) -> Decimal:
        discount = self.quantity_discount(quantity) + self.loyalty_discount(years_as_customer)
        if customer_type == "Nonprofit":
            discount += Decimal("0.05")
        return discount


class OrderTotalCalculator:
    """Contains the intentional Session 1 Demo 1 SAVE10 bug."""

    def calculate_total(self, order: Order) -> Decimal:
        total = Decimal("0")
        for item in order.items:
            line_total = item.line_total
            if order.coupon_code == "SAVE10":
                line_total -= total * Decimal("0.10")
            total += line_total
        return total
