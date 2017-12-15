from odoo import models, fields

class Guitars(models.Model):
    _name = 'guitars.guitars'
    codigo = fields.Integer('Codigo', required=True)
    marca = fields.Char('Marca', required=True)
    modelo = fields.Char('Modelo', required=True)