import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

export interface Invoice {
  id: string;
  customerName: string;
  amount: number;
  status: string;
  createdAt: string;
  approvedBy?: string;
  decisionNote?: string;
}

const API_BASE = 'http://localhost:5000/api';

@Injectable({ providedIn: 'root' })
export class InvoiceService {
  constructor(private http: HttpClient) {}

  getAll(): Observable<Invoice[]> {
    return this.http.get<Invoice[]>(`${API_BASE}/invoices`);
  }

  create(invoice: Partial<Invoice>): Observable<Invoice> {
    return this.http.post<Invoice>(`${API_BASE}/invoices`, invoice);
  }

  approve(invoiceId: string, approvedBy: string): Observable<Invoice> {
    return this.http.post<Invoice>(`${API_BASE}/approvals/${invoiceId}/approve`, { approvedBy });
  }

  reject(invoiceId: string, approvedBy: string, reason: string): Observable<Invoice> {
    return this.http.post<Invoice>(`${API_BASE}/approvals/${invoiceId}/reject`, { approvedBy, reason });
  }

  // TODO (Session 1, Demo 5): add exportCsv() once the API endpoint exists.
}
