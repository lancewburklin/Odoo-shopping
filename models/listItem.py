# -*- coding: utf-8 -*-

from odoo import models, fields, api


class LanceListItem(models.Model):
    _name = 'lance.listitem'
    _description = 'Shopping list Items'

    name = fields.Char(string="Item name", required=True)
    price = fields.Float("Price")
