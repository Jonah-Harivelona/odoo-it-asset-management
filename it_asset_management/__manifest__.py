{
    "name": "IT Asset Management",  
    "version": "1.0",
    'description':'IT Asset & Maintenance Management',
    'depends': ['maintenance','hr'],
    'data':[
        'security/ir.model.access.csv',
        'views/maintenance_equipment_views.xml',
        'views/it_asset_loan_views.xml'
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
    'author': 'Jonah',
}