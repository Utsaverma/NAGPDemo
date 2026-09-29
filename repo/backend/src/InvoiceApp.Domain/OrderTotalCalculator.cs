namespace InvoiceApp.Domain;

// Seeded bug for Session 1 - Demo 1 ("One task, two agents").
//
// Intent: SAVE10 should take 10% off the order's subtotal ONCE.
// Bug: the discount is applied inside the per-item loop instead of
// after the subtotal is known, so a 2-item order gets discounted twice
// and a 3-item order three times. OrderTotalTests.AppliesDiscountOnce
// (see backend/tests) fails against this implementation.
//
// Do not fix this by hand before the workshop - the agent is meant to
// find and fix it live.
public class OrderTotalCalculator
{
    public decimal CalculateTotal(Order order)
    {
        decimal total = 0m;

        foreach (var item in order.Items)
        {
            var lineTotal = item.LineTotal;

            if (order.CouponCode == "SAVE10")
            {
                lineTotal -= total * 0.10m; // BUG: discounts the running total on every iteration
            }

            total += lineTotal;
        }

        return total;
    }
}
