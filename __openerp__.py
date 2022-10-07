# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Reportes Contables Excel',
    'version': '10.0.0.1',
    'sequence': 4,
    'summary': 'Reportes PDF en excel',
    'category': 'Accounting',
    'description': """
    Reportes financieros en excel
    """,
    'author': 'sapex.miguel@gmail.com',
    'website': '',
    'depends': ['account'],
    'data': [
        "wizard/account_financial_report_view.xml",
    ],
    'qweb': [
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
