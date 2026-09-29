from fastapi.testclient import TestClient

from app.main import app


def test_invoice_and_approval_routes_preserve_the_existing_contract() -> None:
    client = TestClient(app)

    listed = client.get("/api/invoices")
    assert listed.status_code == 200
    assert [invoice["id"] for invoice in listed.json()] == [
        "INV-1001",
        "INV-1002",
        "INV-1003",
        "INV-1004",
    ]
    assert listed.json()[0]["status"] == "PendingApproval"

    created = client.post(
        "/api/invoices",
        json={"id": "INV-2001", "customerName": "Verification School", "amount": 99.5},
    )
    assert created.status_code == 201
    assert created.headers["location"] == "http://testserver/api/invoices/INV-2001"
    assert created.json()["status"] == "PendingApproval"

    approved = client.post(
        "/api/approvals/INV-2001/approve", json={"approvedBy": "demo.approver"}
    )
    assert approved.status_code == 200
    assert approved.json()["approvedBy"] == "demo.approver"

    rejected = client.post(
        "/api/approvals/INV-1002/reject",
        json={"approvedBy": "demo.approver", "reason": "Verification"},
    )
    assert rejected.status_code == 200
    assert rejected.json()["decisionNote"] == "Verification"

    assert client.get("/api/invoices/does-not-exist").status_code == 404
