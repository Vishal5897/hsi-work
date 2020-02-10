from odoo import http
from odoo.http import request
from odoo.addons.web.controllers.main import Home
from odoo.addons.portal.controllers.portal import CustomerPortal, pager

class Home(Home):
    # pass
    def _login_redirect(self, uid, redirect=None):
        if request.session.uid and request.env['res.users'].sudo().browse(request.session.uid).has_group('feescollection.group_manager'):
            return '/web/'
        if request.session.uid and request.env['res.users'].sudo().browse(request.session.uid).has_group('base.group_user'):
            return'/web/'
        if  request.session.uid and request.env['res.users'].sudo().browse(request.session.uid).has_group('base.group_portal'):
            return '/index/'
        return super(StudentDetails , self)._login_redirect(uid, redirect=redirect)

class StudentDetails(CustomerPortal):

    # @http.route(['/index/'], type='http', auth="public", website=True)
    # def user_reg(self, page=1, date_begin=None, date_end=None, sortby=None, **post):
    #     if request.httprequest.method == "POST":
    #         print(">>>>>>>>>>>>>", request.params)
    #     record = request.env['student.student'].sudo().search([("res_user","=",request.env.user.id)])
    #     return request.render('feescollection.index_1', {
    #         "record": record,
    #     })

    @http.route(['/my/test'], type='http', auth="public", website=True)
    def user_registration(self, page=1, date_begin=None, date_end=None, sortby=None, **kw):
        if request.httprequest.method == "POST":
            if request.params.get('user_type') == "8":
                request.env["res.users"].sudo().create({
                    'login': request.params.get("txt_uname"),
                    'password': request.params.get('txt_password'),
                    'name': request.params.get("txt_uname"),
                    'groups_id': [
                        (6, 0, [request.env.ref('base.group_portal').id]
                    )],
                })

            if request.params.get('user_type') == "1":
                request.env['institute.institute'].create({
                    'name':request.params.get("txt_uname"),
                    'partner_id':request.params.get("txt_uname"),
                    'address':request.params.get("txt_uname"),
                    'contact':request.params.get("txt_uname"),
                    'password':request.params.get("txt_password"),
                    'currency_id':request.params.get("currncy_id"),

                    })
            return request.redirect("/web/login")
        rec = request.env['res.currency'].sudo().search([])
        return request.render("feescollection.user_register", \
            {"rec": rec, "values": values})

    @http.route(['/payment/'], type='http', auth="public", website=True)
    def new_try(self, page=1, date_begin=None, date_end=None, sortby=None, **kw):
        return request.render('feescollection.user_register')
