# Copyright 2015-2016 Agile Business Group (<http://www.agilebg.com>)
# Copyright 2015 BREMSKERL-REIBBELAGWERKE EMMERLING GmbH & Co. KG
#    Author Marco Dieckhoff
# Copyright 2018 Alex Comba - Agile Business Group
# Copyright 2023 Simone Rubino - TAKOBI
# Copyright 2025 Rafnix Guzman - Popsolutions
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    "name": "Stock Move Backdating",
    "version": "16.0.0.0.1",
    "category": "Stock Logistics",
    "license": "AGPL-3",
    "author": "Marco Dieckhoff, BREMSKERL, Agile Business Group, Odoo Community Association (OCA)",
    "website": "https://github.com/OCA/stock-logistics-workflow",
    "depends": [
        "stock_account",
        "stock",
    ],
    "data": [
        "security/ir.model.access.csv",
        "wizards/fill_date_backdating.xml",
        "views/stock_inventory_views.xml",
        "views/stock_picking.xml",
        "views/stock_move_line_views.xml",
    ],
    "installable": True,
}
