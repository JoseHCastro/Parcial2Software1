from odoo import models, fields, api

class Announcement(models.Model):
    _name = 'school.announcement'
    _description = 'Announcement'

    title = fields.Char(string='Title', required=True)
    message = fields.Text(string='Message', required=True)
    audio_url = fields.Char(string='Audio URL')
    video_url = fields.Char(string='Video URL')
    image_url = fields.Char(string='Image URL')
    file_url = fields.Char(string='File URL')
    blockchain_hash = fields.Char(string='Blockchain Hash')  # Puede ser nulo
    date = fields.Date(string='Date', default=fields.Date.context_today)
    sent = fields.Datetime(string='Sent')
    
    # Relaciones
    theme_id = fields.Many2one('school.theme', string='Theme')
    type_id = fields.Many2one('school.announcement_type', string='Announcement Type', required=True)
    emisor_id = fields.Many2one('res.users', string='Emisor', default=lambda self: self.env.user, required=True)
    receiver_ids = fields.Many2many('school.student', 'announcement_user_rel', 'announcement_id', 'student_id', string='Receivers')

# class AnnouncementUser(models.Model):
#     _name = 'school.announcement_user'
#     _description = 'Announcement User'

#     announcement_id = fields.Many2one('school.announcement', string='Announcement', required=True)
#     student_id = fields.Many2one('school.student', string='Student', required=True)
#     state = fields.Selection([('received', 'Received'), ('read', 'Read')], string='State')
#     received = fields.Datetime(string='Received')
#     read = fields.Datetime(string='Read')
