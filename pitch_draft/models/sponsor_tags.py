import string
from odoo import models, fields, api


class SponsorTags(models.Model):
    _name = 'sponsor.tags'
    _description = 'Etiquetas de bandas'

    name = fields.Char(
        string="Nombre de la banda"
    )
    color = fields.Integer(string='Color Index')