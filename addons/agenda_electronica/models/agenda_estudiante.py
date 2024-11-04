# agenda_electronica/models/agenda_estudiante.py

from odoo import models, fields, api
from odoo.exceptions import ValidationError

class AgendaEstudiante(models.Model):
    _name = "agenda.estudiante"
    _description = "Estudiante"

    name = fields.Char(string="Nombre", required=True)
    apellido = fields.Char(string="Apellido", required=True)  # Agregar apellido
    edad = fields.Integer(string="Edad", required=True)  # Agregar edad
    grado = fields.Char(string="Grado", required=True)  # Agregar grado
    email = fields.Char(string="Email", required=True)
    user_id = fields.Many2one("res.users", string="Usuario", default=lambda self: self.env.user)

    
    def submit_agenda_estudiante(self):
        # Aquí puedes realizar validaciones adicionales si es necesario
        for record in self:
            # Puedes agregar lógica adicional aquí si es necesario
            # Por ejemplo, si deseas comprobar que el email sea único:
            existing_student = self.search([('email', '=', record.email)], limit=1)
            if existing_student and existing_student.id != record.id:
                raise ValidationError("El email ya está registrado para otro estudiante.")

        # Si todo está correcto, se guarda el registro
        return True  # Este retorno puede ser útil para saber que se guardó correctamente

    @api.model
    def action_agenda_estudiante_cancel(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Estudiantes',
            'res_model': 'agenda.estudiante',
            'view_mode': 'tree',
            'target': 'current',
        }

    @api.model
    def create(self, vals):
        # Crear usuario automáticamente al crear un estudiante
        user_vals = {
            "name": vals["name"],
            "login": vals["email"],
            "email": vals["email"],
            "groups_id": [
                (6, 0, [self.env.ref("base.group_user").id])
            ],  # Asignar grupo de usuario básico
        }
        user = self.env["res.users"].create(user_vals)
        vals["user_id"] = user.id
        return super(AgendaEstudiante, self).create(vals)

    def unlink(self):
        # Eliminar usuario cuando se elimina el estudiante
        for record in self:
            if record.user_id:
                record.user_id.unlink()
        return super(AgendaEstudiante, self).unlink()
