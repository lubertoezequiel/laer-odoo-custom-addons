from dateutil.relativedelta import relativedelta

from odoo import fields, models


class AccountMove(models.Model):
    _inherit = 'account.move'

    def _laer_is_next_month_subscription(self):
        self.ensure_one()
        plans = self.invoice_line_ids.sale_line_ids.order_id.plan_id
        return bool(plans) and all(plans.mapped('laer_bill_next_month'))

    def _laer_set_next_month_period(self):
        """Período de servicio = mes calendario siguiente a la emisión, solo si
        está vacío y la factura viene de un plan 'Facturar el mes siguiente'."""
        for move in self.filtered(lambda m: m.move_type == 'out_invoice' and m.state == 'draft'):
            if move.l10n_ar_afip_service_start or move.l10n_ar_afip_service_end:
                continue
            if not move._laer_is_next_month_subscription():
                continue
            base = move.invoice_date or fields.Date.context_today(move)
            start = base + relativedelta(day=1, months=1)
            move.write({
                'l10n_ar_afip_service_start': start,
                'l10n_ar_afip_service_end': start + relativedelta(day=31),
            })

    def _post(self, soft=True):
        # Antes de super: l10n_ar solo completa el período si está vacío.
        self._laer_set_next_month_period()
        return super()._post(soft=soft)
