from odoo import fields, models, api

from datetime import date


class SchoolClass(models.Model):
    _name = 'school.class'
    _description = 'School Class'

    name = fields.Char(compute="_cal_name",required=False)
    subject_id = fields.Many2one(
        comodel_name='subject.subject',
        string='Subject',
        required=True)
    student_id = fields.Many2one(
        comodel_name='res.partner',
        string='Student',
        required=True)
    teacher_id = fields.Many2one(
        comodel_name='res.partner',
        string='Teacher',
        required=True)

    @api.depends("subject_id")
    def _cal_name(self):
        for rec in self:
            if rec.subject_id:
                month = date.today().strftime("%m")
                years = date.today().strftime("%y")
                rec.name = rec.subject_id.name+"-20"+years+"-"+month
            else:
                rec.name = False
