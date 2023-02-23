from odoo import http
from odoo.http import request


class Sales(http.Controller):
    @http.route(['/recently_viewed'], type="json", auth="public")
    def sold_total(self):
        max_number_of_product_for_snippet = 10
        visitor = request.env['website.visitor']._get_visitor_from_request()
        print(visitor)
        if visitor:
            # excluded_products = request.website.sale_get_order().mapped(
            #     'order_line.product_id.id')
            # print(excluded_products)

            products = request.env['website.track'].sudo().search(
                [('visitor_id', '=', visitor.id), ('product_id', '!=', False)])
            print(products)
        #     products_ids = [product['product_id'][0] for product in products]
        #     if products_ids:
        #         viewed_products = request.env['product.product'].with_context(
        #             display_default_code=False).browse(products_ids)
        #     FieldMonetary = request.env['ir.qweb.field.monetary']
        #     monetary_options = {
        #         'display_currency': request.website.get_current_pricelist().currency_id,
        #     }
        #     rating = request.website.viewref(
        #         'website_sale.product_comment').active
        #     res = {'products': []}
        #     for product in viewed_products:
        #         combination_info = product._get_combination_info_variant()
        #         res_product = product.read(['id', 'name', 'website_url'])[0]
        #         res_product.update(combination_info)
        #         res_product['price'] = FieldMonetary.value_to_html(
        #             res_product['price'], monetary_options)
        #         if rating:
        #             res_product['rating'] = request.env[
        #                 "ir.ui.view"]._render_template(
        #                 'portal_rating.rating_widget_stars_static', values={
        #                     'rating_avg': product.rating_avg,
        #                     'rating_count': product.rating_count,
        #                 })
        #         res['products'].append(res_product)
        #     return res
        # return {}
