from odoo import models, fields

class Student(models.Model):
    _name = 'school.student'
    _description = 'Student'

    name = fields.Char(string='Name', required=True)
    email = fields.Char(string='Email')
    password = fields.Char('Password')
    parent_id = fields.Many2one('school.parent', string='Parent')
    user_id = fields.Many2one('res.users', string='User', ondelete='cascade')
    
    # Relación con Classroom
    classroom_id = fields.Many2one('school.classroom', string='Classroom', domain="[('id', '!=', False)]")

    def create_user_for_student(self):
        password = self.password or '12345678'
        user_vals = {
            'name': self.name,
            'login': self.email,
            'password': password,  # Cambiar luego o pedir al usuario que restablezca
            'student_id': self.id
        }
        self.user_id = self.env['res.users'].create(user_vals)
