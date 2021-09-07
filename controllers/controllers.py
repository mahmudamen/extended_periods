# -*- coding: utf-8 -*-
# from odoo import http


# class ExtendedPeriods(http.Controller):
#     @http.route('/extended_periods/extended_periods/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/extended_periods/extended_periods/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('extended_periods.listing', {
#             'root': '/extended_periods/extended_periods',
#             'objects': http.request.env['extended_periods.extended_periods'].search([]),
#         })

#     @http.route('/extended_periods/extended_periods/objects/<model("extended_periods.extended_periods"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('extended_periods.object', {
#             'object': obj
#         })
