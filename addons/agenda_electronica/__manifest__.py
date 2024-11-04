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
        'views/agenda_estudiante_views.xml',
    ],
    'installable': True,
    'application': True,
}
