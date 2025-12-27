{
    'name': 'GearGuard',
    'version': '1.1',
    'author': 'TEAM_CLASHES',
    'category': 'Manufacturing/Maintenance',
    'summary': 'Advanced Equipment Maintenance and Asset Health Tracking',
    'description': """
GearGuard Maintenance Pro
========================
A comprehensive solution for tracking industrial equipment assets, 
managing maintenance teams, and automating repair workflows.

Key Features:
-------------
* Asset Health Scoring & Gauges
* Kanban Repair Pipeline
* Maintenance Team Management
* Cost Tracking & Analysis
* Automated Scrap Logic
    """,
    'depends': ['base', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'views/gearguard_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}