from odoo import models, fields, api

class AnnouncementUserRel(models.Model):
    _name = 'announcement_user_rel'
    _description = 'Relacion entre Anuncios y Usuarios'

    announcement_id = fields.Many2one(
        'school.announcement', 
        string='Announcement', 
        required=True,
        ondelete='cascade'  # Esto asegura que los registros se eliminen cuando se borra un anuncio
    )
    user_id = fields.Many2one(
        'res.users', 
        string='User', 
        required=True,
        ondelete='cascade'  # Esto asegura que los registros se eliminen cuando se borra un usuario
    )
    
    # El campo state de tipo string (puede estar vacío al principio)
    state = fields.Char(string="State", default=False)  # default=False asegura que empiece vacío (null)

    received = fields.Datetime(string="Received")
    sent = fields.Datetime(string="Sent")
 
    _sql_constraints = [
        ('announcement_user_unique', 'unique(announcement_id, user_id)', 'The user is already assigned to this announcement!')
    ]


    @api.model
    def create(self, vals):
        # Si el valor de 'received' no está en vals (por ejemplo, en la creación automática de la relación)
        # entonces lo asignamos a la hora actual
        if 'received' not in vals:
            vals['received'] = fields.Datetime.now()
        
        # Si 'state' no está en vals, lo dejamos vacío (default=False es equivalente a None en este caso)
        if 'state' not in vals:
            vals['state'] = 'holaa'
        
        # El campo 'sent' puede quedarse como None (null)
        return super(AnnouncementUserRel, self).create(vals)
   
