# -*- coding: utf-8 -*-

from odoo import models, fields, api


class StageSponsor(models.Model):
    _name = 'stage.sponsor'
    _description = 'Estado de patrosinador'

    sequence = fields.Integer(default=1)
    name = fields.Char(
        string="Nombre"
    )