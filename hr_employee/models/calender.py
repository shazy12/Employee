from odoo import api, fields, models

class Calender(models.Model):
    _name = 'calender'
    _description = "calender records"

    name = fields.Char(string='Name', required=True)
    tz = fields.Selection([
        ('asia', 'Asia'),
        ('america', 'America'),
        ('africa', 'AFrica')
    ], string='Timezone', required=True, default='asia')
