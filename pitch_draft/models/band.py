import string
from odoo import models, fields, api,SUPERUSER_ID


class Band(models.Model):
    _name = 'band'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Bandas'

    name = fields.Char(
        string="Nombre de la banda"
    )
    color = fields.Integer(string='Color Index')
    sequence = fields.Integer(default=10)
    stage_band_id = fields.Many2one(
        'stage.band',
        string='Estado bandas',
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
    facebook = fields.Char(
        string="Correo electrónico?"
    )
    instagram = fields.Char(
        string="Correo electrónico?"
    )
    tik_tok = fields.Char(
        string="Correo electrónico?"
    )
    youtube = fields.Char(
        string="Correo electrónico?"
    )
    website = fields.Char(
        string="Correo electrónico?"
    )
    liga_informacin_extra = fields.Html(
        string="Liga información extra"
    )
    informacin_general = fields.Text(
        string="Liga información extra"
    )

    foto1 = fields.Image(store=True)
    foto2 = fields.Image(store=True)
    foto3 = fields.Image(store=True)
    foto4 = fields.Image(store=True)

    evaluador_1 = fields.Text(
        string="Evaluador 1"
    )
    evaluador_2 = fields.Text(
        string="Evaluador 2"
    )
    evaluador_3 = fields.Text(
        string="Evaluador 3"
    )
    evaluador_4 = fields.Text(
        string="Evaluador 4"
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
        return self.env['stage.band'].search([])

    #-----------------------------------------------------------------#