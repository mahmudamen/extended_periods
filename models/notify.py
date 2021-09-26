# -*- coding: utf-8 -*-
# Part of Nuca Erp create by Mahmudamen. See LICENSE file for full copyright and licensing details.

from odoo import fields, models, api


class Notify(models.Model):
    _inherit = ['mail.message']
    _description = 'Notify'

