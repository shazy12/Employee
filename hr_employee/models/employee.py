from odoo import api, fields, models
# from odoo.odoo.exceptions import ValidationError
from odoo.exceptions  import ValidationError


class Employee(models.Model):
    _name = 'employee'
    _description = "employee records"

    name = fields.Char(string='Employee Name', required=True)
    job = fields.Char(string='Job Position')
    tag = fields.Char(string='Tags')
    mobile = fields.Char(string='Work Mobile', required=True)
    phone = fields.Char(string='Work Phone')
    email = fields.Char(string='Work Email')
    department = fields.Many2one('department', string='Department')
    manager = fields.Many2one('employee', string='Manager')
    coach = fields.Many2one('employee', string='Coach')
    cnic = fields.Char(string="CNIC", size=13, required=True, unique=True)
    job_id = fields.Many2one('job', string='Job Position')
    image = fields.Binary(string='Image', attachment=True, widget="image", help="Upload an image")
    work_notes = fields.Text(string="Work Information")
    private_notes = fields.Text(string="Private Information")
    hr_setting_notes = fields.Text(string="HR Setting")
    address_id = fields.Many2one('res.partner', string='Work Address', help="Employee's Work Address")
    work_location_id = fields.Many2one('work.location', string='Work Location', help="Employee's Work Location")
    timesheet = fields.Many2one('employee', string='Timesheet')
    tz = fields.Selection([
        ('asia', 'Asia'),
        ('america', 'America'),
        ('africa', 'AFrica')
    ], string='Timezone', required=True, default='asia')
    working_hours = fields.Many2one('calender', string='Working Hours')
    role = fields.Many2many('role', string='Roles')
    default_role = fields.Many2one('role', string='Default Role')





    @api.depends('address_id')
    def _compute_employee_address(self):
        for employee in self:
            if employee.address_id:
                employee.address = employee.address_id.contact_address
            else:
                employee.address = ''

    address = fields.Text(string="Address", compute="_compute_employee_address")


    @api.constrains('cnic')
    def _check_cnic_length(self):
        for record in self:
            if record.cnic and len(record.cnic) != 13:
                raise ValidationError("CNIC must be exactly 13 characters.")

        # Define your create_employee function

    # def create_employee(self):
    #     new_employee_data = {
    #         'name': 'qwef',
    #         'job': 'xyz',
    #         'tag': '123',
    #         "mobile": '0987',
    #         "phone": '1234',
    #         "email": 'xyz@gmail.com',
    #         # "department": 1,  # Replace with the actual department ID
    #         # "manager": 1,  # Replace with the actual manager ID
    #         # "coach": 1,  # Replace with the actual coach ID
    #         # "job_id": 1,  # Replace with the actual job ID
    #         "cnic": 'abc1234567890',
    #     }
    #     employee = self.create(new_employee_data)
    #     return employee