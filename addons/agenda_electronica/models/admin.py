from odoo import models, fields

class Admin(models.Model):
    _name = 'school.admin'
    _description = 'Admin'

    name = fields.Char(string='Name', required=True)
    email = fields.Char(string='Email')
    password = fields.Char('Password')
    user_id = fields.Many2one('res.users', string='User', ondelete='cascade')

    # Opcional: para crear automáticamente un usuario al crear un admin
    def create_user_for_admin(self):
        password = self.password or '12345678'
        user_vals = {
            'name': self.name,
            'login': self.email,
            'password': password,  # Cambiar luego o pedir al usuario que restablezca
            'admin_id': self.id
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
