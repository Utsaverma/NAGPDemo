from decimal import Decimal

from app.models import Order, OrderItem
from app.services import OrderTotalCalculator


class TestOrderTotalCalculator:
    # Session 1, Demo 1: this intentionally fails against the seeded bug.
    # Give this test, and only this test, to separate agents during the demo.
    def test_applies_discount_once(self) -> None:
        order = Order(
            id="ORD-1",
            coupon_code="SAVE10",
            items=[
                OrderItem(sku="BOOK-1", quantity=1, unit_price=Decimal("50")),
                OrderItem(sku="BOOK-2", quantity=1, unit_price=Decimal("50")),
            ],
        )

        total = OrderTotalCalculator().calculate_total(order)

        assert total == Decimal("90")

    def test_no_coupon_charges_full_price(self) -> None:
        order = Order(
            id="ORD-2",
            items=[OrderItem(sku="BOOK-1", quantity=2, unit_price=Decimal("20"))],
        )

        total = OrderTotalCalculator().calculate_total(order)

        assert total == Decimal("40")
