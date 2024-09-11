{
    'name': "Real Estate",
    'version': '1.0',
    'depends': ['base'],
    'author': "Tomas Richtarik",
    'category': 'Real Estate',
    'description': """
        A module to manage real estate properties and offers.
    """,
    'installable': True,
    'application': True,
    'data': [
        'security/ir.model.access.csv',
        'views/estate_property_views.xml',
        'views/estate_menus.xml', ],
}
