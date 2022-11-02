import string
from odoo import models, fields, api


class Sponsor(models.Model):
    _name = 'sponsor'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Patrocinador'

    name = fields.Char(
        string="Nombre de la banda"
    )
    color = fields.Integer(string='Color Index')
    sequence = fields.Integer(default=10)

    stage_sponsor_id = fields.Many2one(
        'stage.sponsor',
        string='Estado patrosinador',
        index=True, tracking=True,
        store=True,
        copy=False,
        group_expand='_read_group_stage_ids',
    )
    kanban_state = fields.Selection(
        selection=[
            ("normal", "En progreso"),
            ("done", "Listo"),
            ("blocked", "Bloqueado"),
        ],
        string="Estado de kanban", tracking=True,
        store=True,       
    )
    foto0 = fields.Image(store=True)
    partner_id = fields.Many2one(
        'res.partner',
        string='Contacto de banda',
        index=True, tracking=True,
        copy=False,
    )
    band_tags_ids = fields.Many2many('band.tags', string='Etiquetas')
    active = fields.Boolean(default="1")
    partner_phone = fields.Char(
        string="Teléfono"
    )
    partner_email = fields.Char(
        string="Correo electrónico?"
    )
    sponsor_tags_ids = fields.Many2many('sponsor.tags', string='Etiquetas')

    misin = fields.Text(
        string="Misión"
    )
    visin = fields.Text(
        string="Visión"
    )
    valores = fields.Text(
        string="Valores"
    )
    informacin_genera = fields.Text(
        string="Información General"
    )
    objetivos_mercadolgicos = fields.Text(
        string="Objetivos Mercadológicos"
    )
    campaa_a_participar = fields.Text(
        string="Campaña a participar"
    )
    pblico_meta = fields.Text(
        string="Público meta"
    )
    priority = fields.Boolean()
    que_ofrece = fields.Text(
        string="Que puede ofrecer que los hace únicos"
    )

    # -------------------- FUNCTIONS --------------------------------#

    @api.onchange('partner_id')
    def _onchange_partner_id(self):
        for rec in self:
            if rec.partner_id:
                rec.partner_phone = rec.partner_id.phone
                rec.partner_email = rec.partner_id.email

    @api.model
    def _read_group_stage_ids(self,stages, domain, order):

        # perform search
        return self.env['stage.sponsor'].search([])

    #-----------------------------------------------------------------#