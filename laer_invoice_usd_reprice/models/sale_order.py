# -*- coding: utf-8 -*-
from odoo import api, fields, models


class SaleOrder(models.Model):
    _inherit = 'sale.order'

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
             "en dolares. Se autocompleta con la cotización cargada para "
             "la fecha de la orden; se puede editar a mano. Este valor se "
             "arrastra a la factura que se genere desde esta orden.",
    )

    @api.depends('date_order', 'company_id')
    def _compute_laer_expected_tc(self):
        usd = self.env['res.currency'].search([('name', '=', 'USD')], limit=1)
        for order in self:
            if usd and order.company_id:
                order.laer_expected_tc = self.env['res.currency']._get_conversion_rate(
                    usd,
                    order.company_id.currency_id,
                    order.company_id,
                    order.date_order.date() if order.date_order else fields.Date.context_today(order),
                )
            else:
                order.laer_expected_tc = 0.0

    @api.depends('laer_expected_tc')
    def _compute_laer_tc_manual(self):
        for order in self:
            order.laer_tc_manual = order.laer_expected_tc

    def action_confirm(self):
        # Confirmar la orden actualiza date_order a la fecha/hora actual
        # (ver sale_order.py, _prepare_confirmation_values). Como
        # laer_tc_manual depende (via laer_expected_tc) de date_order, ese
        # cambio dispara un recalculo que pisaria el T.C. cargado a mano.
        # Se protege el campo durante la confirmacion, igual que Odoo ya
        # hace con invoice_currency_rate en un caso parecido.
        with self.env.protecting([self._fields['laer_tc_manual']], self):
            return super().action_confirm()

    def laer_action_refresh_tc(self):
        self.ensure_one()
        self.laer_tc_manual = self.laer_expected_tc

    def laer_action_update_prices_from_usd(self):
        self.ensure_one()
        if self.state not in ('draft', 'sent'):
            return
        for line in self.order_line:
            if line.display_type:
                continue
            usd_price = line._laer_get_usd_reference_price()
            if usd_price:
                line.price_unit = usd_price * self.laer_tc_manual
