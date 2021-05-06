# -*- coding: utf-8 -*-
# from odoo import http


# class Lance(http.Controller):
#     @http.route('/lance/lance/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/lance/lance/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('lance.listing', {
#             'root': '/lance/lance',
#             'objects': http.request.env['lance.lance'].search([]),
#         })

#     @http.route('/lance/lance/objects/<model("lance.lance"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('lance.object', {
#             'object': obj
#         })
