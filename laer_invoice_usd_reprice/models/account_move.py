# -*- coding: utf-8 -*-
from odoo import api, fields, models


class AccountMove(models.Model):
    _inherit = 'account.move'

    laer_expected_tc = fields.Float(
        string="T.C. USD esperado",
        compute='_compute_laer_expected_tc',
        digits=0,
    )
    laer_tc_manual = fields.Float(
        string="T.C. USD",
        compute='_compute_laer_tc_manual',
        store=True, readonly=False, precompute=True,
        copy=False,
        digits=0,
        help="Tipo de cambio USD usado por el boton 'Actualizar precios' "
             "para recalcular las lineas cuyo precio proviene de una lista "
             "en dolares. Se autocompleta con la cotizacion cargada para "
             "la fecha de la factura; se puede editar a mano.",
    )

    @api.depends('invoice_date', 'company_id')
    def _compute_laer_expected_tc(self):
        usd = self.env['res.currency'].search([('name', '=', 'USD')], limit=1)
        for move in self:
            if usd and move.company_id:
                move.laer_expected_tc = self.env['res.currency']._get_conversion_rate(
                    usd,
                    move.company_id.currency_id,
                    move.company_id,
                    move.invoice_date or fields.Date.context_today(move),
                )
            else:
                move.laer_expected_tc = 0.0

    @api.depends('laer_expected_tc', 'invoice_line_ids.sale_line_ids.order_id.laer_tc_manual')
    def _compute_laer_tc_manual(self):
        for move in self:
            orders = move.invoice_line_ids.sale_line_ids.order_id
            if orders:
                # Se arrastra el T.C. de la orden de venta que origino la
                # factura (si la orden nunca lo tocaron a mano, ya viene
                # con el valor de la cotizacion cargada, asi que la cadena
                # de respaldo sigue funcionando igual).
                move.laer_tc_manual = orders[:1].laer_tc_manual
            else:
                move.laer_tc_manual = move.laer_expected_tc

    def laer_action_refresh_tc(self):
        self.ensure_one()
        self.laer_tc_manual = self.laer_expected_tc

    def laer_action_update_prices_from_usd(self):
        self.ensure_one()
        if self.state != 'draft':
            return
        for line in self.invoice_line_ids:
            if line.display_type not in (False, 'product'):
                continue
            usd_price = line._laer_get_usd_reference_price()
            if usd_price:
                line.price_unit = usd_price * self.laer_tc_manual
