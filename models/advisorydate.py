from odoo import fields, models, api


class AdvisoryDate(models.Model):
    _name = 'extend.advisorydate'
    _description = 'advisory opinion issue date'

    name = fields.Date(string='advisory opinion issue date')
