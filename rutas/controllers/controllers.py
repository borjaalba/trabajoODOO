# -*- coding: utf-8 -*-
# from odoo import http


# class Prueba(http.Controller):
#     @http.route('/prueba/prueba', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/prueba/prueba/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('prueba.listing', {
#             'root': '/prueba/prueba',
#             'objects': http.request.env['prueba.prueba'].search([]),
#         })

#     @http.route('/prueba/prueba/objects/<model("prueba.prueba"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('prueba.object', {
#             'object': obj
#         })


from odoo import http

class RutaController(http.Controller):

    @http.route('/ruta/property/calculardistancia', type='json', auth='user')
    def calcular_distancia(self, origen, destino):
        distancia, duracion = self.get_distancia(origen, destino)
        return {'distancia': distancia, 'duracion': duracion}

    def get_distancia(self, origen, destino):
        return origen +" "+ destino
