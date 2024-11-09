from odoo import models, fields

class AnnouncementType(models.Model):
    _name = 'school.announcement_type'  # Asegúrate de que coincida con lo que usas en las vistas
    _description = 'Announcement Type'

    type = fields.Char(string='Type', required=True)
    description = fields.Text(string='Description')
