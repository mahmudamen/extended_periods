# -*- coding: utf-8 -*-
{
    'name': "extended_periods",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "nuca",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'erp',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base' ,'mail'],

    # always loaded
    'data': [
        'data/ir_sequence_data.xml',
        'security/erp_security.xml',
        'security/ir.model.access.csv',
        'report/extended_periods_list.xml',
        'report/report.xml',
        'views/main_menu_file.xml',
        'views/extendedperiodslist.xml',
        'views/notify.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    "author": "Mahmudamen",
    "website": "https://mahmudamen.github.io/ten/",
    "installable": True,
    "application": True,
    "auto_install": False,
}
