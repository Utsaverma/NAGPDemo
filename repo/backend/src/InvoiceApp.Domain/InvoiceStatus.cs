namespace InvoiceApp.Domain;

public enum InvoiceStatus
{
    Draft,
    PendingApproval,
    Approved,
    PartiallyApproved, // added for Session 2 - Demo 9 (OpenSpec) - not yet used by ApprovalService
    Rejected
}
