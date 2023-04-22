# -*- coding: utf-8 -*-
from odoo import fields, models
import googlemaps
from datetime import datetime

class RutaProperty(models.Model):
    _name = "ruta.property"
    name = fields.Char('Nombre', required=True)

    _description = "Modulo para generar rutas en Google Maps"

    origen = fields.Char('Punto de inicio', required=True)
    destino = fields.Char('Punto de fin', required=True)
    waypoints = fields.Char('Puntos intermedios')
    distancia = fields.Float('Distancia', readonly=True)
    duracion = fields.Float('Duración', readonly=True)

    def calcular_ruta(self):
        apiGoogle = 'AIzaSyBmvKq4xWz9axrxSqTsuiop51YWBRU6gpA'

        gmaps = googlemaps.Client(key=apiGoogle) # Reemplazar con su clave de API

        #Puntos por los que se debe de pasar
        if(self.waypoints==False):
            puntos_intermedios = [self.destino]
        else:
            puntos_intermedios = self.waypoints.split(',')
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

        # Extracción de las coordenadas de la ruta
        # route = []
        # steps = directions_result[0]['legs'][0]['steps']
        # for step in steps:
        #     start_location = step['start_location']
        #     end_location = step['end_location']
        #     route.append((start_location['lat'], start_location['lng']))
        #     route.append((end_location['lat'], end_location['lng']))

        #     # Configuración del mapa
        #     gmap = gmplot.GoogleMapPlotter(route[0][0], route[0][1], 8)

        #     # Dibujar la ruta en el mapa
        #     latitude_list, longitude_list = zip(*route)
        #     gmap.plot(latitude_list, longitude_list, 'cornflowerblue', edge_width=5)

        #     # Mostrar el mapa en un archivo HTML
        #     gmap.draw("ruta.html")

        print(distanciaMetros)
        print(tiempoSegundos)

        # return self.env['Rutas.ruta'].create({
        #     'origen': origen,
        #     'destino': destino,
        #     'waypoints': puntos_intermedios,
        #     'distancia': distanciaMetros,
        #     'duracion': tiempoSegundos,
        # })
