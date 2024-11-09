from odoo import models, fields, api

class Schedule(models.Model):
    _name = 'school.schedule'
    _description = 'Schedule'

    # Usamos campos Float para almacenar la hora en formato decimal
    schedule_init = fields.Float(string='Schedule Start', required=True)
    schedule_end = fields.Float(string='Schedule End', required=True)

    subject_id = fields.Many2one('school.subject', string='Subject', required=True)
    classroom_id = fields.Many2one('school.classroom', string='Classroom', required=True)
    professor_id = fields.Many2one('school.professor', string='Professor', required=True)

    display_name = fields.Char(compute='_compute_display_name', store=True)

    @api.depends('schedule_init', 'schedule_end', 'subject_id', 'classroom_id', 'professor_id')
    def _compute_display_name(self):
        for record in self:
            # Convertimos el tiempo decimal a formato HH:MM
            init_hour = int(record.schedule_init)
            init_minute = int((record.schedule_init - init_hour) * 60)
            end_hour = int(record.schedule_end)
            end_minute = int((record.schedule_end - end_hour) * 60)
            record.display_name = f"{record.subject_id.name} - {record.classroom_id.display_name} ({init_hour:02}:{init_minute:02} - {end_hour:02}:{end_minute:02})"
