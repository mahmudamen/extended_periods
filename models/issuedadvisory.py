from odoo import fields, models, api


class IssuedByTheCommitteeToTheAdvisory(models.Model):
    _name = 'extend.issuedadvisory'
    _description = 'Issued By The Committee To The Advisory'

    name = fields.Date(string='Issued By The Committee To The Advisory')
