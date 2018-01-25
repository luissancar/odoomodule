
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



