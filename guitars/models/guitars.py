from odoo import models, fields, api

class GuitarsGuitars(models.Model):
    _name = 'guitars.guitars'
    codigo = fields.Integer('Codigo', required=True)
    marca = fields.Char('Marca', required=True)
    modelo = fields.Char('Modelo', required=True)
    pais = fields.Many2one('guitars.paises', 'Paises')



    @api.one
    def limpiar(self):
        self.marca = ""
        return True

    @api.multi
    def limpia_todo(self):
        done_recs = self.search([('marca', '=', 'fender')])
        done_recs.write({'marca': 'Fender'})
        return True

