from odoo import models, fields

class Subject(models.Model):
    _name = 'school.subject'
    _description = 'Subject'

    name = fields.Char(string='Subject Name', required=True)
    
    # Agregamos un campo display_name
    display_name = fields.Char(compute='_compute_display_name', store=True)

    def _compute_display_name(self):
        for record in self:
            record.display_name = record.name
