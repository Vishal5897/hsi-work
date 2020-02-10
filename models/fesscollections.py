# -*- coding: utf-8 -*-
# Copyright YEAR(S), AUTHOR(S)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models, api


class Institute(models.Model):
    _name = 'institute.institute'
    _description = 'institute data'
    _rec_name = 'company_id'

    company_id = fields.Many2one('res.company',string='Institute Name')
    partner_id = fields.Many2one("res.partner", string='Partner Name')
    currency_id = fields.Many2one('res.currency', string='Currency')
    user_id = fields.Many2one('res.users', string='User')
    address = fields.Text(string='Address')
    contact = fields.Char(string='Contact Number')
    password = fields.Char(tring='pass')

    # @api.model
    # def create(self, vals):
            # partner = self.env['res.partner'].sudo().create({
            #     'name': vals.get("name"),
            #     "email": vals.get("name"),
            # })
            # # currency = self.env['res.company'].sudo().browse(vals.get("currency_id"))
            # company = self.env['res.company'].sudo().create({
            #     "name": vals.get("name"),                                       
            #     "partner_id": partner.id,
            #     "currency_id": vals.get("currency_id"),
            # })

            # user = self.env["res.users"].sudo().create({
            #     'login': vals.get("name"),
            #     'password': vals.get('password'),
            #     'name': vals.get('name'),
            #     'partner_id': partner.id,
            #     'groups_id': [(6, 0, [self.env.ref('base.group_user').id])],
            # })

            # user.sudo().update({
            #     'company_ids': [(4, company.id)],
            #     'company_id': company.id,
            # })
        # return super(Institute, self).create(vals)

class Course(models.Model):
    _name = 'course.course'
    _description = 'Description'

    name = fields.Char(string="Cource Name")
    course_fees = fields.Integer(string='Course Fees')


class Student(models.Model):
    _name = 'student.student'
    _description = 'student Description'
    _rec_name = "student_name"

    student_name = fields.Char(string='Student Name')
    course_name = fields.Many2one('course.course', string='Course Name')
    # student_id = fields.Char(string='student id')
    enrolment_no = fields.Integer(string='Enrolment No')
    mobile_number = fields.Integer(string='Mobile Number')
    address = fields.Char(string='Address')
    institute_ids = fields.Many2one('institute.institute', string='Institute')
    res_user = fields.Many2one('res.users', string='student id')


    @api.model
    def create(self, vals):
        user = self.env["res.users"].create({
            'login': vals.get("enrolment_no"),
            'password': vals.get("enrolment_no"),
            'name': vals.get("student_name"),
            'groups_id': [(6, 0, [self.env.ref('base.group_portal').id])],
        })
        vals['res_user'] = user.id
        return super(Student, self).create(vals)

