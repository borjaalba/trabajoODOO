import googlemaps
from datetime import datetime
from gmplot import gmplot

# Configuración de la API de Google Maps
gmaps = googlemaps.Client(key='AIzaSyBmvKq4xWz9axrxSqTsuiop51YWBRU6gpA') # Reemplazar con su clave de API

# Coordenadas de los puntos de inicio y finalización
start_point = "Lucena, Spain"
end_point = "Barcelona, Spain"


#Puntos por los que se debe de pasar

waypoints = ["Málaga, Spain", end_point]


# Obtención de la información de la ruta
now = datetime.now()
directions_result = gmaps.directions(start_point, end_point,waypoints = waypoints , mode="driving", departure_time=now, language="es")

# Extracción de las coordenadas de la ruta
route = []
steps = directions_result[0]['legs'][0]['steps']
for step in steps:
    start_location = step['start_location']
    end_location = step['end_location']
    route.append((start_location['lat'], start_location['lng']))
    route.append((end_location['lat'], end_location['lng']))

# Configuración del mapa
gmap = gmplot.GoogleMapPlotter(route[0][0], route[0][1], 8)

# Dibujar la ruta en el mapa
latitude_list, longitude_list = zip(*route)
gmap.plot(latitude_list, longitude_list, 'cornflowerblue', edge_width=5)

# Mostrar el mapa en un archivo HTML
gmap.draw("ruta.html")