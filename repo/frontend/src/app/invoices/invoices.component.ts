import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { Invoice, InvoiceService } from '../invoice.service';

// Session 1 - Demo 5 target: add a "Download CSV" button to this page
// that calls the new export endpoint. No CSV button exists yet on purpose.
@Component({
  selector: 'app-invoices',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './invoices.component.html',
})
export class InvoicesComponent implements OnInit {
  invoices: Invoice[] = [];
  loading = true;

  constructor(private invoiceService: InvoiceService) {}

  ngOnInit(): void {
    this.invoiceService.getAll().subscribe((invoices) => {
      this.invoices = invoices;
      this.loading = false;
    });
  }

  // TODO (Session 1, Demo 5): downloadCsv() calling invoiceService.exportCsv()
}
