import googlemaps
from odoo import models, api
from datetime import datetime

class CalculadorRuta(models.Model):
    _name = 'Rutas.calculadorRuta'
    _description = 'Módulo para generar rutas en Google Maps'

    @api.model
    def calcula_ruta(self, origen, destino, puntos_intermedios):
        apiGoogle = 'AIzaSyBmvKq4xWz9axrxSqTsuiop51YWBRU6gpA'

        gmaps = googlemaps.Client(key=apiGoogle) # Reemplazar con su clave de API

        #Puntos por los que se debe de pasar
        puntos_intermedios.append(destino)

        # Obtención de la información de la ruta
        now = datetime.now()
        directions_result = gmaps.directions(origen, destino, waypoints = puntos_intermedios, mode="driving", departure_time=now, language="es")

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

        return self.env['Rutas.ruta'].create({
            'origen': origen,
            'destino': destino,
            'waypoints': puntos_intermedios,
            'distancia': distanciaMetros,
            'duracion': tiempoSegundos,
        })