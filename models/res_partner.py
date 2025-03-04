
from odoo import models, fields

#reusamos un modulo
class ResPartner(models.Model):
    _inherit = 'res.partner'
    _order = 'name'

    es_veterinario = fields.Boolean(string='Es Veterinario', default=False)
    es_propietario_mascota = fields.Boolean(string='Es Propietario de Mascota', default=False)