{
    'name': 'Car Archive Management',
    'version': '1.0.0',
    'sequence': -100,
    'author': 'rami',
    'website': 'www.rami',.com',
    'category': 'Automotive',
    'summary': 'Car archive management system',
    'description': 'Car archive system',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/car_archive_views.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
    'license': 'LGPL-3',
}
