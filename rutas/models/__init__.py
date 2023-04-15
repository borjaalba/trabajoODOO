# -*- coding: utf-8 -*-
import pip
try:
    import googlemaps
except ImportError:
    print('\n There was no such module named -googlemaps- installed')
    print('xxxxxxxxxxxxxxxx installing googlemaps xxxxxxxxxxxxxx')
    pip.main(['install', 'googlemaps'])

from . import ruta_property