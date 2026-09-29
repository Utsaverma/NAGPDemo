namespace InvoiceApp.Domain;

public interface IInvoiceRepository
{
    IReadOnlyList<Invoice> GetAll();
    Invoice? GetById(string id);
    Invoice Add(Invoice invoice);
    void Update(Invoice invoice);
}
