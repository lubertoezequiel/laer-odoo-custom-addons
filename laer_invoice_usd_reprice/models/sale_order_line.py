# -*- coding: utf-8 -*-
from odoo import fields, models


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    def _reset_price_unit(self):
        # Al agregar una linea (o cambiar producto/cantidad) con un T.C. USD
        # cargado en la orden, el precio de las lineas vinculadas a una lista
        # en dolares se calcula como precio USD x T.C. de la orden, igual que
        # el boton "Recalcular con T.C. USD". Sin esto, la linea nueva tomaba
        # la conversion de la tabla de cotizaciones del sistema y quedaba
        # inconsistente con el resto de la orden.
        # Este metodo solo lo llama _compute_price_unit despues de sus
        # protecciones (precio tipeado a mano, linea ya facturada), asi que
        # esas se respetan igual que siempre.
        self.ensure_one()
        order = self.order_id
        if order.laer_tc_manual and order.state != 'cancel' and not order.locked:
            usd_price = self._laer_get_usd_reference_price()
            if usd_price:
                price_unit = usd_price * order.laer_tc_manual
                self.update({
                    'price_unit': price_unit,
                    'technical_price_unit': price_unit,
                })
                return
        return super()._reset_price_unit()

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
