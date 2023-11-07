from odoo import api, fields, models

class Job(models.Model):
    _name = 'job'
    _description = "job records"

    name = fields.Char(string='Job Name', required=True)