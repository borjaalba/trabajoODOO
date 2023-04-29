# -*- coding: utf-8 -*-
import pip
try:
    import googlemaps
except ImportError:
    print('\n No está el módulo -googlemaps- instalado')
    print('xxxxxxxxxxxxxxxx Instalando googlemaps xxxxxxxxxxxxxx')
    pip.main(['install', 'googlemaps'])

from . import ruta_property