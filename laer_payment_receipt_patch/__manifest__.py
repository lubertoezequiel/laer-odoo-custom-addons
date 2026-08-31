# -*- coding: utf-8 -*-
{
    'name': 'Laer - Recibo de Pago Compacto',
    'version': '19.0.1.0.0',
    'category': 'Technical',
    'summary': 'Tabla única de valores/retenciones e importe total en el recibo de pago',
    'description': """
        Reemplaza las tablas nativas separadas de cheques y retenciones del
        Recibo de Pago por una única tabla estilo planilla (Forma de Pago,
        Referencia, Banco, Fecha, Importe), con subtotales de Valores,
        Retenciones y Monto Abonado alineados a la derecha.
    """,
    'author': 'Laer Technology Group',
    'website': 'https://laertechnology.com/',
    'depends': [
        'account',
        'l10n_ar_withholding',
    ],
    'data': [
        'views/report_payment_receipt.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
    'license': 'LGPL-3',
}
