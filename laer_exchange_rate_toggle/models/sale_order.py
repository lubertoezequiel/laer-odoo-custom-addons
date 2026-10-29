# -*- coding: utf-8 -*-
from odoo import fields, models


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    laer_show_exchange_rate = fields.Boolean(
        string="Mostrar T.C. en PDF",
        help="Si está tildado, el PDF de la cotización/orden de venta muestra "
             "el tipo de cambio usado. La factura generada desde esta orden "
             "hereda este tilde (y se puede cambiar ahí mientras esté en "
             "borrador).",
    )

    def _prepare_invoice(self):
        # La factura hereda el tilde "Mostrar T.C. en PDF" de la orden, para
        # no tener que volver a marcarlo documento por documento.
        invoice_vals = super()._prepare_invoice()
        invoice_vals['laer_show_exchange_rate'] = self.laer_show_exchange_rate
        return invoice_vals
