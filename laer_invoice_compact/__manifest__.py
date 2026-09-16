# -*- coding: utf-8 -*-
{
    'name': 'Laer - Factura Compacta',
    'version': '19.0.1.0.0',
    'category': 'Technical',
    'summary': 'Título dinámico, recuadro de cliente, columna Código y tipografía compacta en la factura',
    'description': """
        Personaliza el PDF de la factura, en línea con laer_sale_order_compact:
        - Título "# / Nota de Crédito # / Documento #" según el tipo de movimiento
        - Recuadro de cliente con borde
        - Columnas: Código, Descripción, Cant, P.Unitario, Impuestos, Importe
        - Descripción de venta del producto en lugar del nombre técnico
        - Tipografía compacta en la tabla de líneas y en los totales (11.5pt/12.5pt)

        Hereda de account.report_invoice_document (genérico, no de la
        vista específica de AR) para que se aplique a cualquier
        factura sin importar la localización fiscal de la empresa.
    """,
    'author': 'Laer Technology Group',
    'website': 'https://laertechnology.com/',
    'depends': [
        'account',
        'l10n_ar',
    ],
    'data': [
        'views/report_invoice_compact.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
    'license': 'LGPL-3',
}
