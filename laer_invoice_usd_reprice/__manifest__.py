# -*- coding: utf-8 -*-
{
    'name': 'Laer - Recalcular Precios por Tipo de Cambio USD',
    'version': '19.0.1.0.0',
    'category': 'Technical',
    'summary': 'Campo de tipo de cambio manual y boton para recalcular precios desde listas en USD, en la cotizacion y en la factura',
    'description': """
        Agrega, tanto a la orden de venta como a la factura (en "Otra
        informacion"):
        - Un campo "T.C. USD" que se comporta igual que el campo nativo de
          tipo de cambio de Odoo (invoice_currency_rate): se autocompleta
          con la cotizacion cargada en el sistema para la fecha del
          documento, es editable a mano, y un boton de refresco lo vuelve
          a poner en el valor automatico.
        - Un boton "Actualizar precios" (solo con el documento en borrador)
          que recorre las lineas cuya lista de precios este vinculada a
          una lista en dolares (regla tipo formula con base en otra lista,
          como ya usan DISTRIBUIDOR ARS y GREMIO ARS), y recalcula el
          precio unitario como precio_usd x T.C. Las lineas sin ese
          vinculo (precios fijos en pesos) quedan intactas.

        El T.C. de la orden de venta se arrastra automaticamente a la
        factura que se genere desde ella; si nunca se toco a mano en
        ningun lado, sigue cayendo en la cotizacion cargada en el sistema.

        Solo toca price_unit; el resto (subtotal, impuestos, asiento
        contable) lo recalcula Odoo solo, con su mecanismo normal.
    """,
    'author': 'Laer Technology Group',
    'website': 'https://laertechnology.com/',
    'depends': [
        'sale',
        'account',
        'laer_exchange_rate_toggle',
    ],
    'data': [
        'views/sale_order_views.xml',
        'views/account_move_views.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
    'license': 'LGPL-3',
}
