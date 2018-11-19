# -*- coding: utf-8 -*-
{
    'name': "Customizations",

    'summary': """
         General customizations""",

    'description': """
        General customizations
    """,

    'author': "Fayez Qandeel",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'project'],

    # always loaded
    'data': [
        'data/rules.xml',
        'views/views.xml',
        'views/templates.xml',
    ],
}