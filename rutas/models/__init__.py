# -*- coding: utf-8 -*-
import pip
try:
    import googlemaps
    import gmplot
except ImportError:
    print('\n There was no such module named -googlemaps- installed')
    print('xxxxxxxxxxxxxxxx installing googlemaps xxxxxxxxxxxxxx')
    pip.main(['install', 'googlemaps'])
    print('\n There was no such module named -gmplot- installed')
    print('xxxxxxxxxxxxxxxx installing gmplot xxxxxxxxxxxxxx')
    pip.main(['install', 'gmplot'])

from . import ruta_property