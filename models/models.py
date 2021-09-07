# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class extended_periods(models.Model):
#     _name = 'extended_periods.extended_periods'
#     _description = 'extended_periods.extended_periods'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
