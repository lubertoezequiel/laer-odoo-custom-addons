# -*- coding: utf-8 -*-
from odoo import fields, models


class AccountMove(models.Model):
    _inherit = 'account.move'

    laer_show_exchange_rate = fields.Boolean(
        string="Mostrar T.C. en PDF",
        help="Si está tildado, el PDF de la factura muestra el tipo de "
             "cambio usado. Editable solo mientras la factura está en "
             "borrador.",
    )
