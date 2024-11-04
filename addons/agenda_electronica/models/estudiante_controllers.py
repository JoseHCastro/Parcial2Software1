# agenda_electronica/controllers/estudiante_controller.py
from odoo import http
from odoo.http import request

class EstudianteController(http.Controller):
    @http.route('/api/estudiantes', auth='public', methods=['GET'], type='json')
    def get_estudiantes(self, **kwargs):
        estudiantes = request.env['agenda.estudiante'].sudo().search([])
        data = []
        for estudiante in estudiantes:
            data.append({
                'id': estudiante.id,
                'name': estudiante.name,
                'apellido': estudiante.apellido,
                'edad': estudiante.edad,
                'grado': estudiante.grado,
                'email': estudiante.email,
            })
        return data
