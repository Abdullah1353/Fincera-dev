{
    'name': 'Prisma Purchase Order Print',
    'version': '13.0.1.0.0',
    'category': 'Extra Tools',
    'summary': 'Module for manging the Prisma Purchase Order Print',
    'sequence': '-10001',
    'license': 'AGPL-3',
    'author': 'Hasnain Jutt',
    'Maintainer': 'Odoo Mates',
    'website': 'odoomates.com',
    'depends': [
        'purchase',
        'purchase_request_print',
    ],
    'demo': [],
    'data': [

        'reports/po_print.xml',
    ],
    'installable': True,
    'application': True,
    'auto install': False,
}
