# -*- coding: utf-8 -*-
{
    'name': 'Laer - Reportes Compactos',
    'version': '19.0.1.0.0',
    'category': 'Technical',
    'summary': 'Encabezado compacto en todos los reportes: cotizaciones, facturas, órdenes de venta, recibos, etc.',
    'description': """
        Optimiza el espacio en todos los reportes PDF de Odoo 19:
        - Logo + info empresa + info cliente en la misma fila superior
        - Número de documento con fuente reducida (no gigante)
        - Fechas y datos secundarios más compactos
        - Más líneas de productos por página
        Aplica a: Cotizaciones, Órdenes de Venta, Facturas, Notas de Crédito,
                  Recibos, Órdenes de Compra, Albaranes/Remitos y Pagos.
    """,
    'author': 'Laer Technology Group',
    'website': 'https://laertechnology.com/',
    'depends': [
        'web',
        'account',
        'sale',
        'purchase',
        'stock',
    ],
    'data': [
        'views/report_compact_layout.xml',
    ],
    'assets': {
        'web.report_assets_common': [
            'laer_report_compact/static/src/css/compact_reports.css',
        ],
    },
    'installable': True,
    'auto_install': False,
    'application': False,
    'license': 'LGPL-3',
}
