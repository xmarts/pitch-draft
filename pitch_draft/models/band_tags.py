import string
from odoo import models, fields, api


class BandTags(models.Model):
    _name = 'band.tags'
    _description = 'Etiquetas de bandas'

    name = fields.Char(
        string="Nombre de la banda"
    )
    color = fields.Integer(string='Color Index')