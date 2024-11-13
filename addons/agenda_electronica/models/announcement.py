# announcement.py

from odoo import models, fields, api
from datetime import datetime

class Announcement(models.Model):
    _name = "school.announcement"
    _description = "Announcement"

    title = fields.Char(string="Title", required=True, tracking=True)
    message = fields.Text(string="Message", required=True, tracking=True)
    date = fields.Date(string="Date", required=True, tracking=True)
    type = fields.Selection(
        [
            ("announcement", "Announcement"),
            ("notice", "Notice"),
        ],
        string="Type",
        required=True,
        tracking=True,
    )
    sent = fields.Datetime(string="Sent", readonly=True, default=fields.Datetime.now)
    emisor_id = fields.Many2one(
        "res.users",
        string="Emisor",
        default=lambda self: self.env.user,
        required=True,
        tracking=True,
    )
    binary_file_name = fields.Char("Binary File Name")
    binary_fields = fields.Many2many("ir.attachment", string="Multi Files Upload")

    # Relación Many2many con los usuarios, solo para indicar a quién se enviará el anuncio
    user_ids = fields.Many2many(
        'res.users',  # Relación con el modelo de usuarios
        'announcement_user_rel',  # Nombre de la tabla intermedia
        'announcement_id',  # Campo en la tabla intermedia
        'user_id',  # Campo en la tabla intermedia
        string='Users'  # Nombre del campo para mostrarlo en la vista
    )
    

    @api.model
    def create(self, vals):
        vals['sent'] = fields.Datetime.now()  # Establece la fecha y hora de envío
        return super(Announcement, self).create(vals)
