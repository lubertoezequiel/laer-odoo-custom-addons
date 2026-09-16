# -*- coding: utf-8 -*-
from odoo import fields, models


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    laer_show_exchange_rate = fields.Boolean(
        string="Mostrar T.C. en PDF",
        help="Si está tildado, el PDF de la cotización/orden de venta muestra "
             "el tipo de cambio usado.",
    )
