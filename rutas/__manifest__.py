# -*- coding: utf-8 -*-
{
    'name': "ruta",

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
        'views/ruta_propiedades.xml',
        'views/ruta_menus.xml',
        'security/ir.model.access.csv',
    ],

    'application': True,
    # 'installable': True,   
    # 'license': 'AGPL-3'
}
