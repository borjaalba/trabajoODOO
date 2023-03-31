# -*- coding: utf-8 -*-
{
    'name': "Ruta de entrega",

    'summary': """
        Módulo para la gestión de rutas de entrega""",

    'description': """
        Módulo para la gestión de rutas de entrega
    """,

    'author': "Grupo SIE",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Sales',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/menu.xml',
        'views/route.xml',
        'views/config.xml',
        'views/menu2.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],

    'application': True,
    'license': 'LGPL-3'
}
