# -*- coding: utf-8 -*-

from odoo import models, fields, api


class StageBand(models.Model):
    _name = 'stage.band'
    _description = 'Etiquetas de bandas'

    sequence = fields.Integer(default=10)
    color = fields.Integer('Color Index')
    fold = fields.Boolean(default=False)
    
    name = fields.Char(
        string="Nombre"
    )

    def _get_default_band_ids(self):
        default_project_id = self.env.context.get('default_project_id')
        return None

    band_ids = fields.Many2many('band', 'stage_band_rel', tring='Projects',
        default=_get_default_band_ids,)