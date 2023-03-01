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
        'views/snippet_view.xml',
        'views/recently_viewed.xml',
    ],
    'assets': {
       'web.assets_frontend': [
           'web_recently_viewed_product/static/src/xml/snippet_template.xml',
           'web_recently_viewed_product/static/src/js/dynamic.js',
           'web_recently_viewed_product/static/src/css/snippet_template.scss',
       ],
}
}