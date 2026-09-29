using InvoiceApp.Domain;
using Microsoft.AspNetCore.Mvc;

namespace InvoiceApp.Api.Controllers;

// Session 1 - Demo 5 target: add a "Download CSV" endpoint + Angular button
// to this controller. Nothing CSV-related exists here yet on purpose.
[ApiController]
[Route("api/[controller]")]
public class InvoicesController : ControllerBase
{
    private readonly IInvoiceRepository _repository;

    public InvoicesController(IInvoiceRepository repository)
    {
        _repository = repository;
    }

    [HttpGet]
    public ActionResult<IReadOnlyList<Invoice>> GetAll() => Ok(_repository.GetAll());

    [HttpGet("{id}")]
    public ActionResult<Invoice> GetById(string id)
    {
        var invoice = _repository.GetById(id);
        return invoice is null ? NotFound() : Ok(invoice);
    }

    [HttpPost]
    public ActionResult<Invoice> Create([FromBody] Invoice invoice)
    {
        invoice.Status = InvoiceStatus.PendingApproval;
        var created = _repository.Add(invoice);
        return CreatedAtAction(nameof(GetById), new { id = created.Id }, created);
    }

    // TODO (Session 1, Demo 5): [HttpGet("export")] returning a CSV of
    // all invoices. Left for the live demo.
}
