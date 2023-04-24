# -*- coding: utf-8 -*-
import pip
try:
    import googlemaps
    import folium
    import gmplot
except ImportError:
    print('\n There was no such module named -googlemaps- installed')
    print('xxxxxxxxxxxxxxxx installing googlemaps xxxxxxxxxxxxxx')
    pip.main(['install', 'googlemaps'])
    print('\n There was no such module named -gmplot- installed')
    print('xxxxxxxxxxxxxxxx installing gmplot xxxxxxxxxxxxxx')
    pip.main(['install', 'gmplot'])
    print('\n There was no such module named -folium- installed')
    print('xxxxxxxxxxxxxxxx installing folium xxxxxxxxxxxxxx')
    pip.main(['install', 'folium'])

from . import ruta_property