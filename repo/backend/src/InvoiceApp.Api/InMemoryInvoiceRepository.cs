using InvoiceApp.Domain;

namespace InvoiceApp.Api;

// Simple in-memory store so the sample app runs with zero setup.
// Seeded with a few invoices so the Playwright demo (Session 2, Demo 14)
// and the Angular Invoices page have something to show immediately.
public class InMemoryInvoiceRepository : IInvoiceRepository
{
    private readonly List<Invoice> _invoices = new()
    {
        new Invoice { Id = "INV-1001", CustomerName = "Lakeside School District", Amount = 4250.00m, Status = InvoiceStatus.PendingApproval },
        new Invoice { Id = "INV-1002", CustomerName = "Hilltop Academy", Amount = 980.50m, Status = InvoiceStatus.PendingApproval },
        new Invoice { Id = "INV-1003", CustomerName = "Riverside Charter", Amount = 12300.00m, Status = InvoiceStatus.Approved, ApprovedBy = "demo.approver" },
        new Invoice { Id = "INV-1004", CustomerName = "Oakwood Independent", Amount = 615.75m, Status = InvoiceStatus.PendingApproval },
    };

    public IReadOnlyList<Invoice> GetAll() => _invoices;

    public Invoice? GetById(string id) => _invoices.FirstOrDefault(i => i.Id == id);

    public Invoice Add(Invoice invoice)
    {
        _invoices.Add(invoice);
        return invoice;
    }

    public void Update(Invoice invoice)
    {
        var index = _invoices.FindIndex(i => i.Id == invoice.Id);
        if (index >= 0) _invoices[index] = invoice;
    }
}
