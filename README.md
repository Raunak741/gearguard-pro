🛠️ GearGuard Pro: Advanced Maintenance Management

GearGuard Pro is a high-performance Odoo 19 module designed for industrial maintenance tracking. It features automated asset health scoring, a drag-and-drop repair pipeline, and real-time cost analysis.

🌟 Key Features

Asset Health Gauge: Visual health tracking that automatically updates based on repair frequency.

Smart Kanban Board: Drag-and-drop workflow (New → In Progress → Repaired → Scrap).

Automated Logic: Scraping a request automatically marks equipment as "Unusable."

Financial Tracking: Tracks estimated vs. actual repair costs across your entire asset fleet.

Social Collaboration: Built-in Odoo Chatter for team communication and task scheduling.

🚀 Beginner's Installation Guide (Step-by-Step)

  If you are new to Odoo, follow these steps to get this project running on your local machine.

1. Prerequisites->

 Ensure you have the following installed:

 Odoo 19.0 Community/Enterprise (Windows or Linux version).

 PostgreSQL: The database engine used by Odoo.

 Python 3.10+: Ensure it's added to your System Path.

2. Download the Project->

 1. Open your terminal or command prompt.

 2. Navigate to your Odoo custom addons directory.

 3. Clone this repository:

 git clone [https://github.com/Raunak741/gearguard-pro.git](https://github.com/Raunak741/gearguard-pro.git)


3. Configure Odoo to "See" the Module->

 You must tell Odoo where your new folder is located.

 1. Locate your odoo.conf file (usually in the server folder).

 2. Find the line starting with addons_path.

 3. Add the path to this folder, separated by a comma.

 Example: addons_path = C:/Program Files/Odoo/server/addons, C:/Your_Folder/gearguard-pro

 4. Restart the Odoo Service via Windows Services (services.msc) or your terminal.


4. Install the Module in the UI->

 1. Open your browser to localhost:8069 and log in.

 2. Go to Settings and scroll down to click Activate Developer Mode.

 3. Go to the Apps menu.

 4. Click Update Apps List at the top and confirm.

 5. Remove the "Apps" filter in the search bar.

 6. Search for GearGuard and click Activate.

📂 Project Structure

gearguard/
├── __init__.py            # Main entry point
├── __manifest__.py        # Module metadata and dependencies
├── models/                # Backend Python logic
│   ├── __init__.py
│   └── gearguard.py       # Asset and Request logic
├── security/              # Access rights
│   └── ir.model.access.csv
└── views/                 # Frontend XML layouts
    └── gearguard_views.xml


🛠️ Troubleshooting for Noobs

"Module Not Found": Double-check your odoo.conf path. Ensure you use forward slashes / and no extra spaces.

"Invalid View Type tree": This module is optimized for Odoo 17/19. Ensure you are not running it on Odoo 16 or older.

"RPC_ERROR": This usually means a service restart is needed. Restart the Odoo service and try again.

👨‍💻 Author

TEAM_CLASHES->
1. RAUNAK KHANDELWAL
2. RAJDEEP SINGH
3. AARUSHI SHARMA
4. HIRAL TIWARI
