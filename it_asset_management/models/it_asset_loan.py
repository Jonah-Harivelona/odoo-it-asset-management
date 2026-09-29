from odoo.exceptions import UserError, ValidationError

from odoo import models, fields, api


class ItAssetLoan(models.Model):
    _name = 'it.asset.loan'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Prêt d'équipement IT"
    _order = 'date_loan desc'

    equipment_id = fields.Many2one(
        'maintenance.equipment', string="Équipement",
        required=True, tracking=True,
    )
    employee_id = fields.Many2one(
        'hr.employee', string="Employé",
        required=True, tracking=True,
    )
    date_loan = fields.Date(
        string="Date de prêt",
        default=fields.Date.context_today,
        required=True, tracking=True,
    )
    date_return_expected = fields.Date(string="Retour prévu")
    date_return_actual = fields.Date(string="Retour effectif", tracking=True)
    state = fields.Selection(
        selection=[
            ('ongoing', "En cours"),
            ('returned', "Retourné"),
        ],
        string="Statut", default='ongoing', tracking=True,
    )
    notes = fields.Text(string="Notes")
    
    @api.constrains('equipment_id', 'state')
    def _check_equipment_availability(self):
        for loan in self:
            if loan.state == 'ongoing' and loan.equipment_id.asset_status != 'available':
                raise ValidationError(
                    "Impossible de prêter « %s » : son statut actuel est « %s ». "
                    "Seul un équipement « Disponible » peut être prêté."
                    % (loan.equipment_id.name, loan.equipment_id.asset_status)
                )

    @api.model_create_multi
    def create(self, vals_list):
        loans = super().create(vals_list)
        for loan in loans:
            loan.equipment_id.asset_status = 'assigned'
        return loans

    def action_return(self):
        for loan in self:
            loan.write({
                'state': 'returned',
                'date_return_actual': fields.Date.context_today(loan),
            })
            loan.equipment_id.asset_status = 'available'