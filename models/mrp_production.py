from odoo import models, fields, api
from odoo.exceptions import UserError

class MrpProduction(models.Model):
    _inherit = 'mrp.production'

    @api.model
    def create_serial_number(self):
        if not self.product_id.default_prefix_id:
            raise UserError("Please configure a serial prefix for the product.")
        
        prefix = self.product_id.default_prefix_id.name
        new_serial = self.env['serial.number.tracking'].create({
            'serial_number': f"{prefix}{self.env['ir.sequence'].next_by_code('serial.number')}",
            'reference': f'mrp.production,{self.id}'
        })
        return new_serial.serial_number

    def action_confirm(self):
        for order in self:
            serial = order.create_serial_number()
            order.message_post(body=f"Serial Number {serial} generated for Manufacturing Order.")
        return super(MrpProduction, self).action_confirm()
