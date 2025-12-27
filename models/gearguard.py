from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class GearEquipment(models.Model):
    _name = 'gearguard.equipment'
    _description = 'Equipment Asset'
    _inherit = ['mail.thread', 'mail.activity.mixin'] # Adds chatter for hackathon "collaboration" points

    name = fields.Char(string='Name', required=True, tracking=True)
    serial_no = fields.Char(string='Serial Number', copy=False)
    department = fields.Char(string='Department')
    team_id = fields.Many2one('gearguard.team', string='Maintenance Team')
    technician_id = fields.Many2one('res.users', string='Lead Technician', tracking=True)
    
    is_usable = fields.Boolean(string='Is Usable', default=True, tracking=True)
    health_score = fields.Float(compute='_compute_health_score', string='Health Score (%)')
    
    maintenance_count = fields.Integer(compute='_count_requests', string='Maintenance Count')
    total_cost = fields.Float(compute='_compute_total_cost', string='Total Repair Cost')

    @api.depends('is_usable')
    def _compute_health_score(self):
        """ Calculate health based on maintenance frequency (Hackathon logic) """
        for rec in self:
            requests = self.env['gearguard.request'].search_count([('equipment_id', '=', rec.id)])
            base_health = 100.0
            penalty = requests * 10.0 # Each repair drops health by 10%
            rec.health_score = max(0, base_health - penalty) if rec.is_usable else 0.0

    def _count_requests(self):
        for rec in self:
            rec.maintenance_count = self.env['gearguard.request'].search_count([('equipment_id', '=', rec.id)])

    @api.depends('maintenance_count')
    def _compute_total_cost(self):
        for rec in self:
            requests = self.env['gearguard.request'].search([('equipment_id', '=', rec.id)])
            rec.total_cost = sum(requests.mapped('actual_cost'))

    def action_view_maintenance(self):
        return {
            'name': _('Maintenance Requests'),
            'type': 'ir.actions.act_window',
            'res_model': 'gearguard.request',
            'view_mode': 'kanban,list,form',
            'domain': [('equipment_id', '=', self.id)],
            'context': {'default_equipment_id': self.id},
        }

class GearTeam(models.Model):
    _name = 'gearguard.team'
    _description = 'Maintenance Team'
    name = fields.Char(string='Team Name', required=True)
    member_ids = fields.Many2many('res.users', string='Team Members')
    active = fields.Boolean(default=True)

class GearRequest(models.Model):
    _name = 'gearguard.request'
    _description = 'Maintenance Request'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Subject', required=True, tracking=True)
    equipment_id = fields.Many2one('gearguard.equipment', string='Equipment', required=True)
    team_id = fields.Many2one('gearguard.team', string='Team')
    technician_id = fields.Many2one('res.users', string='Technician', tracking=True)
    
    priority = fields.Selection([
        ('0', 'Low'), 
        ('1', 'Normal'), 
        ('2', 'High'), 
        ('3', 'Critical')
    ], string='Priority', default='1', tracking=True)
    
    stage = fields.Selection([
        ('new', 'New'), 
        ('progress', 'In Progress'), 
        ('repaired', 'Repaired'), 
        ('scrap', 'Scrap')
    ], string="Stage", default='new', group_expand='_read_group_stage_ids', tracking=True)

    request_date = fields.Date(string='Request Date', default=fields.Date.today)
    expected_cost = fields.Float(string='Estimated Cost')
    actual_cost = fields.Float(string='Actual Cost', tracking=True)

    def _read_group_stage_ids(self, stages, domain):
        return ['new', 'progress', 'repaired', 'scrap']

    @api.onchange('equipment_id')
    def _onchange_equipment(self):
        if self.equipment_id:
            self.team_id = self.equipment_id.team_id
            self.technician_id = self.equipment_id.technician_id

    def write(self, vals):
        if vals.get('stage') == 'scrap':
            for record in self:
                if record.equipment_id:
                    record.equipment_id.is_usable = False
        
        # If moved back from scrap to repaired, mark usable again
        if vals.get('stage') == 'repaired':
            for record in self:
                if record.equipment_id:
                    record.equipment_id.is_usable = True
        return super(GearRequest, self).write(vals)