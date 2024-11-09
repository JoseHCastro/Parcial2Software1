from odoo import models, fields, api

class Classroom(models.Model):
    _name = 'school.classroom'
    _description = 'Classroom'

    grade = fields.Integer(string="Grade", required=True)
    class_section = fields.Char(string="Class Section", required=True)
    
    # Relación con Students
    student_ids = fields.One2many('school.student', 'classroom_id', string='Students')

    # El campo display_name es computado
    display_name = fields.Char(compute='_compute_display_name', store=True)

    @api.depends('grade', 'class_section')
    def _compute_display_name(self):
        for record in self:
            # Combinamos el grade y class_section en display_name
            record.display_name = f"{record.grade} {record.class_section}"
