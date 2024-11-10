{
    'name': 'Custom Serial Number for Manufacturing Orders',
    'version': '1.0',
    'category': 'Manufacturing',
    'summary': 'Generate unique serial numbers based on configurable prefixes for each product',
    'author': 'Your Name',
    'depends': ['mrp', 'stock'],
    'data': [
        'views/serial_number_config_views.xml',
        'views/product_template_views.xml',
        'views/mrp_production_views.xml',
    ],
    'installable': True,
    'application': False,
}