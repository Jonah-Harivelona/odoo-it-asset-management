from datetime import timedelta
from odoo import models, fields, api

WARRANTY_ALERT_DAYS = 30

class MaintenanceEquipment(models.Model):
    _inherit = 'maintenance.equipment'

    serial_no = fields.Char(
        required=True,
    )

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

    warranty_status = fields.Selection(
        selection=[
            ("none", "Aucune garantie"),
            ("valid", "Sous garantie"),
            ("expiring_soon", "Expire bientôt"),
            ("expired", "Garantie expirée"),
        ],
        string="Statut garantie",
        compute="_compute_warranty_status",
        store=True,
    )

    @api.depends('warranty_date')
    def _compute_warranty_status(self):
        today = fields.Date.context_today(self)
        alert_limit = today + timedelta(days=WARRANTY_ALERT_DAYS)
        for equipment in self:
            if not equipment.warranty_date:
                equipment.warranty_status = 'none'
            elif equipment.warranty_date < today:
                equipment.warranty_status = 'expired'
            elif equipment.warranty_date <= alert_limit:
                equipment.warranty_status = 'expiring_soon'
            else:
                equipment.warranty_status = 'valid'

    def _cron_warranty_expiration_alert(self):
        equipments = self.search([
            ('warranty_status', '=', 'expiring_soon'),
        ])
        for equipment in equipments:
            already_notified = self.env['mail.activity'].search_count([
                ('res_model', '=', 'maintenance.equipment'),
                ('res_id', '=', equipment.id),
                ('summary', '=', "Garantie bientôt expirée"),
            ])
            if already_notified:
                continue
            equipment.activity_schedule(
                summary="Garantie bientôt expirée",
                note="La garantie de cet équipement expire le %s." % equipment.warranty_date,
                date_deadline=equipment.warranty_date,
                user_id=equipment.technician_user_id.id or self.env.uid,
            )