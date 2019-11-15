from odoo import models, fields, api

class Course(models.Models):
     _name = 'openacademy.course'
     _description= "OpenAcademy Courses"
     responsible_id = fields.Many2one('res.users',
        ondelete='set null', string="Responsible", index=True)
     name = fields.Char(string="Title",reqquired=True)
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
     description = fields.Text()
