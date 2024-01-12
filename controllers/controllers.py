# -*- coding: utf-8 -*-
# from odoo import http


# class Direct(http.Controller):
#     @http.route('/direct/direct', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/direct/direct/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('direct.listing', {
#             'root': '/direct/direct',
#             'objects': http.request.env['direct.direct'].search([]),
#         })

#     @http.route('/direct/direct/objects/<model("direct.direct"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('direct.object', {
#             'object': obj
#         })
