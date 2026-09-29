using InvoiceApp.Domain;
using Xunit;

namespace InvoiceApp.Tests;

public class OrderTotalTests
{
    // Session 1 - Demo 1 ("One task, two agents"). This test currently
    // FAILS against OrderTotalCalculator.cs - that is intentional. Give
    // this test (and only this test) to an IDE agent and a terminal
    // agent side by side and compare how each finds and fixes the bug.
    [Fact]
    public void AppliesDiscountOnce()
    {
        var order = new Order
        {
            Id = "ORD-1",
            CouponCode = "SAVE10",
            Items = new List<OrderItem>
            {
                new() { Sku = "BOOK-1", Quantity = 1, UnitPrice = 50m },
                new() { Sku = "BOOK-2", Quantity = 1, UnitPrice = 50m },
            }
        };

        var calculator = new OrderTotalCalculator();
        var total = calculator.CalculateTotal(order);

        // $100 subtotal, 10% off once = $90.
        Assert.Equal(90m, total);
    }

    [Fact]
    public void NoCouponChargesFullPrice()
    {
        var order = new Order
        {
            Id = "ORD-2",
            Items = new List<OrderItem>
            {
                new() { Sku = "BOOK-1", Quantity = 2, UnitPrice = 20m },
            }
        };

        var calculator = new OrderTotalCalculator();
        var total = calculator.CalculateTotal(order);

        Assert.Equal(40m, total);
    }
}
