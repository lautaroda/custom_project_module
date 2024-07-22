from odoo import models, fields 
class AccountMove(models.Model): 
    _inherit = 'account.move' 
    project_id = fields.Many2one('project.project', string='Proyecto') 
