{
    'name': 'Colombia - Punto de venta - res partner',
    'category': 'Localization',
    'version': '1.0',
    'author': '',
    'license': 'AGPL-3',
    'maintainer': ' ',
    'website': ' ',
    'summary': ' ',
    'description': """
Colombia Point of Sale:
======================
  """,
    'depends': [
        'point_of_sale',
        'l10n_co_res_partner'
       #'l10n_co_tax_extension'
    ],
    'data': [
        'views/pos_view.xml',

    ],
    'qweb': ['static/src/xml/*.xml'],
    'installable': True,
}
