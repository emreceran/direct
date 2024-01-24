# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime



class direct(models.Model):
    _name = 'direct.yapilanislem'
    _description = 'Serviste yapılan işlemler'


    name = fields.Char()


class direct(models.Model):
    _name = 'direct.direct'
    _description = 'direct.direct'


    name = fields.Char('NIU', readonly=True, select=True, copy=False, default='New')
    musteri_isim = fields.Char()
    musteri_soyisim = fields.Char()
    adres = fields.Char()
    mail = fields.Char()
    telefon = fields.Char()

    servis_durumu = fields.Selection(
        selection=[
            ('talep', "Servis Talebi"),
            ('teslim_alındı', "Teslim Alındı"),
            # ('hazır', "Hazır"),
            ('verildi', "Kargoya Verildi"),

        ],
        string="Servis Durumu",
        readonly=True, copy=False, index=True,
        tracking=3,
        default='talep')


    img = fields.Char()
    kargo_takip_no = fields.Char()
    talep_tarih =  fields.Date(string='Talep Tarihi', default=lambda self: fields.datetime.now())
    ulasma_tarih = fields.Date()
    kargo_verilme_tarih = fields.Date()

    mail_durumu = fields.Selection(
        selection=[
            ('no_mail', "Mail Gönderilmedi"),
            # ('talep_mail', "Talep Alındı Maili Gönderildi"),
            ('ulasti_mail', "Ürün Elimize Ulaştı Maili Gönderildi"),
            ('kargo_mail', "Kargoya Verildi Maili Gönderildi"),

        ],
        string="Mail Durumu",
         copy=False, index=True,
        # readonly=True, copy=False, index=True,
        tracking=3,
        default='no_mail')

    servis_sebebi = fields.Char()

    product_id = fields.Many2one(
        comodel_name='product.product',
        string="Product",
        )

    yapilan_islem = fields.Many2one('direct.yapilanislem',
        string="Yapılan İşlem",
        )




    value = fields.Integer()
    value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text()


    def _compute_talep_traihi(self):
        for record in self:
            record.talep_tarih = fields.Date.context_today(self)

    @api.depends('value')
    def _value_pc(self):
        for record in self:
            record.value2 = float(record.value) / 100

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if 'company_id' in vals:
                self = self.with_company(vals['company_id'])
            if vals.get('name', ("New")) == ("New"):
                seq_date = fields.Datetime.context_timestamp(
                    self, fields.Datetime.to_datetime(vals['date_order'])
                ) if 'date_order' in vals else None
                vals['name'] = self.env['ir.sequence'].next_by_code(
                    'direct.direct', sequence_date=seq_date) or ("New")

        return super().create(vals_list)

