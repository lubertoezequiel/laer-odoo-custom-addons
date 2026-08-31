# -*- coding: utf-8 -*-
{
    'name': 'Laer - Factura AR: Cuenta Bancaria',
    'version': '19.0.1.0.0',
    'category': 'Technical',
    'summary': 'Muestra CUIT, Razón Social, Banco y CBU junto al QR de la factura electrónica AR',
    'description': """
        Agrega los datos bancarios de la empresa (CUIT, Razón Social, Banco,
        CBU y Número de cuenta) al lado del código QR en la factura
        electrónica argentina, sin modificar el QR ni el CAE.
    """,
    'author': 'Laer Technology Group',
    'website': 'https://laertechnology.com/',
    'depends': [
        'l10n_ar',
    ],
    'data': [
        'views/report_invoice_bank_account.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
    'license': 'LGPL-3',
}
