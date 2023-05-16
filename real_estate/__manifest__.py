{
    "name": "Real Estate",
    "summary": "Technical Training Module",
    "description": "The real state module is create base on the Odoo 16.0 documentation",
    "author": "Vauxoo",
    "license": "LGPL-3",
    "category": "Uncategorized",
    "version": "16.0.1.0.0",
    "depends": ["base"],
    "data": [
        "security/ir.model.access.csv",
        "data/estate_menus.xml",
        "views/property_views.xml",
        "views/property_type_views.xml",
        "views/property_tag_views.xml",
        "views/property_offer_views.xml",
        "views/res_users_views.xml"
    ],
    "application": True,
    "installable": True
}
