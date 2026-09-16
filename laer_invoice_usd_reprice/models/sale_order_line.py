# -*- coding: utf-8 -*-
from odoo import fields, models


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    def _laer_get_usd_reference_price(self):
        """Precio en USD de esta linea, segun la lista de precios de la
        propia orden. Devuelve 0.0 si el producto no tiene un precio USD
        vinculado real (ver product.pricelist.laer_get_usd_linked_price)."""
        self.ensure_one()
        pricelist = self.order_id.pricelist_id
        product = self.product_id
        if not pricelist or not product:
            return 0.0

        date = self.order_id.date_order.date() if self.order_id.date_order else fields.Date.context_today(self)
        qty = self.product_uom_qty or 1.0

        return pricelist.laer_get_usd_linked_price(product, qty, date=date)
