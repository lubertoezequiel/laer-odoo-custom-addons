from odoo import fields, models


class SaleSubscriptionPlan(models.Model):
    _inherit = 'sale.subscription.plan'

    laer_bill_next_month = fields.Boolean(
        string="Facturar el mes siguiente",
        help="Las facturas se emiten en su fecha pero el período de servicio "
             "(ARCA) es el mes calendario siguiente a la fecha de emisión.",
    )
