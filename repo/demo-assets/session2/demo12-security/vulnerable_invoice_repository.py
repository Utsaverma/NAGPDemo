import sqlite3


# INTENTIONALLY VULNERABLE - for the Session 2, Demo 12 security review
# only. Never import this from backend/app/main.py or deploy it anywhere.
class VulnerableInvoiceRepository:
    # Issue: hardcoded credential in source.
    connection_string = (
        "Server=prod-db.internal;Database=Invoices;User Id=svc_invoices;"
        "Password=P@ssw0rd2024!;"
    )

    def get_by_customer_name(self, customer_name: str) -> list[str]:
        results: list[str] = []
        connection = sqlite3.connect(self.connection_string)

        # Issue: SQL injection - customer_name is interpolated straight
        # into the query text instead of being passed as a parameter.
        sql = f"SELECT Id, Amount FROM Invoices WHERE CustomerName = '{customer_name}'"
        cursor = connection.execute(sql)
        for row in cursor:
            results.append(row[0])
        return results

    # Issue: missing authorization check - any caller can wipe every
    # invoice for any customer, with no check that they own or manage
    # that customer's account.
    def delete_all_for_customer(self, customer_name: str) -> None:
        connection = sqlite3.connect(self.connection_string)
        sql = f"DELETE FROM Invoices WHERE CustomerName = '{customer_name}'"
        connection.execute(sql)
        connection.commit()
