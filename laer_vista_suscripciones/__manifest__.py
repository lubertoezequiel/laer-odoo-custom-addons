# -*- coding: utf-8 -*-
{
    'name': 'Laer - Vista Suscripciones (Deuda)',
    'version': '19.0.1.0.0',
    'category': 'Sales/Subscriptions',
    'summary': 'Muestra en la lista de suscripciones si el cliente tiene deuda y de cuánto es',
    'description': """
        Agrega a la lista de suscripciones (sale.order) los importes pendientes
        de cobro de las facturas generadas por la suscripción:

        - Deuda: total pendiente de las facturas publicadas no pagadas / parciales
          (netea notas de crédito), en la moneda de la compañía.
        - Deuda vencida: parte de esa deuda cuya fecha de vencimiento ya pasó.
        - Vence: fecha de vencimiento más antigua impaga.
        - Filtro "Con deuda" y agrupación, más resaltado en rojo de las vencidas.

        No modifica ningún archivo del core de Odoo.
    """,
    'author': 'Laer Technology Group',
    'website': 'https://laertechnology.com/',
    'depends': [
        'sale_subscription',
    ],
    'data': [
        'views/sale_subscription_views.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
    'license': 'LGPL-3',
}
