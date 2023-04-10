# -*- coding: utf-8 -*-
# from odoo import http


# class PlusOneTask(http.Controller):
#     @http.route('/plus_one_task/plus_one_task', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/plus_one_task/plus_one_task/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('plus_one_task.listing', {
#             'root': '/plus_one_task/plus_one_task',
#             'objects': http.request.env['plus_one_task.plus_one_task'].search([]),
#         })

#     @http.route('/plus_one_task/plus_one_task/objects/<model("plus_one_task.plus_one_task"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('plus_one_task.object', {
#             'object': obj
#         })
