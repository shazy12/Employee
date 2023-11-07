from odoo import api, fields, models

class Department(models.Model):
    _name = 'department'
    _description = "department records"

    name = fields.Char(string='Department Name', required=True)
    manager = fields.Many2one('employee', string='Manager')
    parent = fields.Many2one('department', string='Parent Department')