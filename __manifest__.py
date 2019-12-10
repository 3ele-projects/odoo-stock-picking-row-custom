# -*- coding: utf-8 -*-
{
    'name': "ele-custom-tree",

    'summary': """
        Make tree row font bold if carrier_file_generated not generated. Show field in tree view""",

    'description': """
      Make tree row font bold if carrier_file_generated not generated. Show field in tree view
    """,

    'author': "3ele | Sebastian Weiss",
    'website': "https://3ele.de",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/11.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','stock','hucke_import_11'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}