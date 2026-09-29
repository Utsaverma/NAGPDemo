namespace InvoiceApp.Domain;

// Legacy class for Session 2 - Demo 13 ("Generated tests and edge cases").
// Deliberately untested - no *DiscountCalculatorTests.cs exists anywhere
// in this repo. The agent should list edge cases (boundaries, nulls,
// rounding, currency) before writing tests.
//
// Known quirks worth noticing during the demo:
//  - QuantityDiscount has an off-by-one at the tier boundary (100 units
//    gets the 100-unit rate, but the comment below suggests otherwise).
//  - LoyaltyDiscount does not clamp negative "yearsAsCustomer" values.
//  - Combined discounts are not capped, so they can exceed 100%.
public class DiscountCalculator
{
    // "Over 100 units" was meant to mean 101+, but the check below
    // is inclusive of 100. Left as-is on purpose for the demo.
    public decimal QuantityDiscount(int quantity)
    {
        if (quantity >= 100) return 0.15m;
        if (quantity >= 50) return 0.10m;
        if (quantity >= 10) return 0.05m;
        return 0m;
    }

    public decimal LoyaltyDiscount(int yearsAsCustomer)
    {
        return Math.Min(yearsAsCustomer * 0.01m, 0.10m);
    }

    public decimal CombinedDiscount(int quantity, int yearsAsCustomer, string? customerType)
    {
        var discount = QuantityDiscount(quantity) + LoyaltyDiscount(yearsAsCustomer);

        if (customerType == "Nonprofit")
        {
            discount += 0.05m;
        }

        return discount; // not capped - can exceed 1.0m with enough stacking
    }
}
