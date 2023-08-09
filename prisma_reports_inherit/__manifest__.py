{
    'name': 'Prisma Reports',
    'version': '13.0.1.0.0',
    'category': 'Extra Tools',
    'summary': 'Module for manging the prisma reports',
    'sequence': '-100',
    'license': 'AGPL-3',
    'author': 'Odoo Mates',
    'Maintainer': 'Odoo Mates',
    'website': 'odoomates.com',
    'depends': [
        'purchase',
        'account',
        'bi_print_journal_entries',

    ],
    'demo': [],
    'data': [
        'reports/vendor_address_inherit.xml',
        'reports/payment_voucher.xml',
        'reports/journal_voucher.xml',
        'views/cheque_field.xml',
    ],
    'installable': True,
    'application': True,
    'auto install': False,
}
