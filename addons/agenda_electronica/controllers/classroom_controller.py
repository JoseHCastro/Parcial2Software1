from odoo import http
from odoo.http import request
import json

class ClassroomController(http.Controller):

    @http.route('/api/classrooms', type='http', auth='public', methods=['GET'], csrf=False)
    def get_classrooms(self, **kwargs):
        # Obtenemos todos los registros de Classroom
        classrooms = request.env['school.classroom'].sudo().search([])
        
        # Serializamos los datos en una lista de diccionarios
        classrooms_data = []
        for classroom in classrooms:
            classrooms_data.append({
                'id': classroom.id,
                'grade': classroom.grade,
                'class_section': classroom.class_section,
                'display_name': classroom.display_name,
                'student_ids': [student.id for student in classroom.student_ids]
            })

        # Retornamos la respuesta como JSON
        return request.make_response(json.dumps({'classrooms': classrooms_data}), headers={'Content-Type': 'application/json'})
