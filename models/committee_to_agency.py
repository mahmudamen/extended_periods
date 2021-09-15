from odoo import fields, models, api


class CommitteeAgency(models.Model):
    _name = 'extend.committeeagency'
    _description = 'committee issue number to agency'

    name = fields.Date(string='committee issue number to agency')
