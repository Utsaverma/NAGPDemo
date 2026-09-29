# Security review demo (Session 2, Demo 12)

`VulnerableInvoiceRepository.cs` is intentionally insecure. It is NOT
referenced anywhere in `Program.cs` or wired into dependency injection -
it exists only as a diff to review live. Do not register it as a
service, and do not deploy this repo's `demo-assets/` folder anywhere
that runs the API.

To run the demo: present this file as "a change under review" (e.g.
paste it into the chat, or stage it as an uncommitted file) and ask the
agent for a security review mapped to the OWASP Top 10.

## The three planted issues

1. **SQL injection** - `GetByCustomerName` builds a raw SQL string by
   concatenating user input directly into the query text.
2. **Hardcoded secret** - the connection string embeds a real-looking
   database password in source.
3. **Missing authorization check** - `DeleteAllForCustomer` performs a
   destructive, account-wide action with no check that the caller is
   allowed to do it for that customer.
