# -*- coding: utf-8 -*-
{
    'name': 'Laer - Orden de Venta Compacta',
    'version': '19.0.1.0.0',
    'category': 'Technical',
    'summary': 'Columnas Código/Descripción/Impuestos y tipografía compacta en el PDF de la orden de venta',
    'description': """
        Personaliza el reporte PDF de la orden de venta:
        - Título "Pro-Forma / Cotización / Orden #" según el estado del documento
        - Columnas: Código, Descripción, Cantidad, Precio Unitario, Impuestos, Importe
        - Descripción de venta del producto en lugar del nombre técnico
        - Cantidad sin unidad de medida
        - Impuestos listados por nombre
        - Tipografía más compacta en la tabla de líneas y en los totales
    """,
    'author': 'Laer Technology Group',
    'website': 'https://laertechnology.com/',
    'depends': [
        'sale',
    ],
    'data': [
        'views/report_saleorder.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
    'license': 'LGPL-3',
}
