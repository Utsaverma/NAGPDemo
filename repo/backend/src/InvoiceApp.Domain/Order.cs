namespace InvoiceApp.Domain;

public class Order
{
    public string Id { get; set; } = string.Empty;
    public List<OrderItem> Items { get; set; } = new();

    // Null or empty when no coupon was applied.
    public string? CouponCode { get; set; }
}
