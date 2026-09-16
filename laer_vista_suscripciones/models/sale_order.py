# -*- coding: utf-8 -*-
from odoo import api, fields, models

# Facturas que representan una deuda real del cliente
_OPEN_STATES = ('not_paid', 'partial')
_CUSTOMER_MOVE_TYPES = ('out_invoice', 'out_refund')


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    company_currency_id = fields.Many2one(
        'res.currency',
        string='Moneda de la compañía',
        related='company_id.currency_id',
        store=True,
        readonly=True,
    )

    amount_invoiced_due = fields.Monetary(
        string='Deuda',
        compute='_compute_amount_invoiced_due',
        store=True,
        currency_field='company_currency_id',
        help="Total pendiente de cobro de las facturas publicadas de esta "
             "suscripción (netea notas de crédito), en moneda de la compañía.",
    )
    has_amount_due = fields.Boolean(
        string='Con deuda',
        compute='_compute_amount_invoiced_due',
        store=True,
    )
    amount_invoiced_overdue = fields.Monetary(
        string='Deuda vencida',
        compute='_compute_amount_invoiced_overdue',
        currency_field='company_currency_id',
        help="Parte de la deuda cuya fecha de vencimiento ya pasó.",
    )
    invoice_overdue_date = fields.Date(
        string='Vence',
        compute='_compute_amount_invoiced_overdue',
        help="Fecha de vencimiento más antigua de una factura impaga.",
    )

    def _get_due_invoices(self):
        """account.move de cliente, publicadas y no pagadas / parciales, ligadas a la orden."""
        self.ensure_one()
        return self.order_line.invoice_lines.move_id.filtered(
            lambda m: m.move_type in _CUSTOMER_MOVE_TYPES
            and m.state == 'posted'
            and m.payment_state in _OPEN_STATES
        )

    @api.depends(
        'order_line.invoice_lines',
        'order_line.invoice_lines.move_id.payment_state',
        'order_line.invoice_lines.move_id.state',
        'order_line.invoice_lines.move_id.amount_residual_signed',
        'company_currency_id',
    )
    def _compute_amount_invoiced_due(self):
        for order in self:
            # amount_residual_signed ya viene en moneda de la compañía y con signo
            # (+ factura pendiente, - nota de crédito pendiente).
            currency = order.company_currency_id or order.currency_id
            due = sum(order._get_due_invoices().mapped('amount_residual_signed'))
            due = currency.round(due) if currency else round(due, 2)
            order.amount_invoiced_due = due
            order.has_amount_due = (
                currency.compare_amounts(due, 0.0) > 0 if currency else due > 0.0
            )

    @api.depends(
        'order_line.invoice_lines',
        'order_line.invoice_lines.move_id.payment_state',
        'order_line.invoice_lines.move_id.state',
        'order_line.invoice_lines.move_id.amount_residual_signed',
        'order_line.invoice_lines.move_id.invoice_date_due',
        'company_currency_id',
    )
    def _compute_amount_invoiced_overdue(self):
        today = fields.Date.context_today(self)
        for order in self:
            overdue_moves = order._get_due_invoices().filtered(
                lambda m: m.invoice_date_due and m.invoice_date_due < today
            )
            currency = order.company_currency_id or order.currency_id
            overdue = sum(overdue_moves.mapped('amount_residual_signed'))
            order.amount_invoiced_overdue = currency.round(overdue) if currency else overdue
            due_dates = order._get_due_invoices().filtered('invoice_date_due').mapped('invoice_date_due')
            order.invoice_overdue_date = min(due_dates) if due_dates else False
