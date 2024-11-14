from odoo import http
from odoo.http import request
import json
from datetime import date, datetime

class AnnouncementController(http.Controller):

    @http.route('/api/announcements/<int:user_id>', type='http', auth='public', methods=['GET'], csrf=False)
    def list_user_announcements(self, user_id):
        """Listar anuncios asociados a un usuario específico y sus archivos adjuntos."""
        try:
            # Buscar anuncios que tengan al usuario especificado en user_ids
            announcements = request.env['school.announcement'].sudo().search([
                ('user_ids', 'in', [user_id])
            ])

            # Construir la respuesta con los anuncios y archivos adjuntos encontrados
            announcement_list = []
            for announcement in announcements:
                # Obtener archivos adjuntos directamente desde el campo Many2many `binary_fields`
                attachment_list = [{
                    'id': attachment.id,
                    'name': attachment.name,
                    'url': f"/web/content/{attachment.id}",  # URL para descargar el archivo
                    'file_size': attachment.file_size,
                    'mimetype': attachment.mimetype
                } for attachment in announcement.binary_fields]

                # Agregar el anuncio y sus archivos adjuntos a la lista
                announcement_list.append({
                    'id': announcement.id,
                    'title': announcement.title,
                    'message': announcement.message,
                    'date': announcement.date.strftime('%Y-%m-%d') if isinstance(announcement.date, date) else None,
                    'type': announcement.type,
                    'sent': announcement.sent.strftime('%Y-%m-%d %H:%M:%S') if isinstance(announcement.sent, datetime) else None,
                    'emisor': announcement.emisor_id.name,
                    'binary_file_name': announcement.binary_file_name,
                    'attachments': attachment_list,  # Agregar los archivos adjuntos aquí
                    'user_ids': [user.id for user in announcement.user_ids],  # Lista de IDs de usuarios
                })

            # Devolver la respuesta en formato JSON
            return request.make_response(
                json.dumps({"success": True, "announcements": announcement_list}),
                headers=[('Content-Type', 'application/json')]
            )
        except Exception as e:
            return request.make_response(
                json.dumps({"success": False, "error": str(e)}),
                headers=[('Content-Type', 'application/json')]
            )
