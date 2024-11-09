from odoo import models, fields

class ResUsers(models.Model):
    _inherit = 'res.users'

    professor_id = fields.Many2one('school.professor', string='Professor')
    parent_id = fields.Many2one('school.parent', string='Parent')
    student_id = fields.Many2one('school.student', string='Student')
