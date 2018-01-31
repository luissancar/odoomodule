from odoo import models, fields, api

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

