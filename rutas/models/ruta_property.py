# -*- coding: utf-8 -*-
from odoo import api, fields, models
from odoo.exceptions import ValidationError
import googlemaps
from datetime import datetime
import re
import gmplot

class RutaProperty(models.Model):
    _name = "ruta.property"
    name = fields.Char('Nombre', required=True)

    _description = "Modulo para generar rutas en Google Maps"

    origen = fields.Char('Punto de inicio', required=True)
    destino = fields.Char('Punto de fin', required=True)
    waypoints = fields.Char('Puntos intermedios')
    distancia = fields.Float('Distancia en km', readonly=True)
    duracion = fields.Float('Duración (horas:minutos)', readonly=True)
    # camino = fields.Text('La direccion que se debe de seguir es la siguiente')
    mapa = fields.Html("El mapa es el siguiente")

    ruta_calculada = fields.Boolean('Ruta calculada', readonly=True, default=False)

    @api.constrains('name')
    def checkea_nombre(self):
        #No se pueden crear rutas con el mismo nombre
        if self.search_count([('name', '=', self.name)]) > 1:
            raise ValidationError("Ya existe una ruta con ese nombre")
        
        
        

    @api.constrains('origen', 'destino', 'waypoints')
    def checkea_origen_destino(self):
        formato_lugar = r'^[a-zA-Z\s]+,[a-zA-Z\s]+$'

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
        self.lista = "12"
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

        route = []
        steps = directions_result[0]['legs'][0]['steps']
        for step in steps:
            instruction = step['html_instructions']
            instruction = instruction.replace('<b>', '').replace('</b>', '.').replace('<div style="font-size:0.9em">', ' ').replace('</div>', ' ').replace('/<wbr/>', ' ')
            route.append(instruction)
        #     print("\nRuta establecida:")
        # for i, instruction in enumerate(route):
        #     print(f"\n{i}. {instruction}")
        # print("\n")
        # print("Ha llegado a su destino camarada de Odoo")


        # self.camino = route
        self.ruta_calculada = True

        # Configuración del mapa
        gmap = gmplot.GoogleMapPlotter(route[0][0], route[0][1], 8)

        # Dibujar la ruta en el mapa
        latitude_list, longitude_list = zip(*route)
        gmap.plot(latitude_list, longitude_list, 'cornflowerblue', edge_width=5)

        # Mostrar el mapa en un archivo HTML
        res = gmap.draw("ruta"+self.origen+"_"+self.destino+"."+"html")

        self.mapa = res 

    
