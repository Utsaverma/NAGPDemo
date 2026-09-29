using System.Data.SqlClient;

namespace InvoiceApp.Api.SecurityDemo;

// INTENTIONALLY VULNERABLE - for the Session 2, Demo 12 security review
// only. Never register this in Program.cs or deploy it anywhere.
public class VulnerableInvoiceRepository
{
    // Issue: hardcoded credential in source.
    private const string ConnectionString =
        "Server=prod-db.internal;Database=Invoices;User Id=svc_invoices;Password=P@ssw0rd2024!;";

    public List<string> GetByCustomerName(string customerName)
    {
        var results = new List<string>();

        using var connection = new SqlConnection(ConnectionString);
        connection.Open();

        // Issue: SQL injection - customerName is concatenated straight
        // into the query text instead of using a parameter.
        var sql = "SELECT Id, Amount FROM Invoices WHERE CustomerName = '" + customerName + "'";
        using var command = new SqlCommand(sql, connection);
        using var reader = command.ExecuteReader();

        while (reader.Read())
        {
            results.Add(reader.GetString(0));
        }

        return results;
    }

    // Issue: missing authorization check - any caller can wipe every
    // invoice for any customer, with no check that they own or manage
    // that customer's account.
    public void DeleteAllForCustomer(string customerName)
    {
        using var connection = new SqlConnection(ConnectionString);
        connection.Open();

        var sql = "DELETE FROM Invoices WHERE CustomerName = '" + customerName + "'";
        using var command = new SqlCommand(sql, connection);
        command.ExecuteNonQuery();
    }
}
