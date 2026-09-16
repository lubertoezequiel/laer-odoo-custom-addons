# -*- coding: utf-8 -*-
from odoo import fields, models


class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    def _laer_get_usd_reference_price(self):
        """Precio en USD de esta linea, segun la lista de precios de la
        orden de venta que la origino. Devuelve 0.0 si no viene de una
        orden o si el producto no tiene un precio USD vinculado real
        (ver product.pricelist.laer_get_usd_linked_price)."""
        self.ensure_one()
        sale_line = self.sale_line_ids[:1]
        if not sale_line:
            return 0.0

        pricelist = sale_line.order_id.pricelist_id
        product = self.product_id
        if not pricelist or not product:
            return 0.0

        date = self.move_id.invoice_date or self.move_id.date or fields.Date.context_today(self)
        qty = self.quantity or 1.0

        return pricelist.laer_get_usd_linked_price(product, qty, date=date)
