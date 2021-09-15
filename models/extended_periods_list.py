# -*- coding: utf-8 -*-
# Part of Nuca Erp create by Mahmudamen. See LICENSE file for full copyright and licensing details.

from odoo import fields, models, api , _
from datetime import datetime , timedelta
from dateutil import relativedelta
from dateutil.relativedelta import relativedelta
import time
from datetime import datetime, date, time, timedelta
from odoo.tools import date_utils
from odoo.tools import DEFAULT_SERVER_DATE_FORMAT as DATE_FORMAT, DEFAULT_SERVER_DATETIME_FORMAT as DATETIME_FORMAT

class ExtendedPeriodsList(models.Model):
    _name = 'extend.extendedperiodslist'
    _description = 'extended periods list '
    _rec_name = 'subject_id'
    _inherit = ['mail.thread']

    subject_id = fields.Many2one('res.partner', domain=[('is_subject', '=', True)], string="subject", required=True)
    entity_id = fields.Many2one('res.partner',domain=[('is_entity','=',True)],string="entity", required= True)
    new_city_id = fields.Many2one('res.partner', domain=[('is_new_city', '=', True)], string="new city", required=True)
    name = fields.Char(string='ID', readonly=True)
    agency_issue_date = fields.Many2many('extend.agencyissuedate' ,string='agency issue date')
    modified_expiration_date = fields.Many2many('extend.modifiedlist' ,string='modified expiration date')
    committee_issue_number_to_agency = fields.Many2many('extend.committeeagency' ,string='committee issue number to agency')
    advisory_opinion_issue_date = fields.Many2many('extend.advisorydate' ,string='advisory opinion issue date')
    issued_by_the_committee_to_the_advisory = fields.Many2many('extend.issuedadvisory' ,string='issued by the committee to the advisory')
    Administrator = fields.Many2one('res.users', 'Administrator')
    partner_address_id = fields.Many2one('res.partner', string="Address", )
    state = fields.Selection([('داخل','داخل'),('خارج','خارج')],string="state", defualt='داخل')
    activity_state = fields.Char(string="activity state",defualt='planned')
    date_start = fields.Date(string="Start Date", required=True, default=fields.Date.today)
    date_end = fields.Date(string="End Date", required=True, default=fields.Date.today)


    def print_report(self):
        #data = {'date_start': self.date_start, 'date_end': self.date_end}
        return self.env.ref('extended_periods.extended_periods_document_report').report_action(self)

    @api.model
    def create(self,val):
        val['name'] = self.env['ir.sequence'].next_by_code('extend.extendedperiodslist')
        result = super(ExtendedPeriodsList, self).create(val)
        msg_body = 'Object created '
        for msg in self:
            msg.message_post(body=msg_body)
        return result

    def action_active(self):
        self.state = "active"

    def action_inactive(self):
        self.state = "inactive"

    @api.onchange('entity_id')
    def _onchange_entity(self):
        '''
        The purpose of the method is to define a domain for the available
        Entity address.
        '''
        address_id = self.entity_id
        self.partner_address_id = address_id

    @api.model
    def send_notiy_agency_issue_date(self):

        #today = (datetime.now() + timedelta(days=+15)).strptime('%Y-%m-%d')

       #todays = datetime.strptime(today, '%Y-%m-%d').isocalendar()

        todays = date_utils.add(datetime.now() , days=-15)
        todayss = datetime.strftime(todays,'%Y-%m-%d')
        #todays=  ( datetime.strptime(today, '%Y-%m-%d') + relativedelta(days =+ 30).strftime('%Y-%m-%d') )
        print(todayss)
        extended = self.env['extend.extendedperiodslist']
        extended_periods_date_expire = extended.sudo().search_read([('agency_issue_date', '=', todayss)])
        print(extended_periods_date_expire)
        domain = [('agency_issue_date', '=', todayss)]
        for rec in extended_periods_date_expire:
            print(rec.get('agency_issue_date')[0])
            self.env['mail.message'].create({'message_type':"notification",
                                                 'body': 'الموضوع داخل من 15 يوم من صادر الجهاز' + ' ' + rec.get('subject_id')[1] + ' ' + rec.get('entity_id')[1],
                                                 'subject': rec.get('subject_id')[1] ,
                                                 'model': 'extend.extendedperiodslist',
                                                 'parent_id':2,
                                                  'res_id':rec.get('id'),
                                                 'subtype_id': 1,
                                                 })
            #notif_domain = [('res_partner_id', '=', 12),('is_read', '=', True),('mail_message_id','=',609)]
            #print(notif_domain)
            #notifications = self.env['mail.notification'].sudo().search(notif_domain)
            #notifications.write({'is_read': False})
            extended_periods_date_expire = self.env['mail.message'].sudo().search_read([] ,order='id desc')[0]
            print(extended_periods_date_expire['id'])
            company_info ={
                    'mail_message_id': extended_periods_date_expire['id'],
                    'is_read': False,
                    'res_partner_id': 12,
                    'notification_type':'inbox',
                    'notification_status':'sent',
                }
            self.env['mail.notification'].create(company_info)

    @api.model
    def send_notiy_committee_issue_number_to_agency(self):

        #today = (datetime.now() + timedelta(days=+15)).strptime('%Y-%m-%d')

       #todays = datetime.strptime(today, '%Y-%m-%d').isocalendar()

        todays = date_utils.add(datetime.now() , days=+21)
        todayss = datetime.strftime(todays,'%Y-%m-%d')
        #todays=  ( datetime.strptime(today, '%Y-%m-%d') + relativedelta(days =+ 30).strftime('%Y-%m-%d') )
        print(todayss)
        extended = self.env['extend.extendedperiodslist']
        extended_periods_date_expire = extended.sudo().search_read([('modified_expiration_date', '=', todayss)])
        print(extended_periods_date_expire)
        domain = [('modified_expiration_date', '=', todayss)]
        for rec in extended_periods_date_expire:
            print(rec.get('modified_expiration_date')[0])
            self.env['mail.message'].create({'message_type':"notification",
                                                 'body':  'الموضوع فاضل علي تاريخ النهو المقرر 3 اسبابيع من صادر اللجنة للجهاز' + ' ' + rec.get('subject_id')[1] + ' ' + rec.get('entity_id')[1],
                                                 'subject': rec.get('subject_id')[1],
                                                 'model': 'extend.extendedperiodslist',
                                                 'parent_id':3,
                                                 'res_id': rec.get('id'),
                                                 'subtype_id': 1,
                                                 })
            #notif_domain = [('res_partner_id', '=', 3),('is_read', '=', True),('mail_message_id','=',42)]
            #print(notif_domain)
            #notifications = self.env['mail.notification'].sudo().search(notif_domain)
            #notifications.write({'is_read': False})
            extended_periods_date_expire = self.env['mail.message'].sudo().search_read([] ,order='id desc')[0]
            print(extended_periods_date_expire)
            company_info ={
                    'mail_message_id': extended_periods_date_expire['id'],
                    'is_read': False,
                    'res_partner_id': 12,
                    'notification_type':'inbox',
                    'notification_status':'sent',
                }
            self.env['mail.notification'].create(company_info)