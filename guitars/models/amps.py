from odoo import models, fields

class Amps(models.Model):
    _name = 'guitars.amps'
    codigo = fields.Integer('Codigo', required=True)
    marca = fields.Char('Marca', required=True)
    modelo = fields.Char('Modelo', required=True)