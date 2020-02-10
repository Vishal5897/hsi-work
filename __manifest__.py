{
    "name": "FeesCollection",
    "version": "1.0",
    "depends": ["web", "base", "web_dashboard","portal"],
    "data": [
        # "security/security_fees_collection.xml",
        "security/ir.model.access.csv",         
        "views/Institute_views.xml",
        # "views/portal.xml",
    ],
    "demo":
        [
        # "demo/institute_demo.xml",
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
