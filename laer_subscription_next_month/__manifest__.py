# -*- coding: utf-8 -*-
{
    'name': 'Laer - Suscripciones: período del mes siguiente',
    'version': '19.0.1.0.0',
    'category': 'Sales/Subscriptions',
    'summary': 'Plan de recurrencia cuyas facturas cubren el mes calendario siguiente a la emisión',
    'description': """
        Agrega al plan de recurrencia el check "Facturar el mes siguiente".
        Las facturas de suscripciones con ese plan se emiten en su fecha
        (por ej. el día 20) pero el "Periodo facturado" de ARCA queda del
        día 1 al último día del mes siguiente. Los demás planes no cambian.

        No modifica ningún archivo del core de Odoo.
    """,
    'author': 'Laer Technology Group',
    'website': 'https://laertechnology.com/',
    'depends': ['sale_subscription', 'l10n_ar'],
    'data': ['views/sale_subscription_plan_views.xml'],
    'installable': True,
    'auto_install': False,
    'application': False,
    'license': 'LGPL-3',
}
