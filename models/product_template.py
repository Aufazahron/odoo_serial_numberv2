from odoo import models, fields

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    default_prefix_id = fields.Many2one('serial.number.config', string="Default Serial Prefix")
