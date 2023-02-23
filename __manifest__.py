{
    'name': 'Recently Viewed Product',
    'version': '16.0.1.0.0',
    'sequence': '-6',
    'category': 'website',
    'summary': 'Show Recently Viewed Product',
    'description': 'Show Recently Viewed Product',

    'installation': True,

    'depends': ['base', 'website'],
    'data': [
        # 'security/ir.model.access.csv',
        'views/snippet_template.xml',
        # 'views/supplier_products.xml',
    ],
    'assets': {
       'web.assets_frontend': [
           '/web_recently_viewed_product/static/src/js/dynamic.js',
       ],
}
}