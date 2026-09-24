from odoo import models, fields

class MaintenanceEquipment(models.Model):
    _inherit = 'maintenance.equipment'

    asset_status = fields.Selection(
        selection=[
            ("available", "Disponible"),
            ("assigned", "Affecté / Prêté"),
            ("maintenance", "En maintenance"),
            ("external_repair", "En réparation externe"),
            ("scrapped", "Déclassé / Mis au rebut"),
        ],
        string="Statut équipement",
        default="available",
        tracking=True,
    )
    serial_no = fields.Char(required=True)
    