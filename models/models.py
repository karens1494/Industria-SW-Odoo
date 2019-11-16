# -*- coding: utf-8 -*-

from odoo import models, fields, api, partner

class Course(models.Model):
    _name = 'openacademy.course'

    name = fields.Char(string="Title", required=True)
    description = fields.Text()

    # Relaciones entre tablas
    responsible_id = fields.Many2one('res.users',
                                     ondelete='set null', string="Responsable", index=True)
    session_ids = fields.One2many(
        'openacademy.session', 'course_id', string="Sessions")

#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100
class Session(models.Model):
    _name = 'openacademy.session'
    _description = "OpenAcademy Sessions"
    
    name = fields.Char(required=True)
    start_date = fields.Date()
    duration = fields.Float(digits=(6, 2), help="Duration in days")
    seats = fields.Integer(string="Number of seats")

    instructor_id = fields.Many2one('res.partner', string="Instructor",
        domain=[('instructor', '=', True)])
    course_id = fields.Many2one('openacademy.course',
        ondelete='cascade', string="Course", required=True)
    attendee_ids = fields.Many2many('res.partner', string="Attendees")
