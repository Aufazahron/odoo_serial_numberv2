from odoo import models, fields

class SerialNumberConfig(models.Model):
    _name = 'serial.number.config'
    _description = 'Serial Number Configuration'

    name = fields.Char("Prefix", required=True)
    serial_list = fields.One2many('serial.number.tracking', 'config_id', string="Used Serial Numbers")

class SerialNumberTracking(models.Model):
    _name = 'serial.number.tracking'
    _description = 'Serial Number Tracking'

    config_id = fields.Many2one('serial.number.config', string="Configuration")
    serial_number = fields.Char("Serial Number", required=True, unique=True)
    reference = fields.Reference([('mrp.production', 'Manufacturing Order'), 
                                  ('stock.picking', 'Delivery Order'), 
                                  ('repair.order', 'Repair Order')],
                                 string="Tracking Reference")
