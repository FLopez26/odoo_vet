
from odoo import models, fields

class VetMascota(models.Model):
    _name = 'vet.mascota'
    _description = 'Información de Mascota'

    nombre = fields.Char(string='Nombre de la Mascota', required=True)
    especie = fields.Char(string='Especie')
    raza = fields.Char(string='Raza')
    edad = fields.Integer(string='Edad')
    propietario_id = fields.Many2one('res.partner', string='Propietario')  # Relación Uno a Muchos
    veterinario_cabecera_id = fields.Many2one('res.partner', string='Veterinario de Cabecera')  # Relación Uno a Uno
    cita_ids = fields.One2many('vet.cita', 'mascota_id', string='Citas')  # Relación Uno a Muchos
