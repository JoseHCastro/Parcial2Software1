# agenda_electronica/__manifest__.py

{
    'name': 'Agenda Electrónica',
    'version': '1.0',
    'category': 'Custom',
    'summary': 'Agenda para estudiantes',
    'description': 'Módulo de agenda electrónica con gestión de estudiantes',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',        
        'views/professor_views.xml',
        'views/parent_views.xml',
        'views/student_views.xml',
        'views/classroom_views.xml',
        'views/subject_views.xml',
        'views/schedule_views.xml',
        'views/announcement_type_views.xml',
        'views/menu_views.xml',
    ],
    'installable': True,
    'application': True,
}
