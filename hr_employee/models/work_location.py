from odoo import api, fields, models

class WorkLocation(models.Model):
    _name = 'work.location'
    _description = "work location records"

    name = fields.Char(string='Work Location', required=True)
    location_type = fields.Selection([
        ('home', 'Home'),
        ('office', 'Office'),
        ('other', 'Other')
    ], string='Cover Image', required=True, default='office')
