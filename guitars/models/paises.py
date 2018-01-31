
from odoo import models, fields

class Paises(models.Model):
    _name = 'guitars.paises'
    codigo = fields.Integer('Codigo', required=True)
    nombre = fields.Char('Nombre del pais', required=True)

    def name_get(self):
        res=[]
        for record in self:
            name = record.nombre
            res.append((record.id, name))
        return res



class Regiones(models.Model):
    _name = 'guitars.regiones'
    region = fields.Char('Region', required=True)
    pais = fields.Many2one('guitars.paises', 'Paises')


    def name_get(self):
        res=[]
        for record in self:
            name = record.region
            res.append((record.id, name))
        return res
