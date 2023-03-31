# -*- coding: utf-8 -*-
from odoo import fields, models

class Ruta(models.Model):
    _name = 'ruta'
    _description = 'Módulo para generar rutas en Google Maps'
    start_point = fields.Char('Punto de inicio')
    end_point = fields.Char('Punto de fin')
    waypoints = fields.Char('Puntos intermedios')
