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
        # Establecer una contraseña predeterminada si no se proporciona
        password = self.password or '12345678'
        
        # Crear el diccionario con los valores del usuario
        user_vals = {
            'name': self.name,
            'login': self.email,
            'password': password,  # Cambiar luego o pedir al usuario que restablezca
            'student_id': self.id
        }

        # Crear el nuevo usuario
        new_user = self.env['res.users'].create(user_vals)
        
        # Relacionar el usuario con el estudiante
        self.user_id = new_user

        # Asignar los grupos al nuevo usuario
        group_ids = [1, 2, 3, 4, 7, 8, 9]  # IDs de los grupos que deseas asignar
        groups = self.env['res.groups'].browse(group_ids)  # Obtener los grupos por sus IDs

        # Usar la relación intermedia para asignar los grupos al usuario
        new_user.write({
            'groups_id': [(4, group.id) for group in groups]  # 4 es el comando para agregar a los grupos
        })