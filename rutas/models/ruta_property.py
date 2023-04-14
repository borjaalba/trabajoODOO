# -*- coding: utf-8 -*-
from odoo import fields, models

class RutaProperty(models.Model):
    _name = 'ruta.property'
    _description = 'Modulo para generar rutas en Google Maps'

    origen = fields.Char('Punto de inicio', required=True)
    destino = fields.Char('Punto de fin', required=True)
    waypoints = fields.Char('Puntos intermedios')
    distancia = fields.Float('Distancia', readonly=True)
    duracion = fields.Float('Duración', readonly=True)
