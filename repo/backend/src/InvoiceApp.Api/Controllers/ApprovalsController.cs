using InvoiceApp.Domain;
using Microsoft.AspNetCore.Mvc;

namespace InvoiceApp.Api.Controllers;

// Single-invoice approve/reject only. Session 2 Demo 8 (Spec Kit) adds
// bulk approval here; Demo 9 (OpenSpec) adds partial approval as a
// change to this existing flow.
[ApiController]
[Route("api/[controller]")]
public class ApprovalsController : ControllerBase
{
    private readonly ApprovalService _approvalService;

    public ApprovalsController(ApprovalService approvalService)
    {
        _approvalService = approvalService;
    }

    public record ApproveRequest(string ApprovedBy);
    public record RejectRequest(string ApprovedBy, string Reason);

    [HttpPost("{invoiceId}/approve")]
    public ActionResult<Invoice> Approve(string invoiceId, [FromBody] ApproveRequest request)
    {
        try
        {
            return Ok(_approvalService.Approve(invoiceId, request.ApprovedBy));
        }
        catch (InvalidOperationException ex)
        {
            return NotFound(ex.Message);
        }
    }

    [HttpPost("{invoiceId}/reject")]
    public ActionResult<Invoice> Reject(string invoiceId, [FromBody] RejectRequest request)
    {
        try
        {
            return Ok(_approvalService.Reject(invoiceId, request.ApprovedBy, request.Reason));
        }
        catch (InvalidOperationException ex)
        {
            return NotFound(ex.Message);
        }
    }

    // TODO (Session 2, Demo 8): [HttpPost("bulk-approve")] accepting a
    // list of invoice ids, returning a per-item summary.
}
