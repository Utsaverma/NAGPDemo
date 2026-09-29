using InvoiceApp.Domain;
using Microsoft.AspNetCore.Mvc;

namespace InvoiceApp.Api.Controllers;

[ApiController]
[Route("api/[controller]")]
public class BulkApprovalController : ControllerBase
{
    private readonly IInvoiceRepository _repository;
    private readonly ApprovalService _approvalService;

    public BulkApprovalController(IInvoiceRepository repository, ApprovalService approvalService)
    {
        _repository = repository;
        _approvalService = approvalService;
    }

    public record BulkApproveRequest(List<string> InvoiceIds, string ApprovedBy);
    public record BulkApproveResult(string InvoiceId, bool Success, string? Error);

    [HttpPost("bulk-approve")]
    public ActionResult<List<BulkApproveResult>> BulkApprove([FromBody] BulkApproveRequest request)
    {
        var results = new List<BulkApproveResult>();

        // Issue 1: no null check on request.InvoiceIds - a request body
        // missing the field throws here instead of returning 400.
        foreach (var id in request.InvoiceIds)
        {
            results.Add(ProcessOne(id, request.ApprovedBy, true));
        }

        return Ok(results);
    }

    // Issue 5: "flag" doesn't say what it does (it controls whether a
    // rejection reason is required before processing).
    private BulkApproveResult ProcessOne(string invoiceId, string approvedBy, bool flag)
    {
        // Issue 2: N+1 - fetches one invoice at a time inside the loop
        // instead of a single batched lookup before the loop starts.
        var invoice = _repository.GetById(invoiceId);
        if (invoice is null)
        {
            return new BulkApproveResult(invoiceId, false, "Not found");
        }

        // Issue 3: read-then-write with no lock/version check - two
        // concurrent bulk-approve calls hitting the same invoice ID can
        // both pass this check before either call writes back.
        if (invoice.Status != InvoiceStatus.PendingApproval)
        {
            return new BulkApproveResult(invoiceId, false, "Not pending");
        }

        var approved = _approvalService.Approve(invoiceId, approvedBy);
        return new BulkApproveResult(approved.Id, true, null);
    }

    // Issue 4: no BulkApprovalControllerTests.cs anywhere in this PR.
}
