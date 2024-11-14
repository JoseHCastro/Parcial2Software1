from odoo import models, fields, api

class AnnouncementUserRel(models.Model):
    _name = 'announcement_user_rel'
    _description = 'Relacion entre Anuncios y Usuarios'
    _rec_name = 'announcement_id'
    _auto = True  # Permite a Odoo crear la tabla automáticamente

    announcement_id = fields.Many2one(
        'school.announcement', 
        string='Announcement', 
        required=True,
        ondelete='cascade'
    )
    user_id = fields.Many2one(
        'res.users', 
        string='User', 
        required=True,
        ondelete='cascade'
    )

    state = fields.Char(string="State", default=False)
    received = fields.Datetime(string="Received")
    sent = fields.Datetime(string="Sent")

    _sql_constraints = [
        ('announcement_user_unique', 'unique(announcement_id, user_id)', 'The user is already assigned to this announcement!')
    ]

    @api.model
    def create(self, vals):
        if 'received' not in vals:
            vals['received'] = fields.Datetime.now()
        if 'state' not in vals:
            vals['state'] = 'holaa'
        return super(AnnouncementUserRel, self).create(vals)
