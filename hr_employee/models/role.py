from odoo import api, fields, models

class Role(models.Model):
    _name = 'role'
    _description = "role records"

    name = fields.Char(string='Role', required=True)