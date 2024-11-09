from odoo import models, fields

class Parent(models.Model):
    _name = 'school.parent'
    _description = 'Parent'

    name = fields.Char(string='Name', required=True)
    email = fields.Char(string='Email')
    password = fields.Char('Password')
    user_id = fields.Many2one('res.users', string='User', ondelete='cascade')
    student_ids = fields.One2many('school.student', 'parent_id', string='Children')

    def create_user_for_parent(self):
        password = self.password or '12345678'
        user_vals = {
            'name': self.name,
            'login': self.email,
            'password': password,  # Cambiar luego o pedir al usuario que restablezca
            'parent_id': self.id
        }
        self.user_id = self.env['res.users'].create(user_vals)
