# -*- coding: utf-8 -*-
from odoo import models


class ProductPricelist(models.Model):
    _inherit = 'product.pricelist'

    def laer_get_usd_linked_price(self, product, qty, date=False):
        """Devuelve el precio en USD del producto segun la lista USD a la
        que esta lista (self, en pesos) esta vinculada por una regla tipo
        formula con base en otra lista (como ya usan DISTRIBUIDOR ARS ->
        DISTRIBUIDOR y GREMIO ARS -> GREMIO).

        Devuelve 0.0 si:
        - el producto tiene un precio fijo en pesos en esta lista (sin
          vinculo a ninguna lista en dolares), o
        - la lista en dolares no tiene ninguna regla especifica cargada
          para este producto (para no confiar en el valor por default de
          Odoo, que suele ser un placeholder sin sentido como 0 o 1).
        """
        self.ensure_one()
        if not self or not product:
            return 0.0

        __, rule_id = self._get_product_price_rule(product, qty, date=date)
        rule = self.env['product.pricelist.item'].browse(rule_id)
        if not (rule and rule.compute_price == 'formula' and rule.base == 'pricelist' and rule.base_pricelist_id):
            return 0.0

        usd_pricelist = rule.base_pricelist_id
        __, usd_rule_id = usd_pricelist._get_product_price_rule(product, qty, date=date)
        if not usd_rule_id:
            return 0.0

        return usd_pricelist._get_product_price(product, qty, date=date)
