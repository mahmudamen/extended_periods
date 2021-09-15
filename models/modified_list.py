from odoo import fields, models, api


class ModifiedlIST(models.Model):
    _name = 'extend.modifiedlist'
    _description = 'modified expiration date LIST '

    name = fields.Date(string='modified expiration date')
