# -*- coding: utf-8 -*-
from odoo import api, fields, models
from odoo.exceptions import ValidationError
import googlemaps
from datetime import datetime
import re

class RutaProperty(models.Model):
    _name = "ruta.property"
    name = fields.Char('Nombre', required=True)

    _description = "Modulo para generar rutas en Google Maps"

    origen = fields.Char('Punto de inicio', required=True)
    destino = fields.Char('Punto de fin', required=True)
    waypoints = fields.Char('Puntos intermedios')
    distancia = fields.Float('Distancia en km', readonly=True)
    duracion = fields.Float('Duración (horas:minutos)', readonly=True)
    coor_ini = fields.Char('Coordenadas de inicio', readonly=True)
    coor_fin = fields.Char('Coordenadas de fin', readonly=True)
    camino = fields.Text('Camino', readonly=True)

    ruta_calculada = fields.Boolean('Ruta calculada', readonly=True, default=False)

    @api.constrains('name')
    def checkea_nombre(self):
        #No se pueden crear rutas con el mismo nombre
        if self.search_count([('name', '=', self.name)]) > 1:
            raise ValidationError("Ya existe una ruta con ese nombre")
        
    @api.constrains('origen', 'destino', 'waypoints')
    def checkea_origen_destino(self):
        formato_lugar = r'^[a-zA-ZñÑ\s]+,[a-zA-ZñÑ\s]+$'

        if not re.match(formato_lugar, self.origen):
            raise ValidationError("El formato del origen es incorrecto")
        
        if not re.match(formato_lugar, self.destino):
            raise ValidationError("El formato del destino es incorrecto")
        
        if self.waypoints!=False:
            if ';' in self.waypoints:
                for punto in self.waypoints.split(';'):
                    if not re.match(formato_lugar, punto):
                        raise ValidationError("El formato de los puntos intermedios es incorrecto")
            
            elif not re.match(formato_lugar, self.waypoints):    
               raise ValidationError("El formato de los puntos intermedios es incorrecto")

        if self.origen == self.destino:
            raise ValidationError("El origen y el destino no pueden ser el mismo lugar")

    def calcular_ruta(self):
        apiGoogle = 'AIzaSyBmvKq4xWz9axrxSqTsuiop51YWBRU6gpA'

        gmaps = googlemaps.Client(key=apiGoogle) # Reemplazar con su clave de API

        #Puntos por los que se debe de pasar
        if(self.waypoints==False):
            puntos_intermedios = [self.destino]
        else:
            puntos_intermedios = self.waypoints.split(';')
            puntos_intermedios.append(self.destino)
        
        # Obtención de la información de la ruta
        now = datetime.now()
        directions_result = gmaps.directions(self.origen, self.destino, waypoints = puntos_intermedios, mode="driving", departure_time=now, language="es")

        # Extracción de la distancia y el tiempo de la ruta
        distanciaMetros = 0
        tiempoSegundos = 0
        for x in directions_result[0]['legs']:
            distanciaMetros += x['distance']['value']
            tiempoSegundos += x['duration']['value']

        self.distancia = distanciaMetros/1000
        self.duracion = (tiempoSegundos/60)/24

        ruta = []
        camino = []
        for step in directions_result[0]['legs'][0]['steps']:
            if(len(ruta)<2):
                start_location = step['start_location']
                ruta.append((start_location['lat'], start_location['lng']))
            
            end_location = step['end_location']
            ruta.append((end_location['lat'], end_location['lng']))
            aux = step['html_instructions'].replace('<b>', '').replace('</b>', '.').replace('<div style="font-size:0.9em">', ' ').replace('</div>', ' ').replace('/<wbr/>', ' ')
            camino.append(aux)

        self.coor_fin = end_location
        self.coor_ini = start_location
        self.camino = "\n".join([f"{i+1}. {x}" for i, x in enumerate(camino)])

        self.ruta_calculada = True
        
