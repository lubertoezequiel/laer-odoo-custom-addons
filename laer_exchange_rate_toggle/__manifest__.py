# -*- coding: utf-8 -*-
{
    'name': 'Laer - Mostrar Tipo de Cambio',
    'version': '19.0.1.0.0',
    'category': 'Technical',
    'summary': 'Checkbox para mostrar el tipo de cambio en el PDF de la orden de venta y de la factura',
    'description': """
        Agrega un checkbox "Mostrar T.C. en PDF" en la orden de venta y en
        "Otra información" de la factura (editable en cualquier estado).
        Si está tildado, el PDF muestra "1 USD = X [moneda empresa]" con la
        cotización real del dólar a la fecha del documento, sin importar en
        qué moneda esté el documento en sí.

        Se ancla en la plantilla genérica de factura (account), justo
        debajo de "Importe total con letra". Como la localización
        argentina (l10n_ar) parte de esa misma plantilla base, también
        aplica a AEN S.R.L. y LAER TECHNOLOGY GROUP sin depender de l10n_ar
        directamente.
    """,
    'author': 'Laer Technology Group',
    'website': 'https://laertechnology.com/',
    'depends': [
        'sale',
        'account',
    ],
    'data': [
        'views/sale_order_views.xml',
        'views/account_move_views.xml',
        'views/report_saleorder.xml',
        'views/report_invoice.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
    'license': 'LGPL-3',
}
