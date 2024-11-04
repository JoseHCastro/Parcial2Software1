import json
from odoo import http
from odoo.http import request

class EstudianteController(http.Controller):
    @http.route('/api/estudiantes', auth='public', methods=['GET'], type='http')
    def get_estudiantes(self, **kwargs):
        estudiantes = request.env['agenda.estudiante'].sudo().search([])
        data = []
        for estudiante in estudiantes:
            data.append({
                'id': estudiante.id,
                'name': estudiante.name,
                'apellido': estudiante.apellido,  # Asegúrate de que este campo exista
                'edad': estudiante.edad,  # Asegúrate de que este campo exista
                'grado': estudiante.grado,  # Asegúrate de que este campo exista
                'email': estudiante.email,
            })
        return request.make_response(json.dumps(data), headers=[('Content-Type', 'application/json')])
