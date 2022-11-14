import string
from odoo import models, fields, api,SUPERUSER_ID


class Band(models.Model):
    _name = 'evaluation'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Bandas'

    user_id = fields.Many2one(
        'res.users',
        string='Evaluador',
    )
    comentario = fields.Char(
        string="Comentarios"
    )
    puntacion = fields.Integer(
        string="Puntacion",
        help="la puntacion es del 1-10"
    )
    band_id = fields.Many2one(
        'band',
        string='danda',
    )

