import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { Invoice, InvoiceService } from '../invoice.service';

// Approve/reject one invoice at a time. Session 2, Demo 8 (Spec Kit) adds
// a bulk-approve checkbox list + summary here.
@Component({
  selector: 'app-approvals',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './approvals.component.html',
})
export class ApprovalsComponent implements OnInit {
  pending: Invoice[] = [];
  currentUser = 'demo.approver';

  constructor(private invoiceService: InvoiceService) {}

  ngOnInit(): void {
    this.invoiceService.getAll().subscribe((invoices) => {
      this.pending = invoices.filter((i) => i.status === 'PendingApproval');
    });
  }

  approve(invoiceId: string): void {
    this.invoiceService.approve(invoiceId, this.currentUser).subscribe(() => {
      this.pending = this.pending.filter((i) => i.id !== invoiceId);
    });
  }

  reject(invoiceId: string): void {
    this.invoiceService.reject(invoiceId, this.currentUser, 'Rejected in demo').subscribe(() => {
      this.pending = this.pending.filter((i) => i.id !== invoiceId);
    });
  }
}
