from odoo import models, fields


class MaintenanceRequest(models.Model):
    _inherit = 'maintenance.request'

    it_request_type = fields.Selection(
        selection=[
            ("incident", "Incident IT"),
            ("service_request", "Demande de service IT"),
        ],
        string="Type de demande IT",
        default="incident",
        tracking=True,
    )