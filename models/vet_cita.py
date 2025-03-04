
from odoo import models, fields

class VetCita(models.Model):
    _name = 'vet.cita'
    _description = 'Cita Veterinaria'

    fecha = fields.Datetime(string='Fecha de la Cita')
    motivo = fields.Text(string='Motivo')
    mascota_id = fields.Many2one('vet.mascota', string='Mascota')  # Relación Uno a Muchos
    veterinario_ids = fields.Many2many('res.partner', 'vet_cita_veterinarios_rel', string='Veterinarios')  # Relación Muchos a Muchos
