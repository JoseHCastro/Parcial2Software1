from odoo import http
from odoo.http import request
import requests
import json

class UserAPIController(http.Controller):
    
    @http.route('/api/authenticate', type='json', auth='public', methods=['POST'], csrf=False)
    def authenticate(self, **kwargs):
        try:
            # Obtener los datos JSON de la solicitud
            data = request.httprequest.get_json()
            email = data.get('email')
            password = data.get('password')
            
            # Verifica que los parámetros necesarios estén presentes
            if not email or not password:
                return {
                    "error": "Faltan parámetros requeridos: email y password",
                    "success": False
                }
            
            # Configura el URL de autenticación
            url = request.httprequest.host_url + 'web/session/authenticate'
            db = request.env.cr.dbname

            # Datos para autenticación en Odoo
            auth_data = {
                'jsonrpc': '2.0',
                'method': 'call',
                'params': {
                    'db': db,
                    'login': email,
                    'password': password,
                }
            }

            headers = {'Content-Type': 'application/json'}
            session_response = requests.post(url, json=auth_data, headers=headers)
            session_data = session_response.json()

            # Verificar si la autenticación fue exitosa
            if session_data.get('result') and session_response.cookies.get('session_id'):
                session_id = session_response.cookies['session_id']

                # Buscar el usuario en res_users
                user = request.env['res.users'].sudo().search([('login', '=', email)], limit=1)
                
                # Preparar datos adicionales según el rol
                role_data = {}
                
                if user.student_id:
                    role_data = {
                        "id": user.student_id.id,
                        "name": user.student_id.name,
                        "email": user.student_id.email,
                        "role": "student",
                        "classroom_id": user.student_id.classroom_id.id if user.student_id.classroom_id else None
                    }
                elif user.professor_id:
                    role_data = {
                        "id": user.professor_id.id,
                        "name": user.professor_id.name,
                        "email": user.professor_id.email,
                        "role": "professor"
                    }
                elif user.parent_id:
                    role_data = {
                        "id": user.parent_id.id,
                        "name": user.parent_id.name,
                        "email": user.parent_id.email,
                        "role": "parent",
                        "children_ids": [child.id for child in user.parent_id.student_ids]
                    }
                elif hasattr(user, 'admin_id') and user.admin_id:
                    role_data = {
                        "id": user.admin_id.id,
                        "name": user.admin_id.name,
                        "email": user.admin_id.email,
                        "role": "admin"
                    }
                
                # Estructura de la respuesta de datos de autenticación
                response_data = {
                    "success": True,
                    "message": "Autenticación exitosa",
                    "data": {
                        "user_id": user.id,
                        "user_name": user.name,
                        "user_email": user.login,
                        "session_id": session_id,
                        **role_data
                    }
                }
                return response_data
            else:
                error_message = session_data.get('error', {}).get('message', 'Error desconocido')
                return {
                    "error": "Error de autenticación",
                    "details": error_message,
                    "success": False
                }
        except Exception as e:
            return {
                "error": "Error Interno del Servidor",
                "message": str(e),
                "success": False
            }
