from odoo import fields, models, api


class ExtendedPeriodsActivity(models.Model):
    _name = 'extended.extendedperiodsactivity'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Description'

    name = fields.Char()
