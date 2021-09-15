from odoo import fields, models, api


class AgencyIssueDate(models.Model):
    _name = 'extend.agencyissuedate'
    _description = 'agency issue date'

    name = fields.Date(string='agency issue date')
