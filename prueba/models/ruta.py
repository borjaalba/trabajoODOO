# -*- coding: utf-8 -*-
from odoo import fields, models

class Ruta(models.Model):
    _name = 'rutas.ruta'
    _description = 'Módulo para generar rutas en Google Maps'

    origen = fields.Char('Punto de inicio', required=True)
    destino = fields.Char('Punto de fin', required=True)
    waypoints = fields.Char('Puntos intermedios')
    distancia = fields.Float('Distancia', readonly=True)
    duracion = fields.Float('Duración', readonly=True)
