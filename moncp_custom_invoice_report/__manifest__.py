{
    'name': 'MONCP Custom Invoice',
    'description': 'MONCP Customized Printed Tax Invoice',
    'version': '16.0.2.0.9',
    'category': 'Accounting/Accounting',
    'summary': """MONCP Customized Printed Tax Invoice""",
    'author': 'Mina Samir Wahib',
    'website': "https://www.qs-solutions.com",
    'company': 'Quick Services Solutions',
    'maintainer': 'Quick Services Solutions',
    'depends': ['base', 'account', 'sale',],
    'data': [
        'report/report_moncp_invoice.xml'
    ],
    'license': 'LGPL-3',
    'installable': True,
    'auto_install': False,
    'application': True,
}
