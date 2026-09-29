from datetime import datetime, timezone
from decimal import Decimal
from enum import Enum
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field, field_serializer


def to_camel(value: str) -> str:
    """Match the JSON field names used by the Angular client."""
    first, *rest = value.split("_")
    return first + "".join(word.capitalize() for word in rest)


class ApiModel(BaseModel):
    model_config = ConfigDict(
        alias_generator=to_camel,
        populate_by_name=True,
    )


class InvoiceStatus(str, Enum):
    DRAFT = "Draft"
    PENDING_APPROVAL = "PendingApproval"
    APPROVED = "Approved"
    PARTIALLY_APPROVED = "PartiallyApproved"
    REJECTED = "Rejected"


class Invoice(ApiModel):
    id: str = ""
    customer_name: str = ""
    amount: Decimal = Decimal("0")
    status: InvoiceStatus = InvoiceStatus.DRAFT
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    approved_by: Optional[str] = None
    decision_note: Optional[str] = None

    @field_serializer("amount")
    def serialize_amount(self, value: Decimal) -> float:
        return float(value)


class OrderItem(ApiModel):
    sku: str = ""
    quantity: int = 0
    unit_price: Decimal = Decimal("0")

    @property
    def line_total(self) -> Decimal:
        return self.quantity * self.unit_price

    @field_serializer("unit_price")
    def serialize_unit_price(self, value: Decimal) -> float:
        return float(value)


class Order(ApiModel):
    id: str = ""
    items: list[OrderItem] = Field(default_factory=list)
    coupon_code: Optional[str] = None


class ApproveRequest(ApiModel):
    approved_by: str


class RejectRequest(ApiModel):
    approved_by: str
    reason: str
