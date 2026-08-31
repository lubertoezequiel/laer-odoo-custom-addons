from odoo import models, fields

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    descripcion_ampliada = fields.Text(string="Descripción ampliada")
