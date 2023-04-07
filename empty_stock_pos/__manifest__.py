# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'Empty Stock POS',
    'version' : '1.0',
    'summary': 'Empty Stock Notification POS',
    'description': """
        Empty Stock Notification POS
        Show Stock POS
    """,
    'category': 'Sales/Point of Sale',
    'website': '',
    'depends' : ['point_of_sale'],
    'assets': {
        'point_of_sale.assets': [
            'empty_stock_pos/static/src/js/Screens/ProductScreen/ProductScreen.js',
            'empty_stock_pos/static/src/xml/Screens/ProductScreen/ProductItem.xml',
        ],
    },
    'installable': True,
    'application': True,
    'sequence': 41,
    "price": 25,
    "currency": "USD",
    "images": ['static/description/thumbnail.png'],
    'license': 'LGPL-3',
}
