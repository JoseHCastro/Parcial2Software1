from odoo import models, fields

class Professor(models.Model):
    _name = 'school.professor'
    _description = 'Professor'

    name = fields.Char(string='Name', required=True)
    email = fields.Char(string='Email')
    password = fields.Char('Password')
    user_id = fields.Many2one('res.users', string='User', ondelete='cascade')

    # Opcional: para crear automáticamente un usuario al crear un professor
    def create_user_for_professor(self):
        password = self.password or '12345678'
        user_vals = {
            'name': self.name,
            'login': self.email,
            'password': password,  # Cambiar luego o pedir al usuario que restablezca
            'professor_id': self.id
        }
        self.user_id = self.env['res.users'].create(user_vals)
