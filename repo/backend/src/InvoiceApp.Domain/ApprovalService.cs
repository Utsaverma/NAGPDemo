namespace InvoiceApp.Domain;

// Current behaviour: an invoice is approved or rejected as a whole, one
// at a time, by a single approver. This is the "existing approval flow"
// referenced in Session 2 - Demo 9 (OpenSpec) and Session 2 - Demo 8
// (Spec Kit extends this to bulk approval).
public class ApprovalService
{
    private readonly IInvoiceRepository _repository;

    public ApprovalService(IInvoiceRepository repository)
    {
        _repository = repository;
    }

    public Invoice Approve(string invoiceId, string approvedBy)
    {
        var invoice = _repository.GetById(invoiceId)
            ?? throw new InvalidOperationException($"Invoice {invoiceId} not found.");

        invoice.Status = InvoiceStatus.Approved;
        invoice.ApprovedBy = approvedBy;
        _repository.Update(invoice);
        return invoice;
    }

    public Invoice Reject(string invoiceId, string approvedBy, string reason)
    {
        var invoice = _repository.GetById(invoiceId)
            ?? throw new InvalidOperationException($"Invoice {invoiceId} not found.");

        invoice.Status = InvoiceStatus.Rejected;
        invoice.ApprovedBy = approvedBy;
        invoice.DecisionNote = reason;
        _repository.Update(invoice);
        return invoice;
    }

    // No BulkApprove / PartialApprove methods yet - Session 2 Demos 8 and 9
    // add these live.
}
