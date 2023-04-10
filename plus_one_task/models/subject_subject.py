from odoo import fields, models, api


class SchoolClass(models.Model):
    _name = 'subject.subject'
    _description = 'subject'

    name = fields.Char(
        string='name',
        required=True)

