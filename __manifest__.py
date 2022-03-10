# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'account_analytic_default',
    'version' : '1.1',
    'summary': 'account_analytic_default from Odoo 14 to 13',
    'sequence': 10,
    'description': "",
    'category': 'Accounting/Accounting',
    'depends' : ['account'],
    'data': [
        'views/account_analytic_default_view.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False
}
