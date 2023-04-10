# -*- coding: utf-8 -*-
{
    'name': "plus_one_task",

    'summary': """
             School Class
        """,

    'description': """
        School Class
    """,

    'author': "Plus One development team osama",
    'website': "https://www.PlusOne.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'learning',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/school_class.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
