from odoo import http
from odoo.http import request, Controller


class ProductsRecentlyViewed(Controller):
    @http.route(['/recently_viewed'], type="json", auth="public")
    def _get_products_recently_viewed(self):
        visitor = request.env['website.visitor']._get_visitor_from_request()
        # print(visitor)
        if visitor:

            products = request.env['website.track'].sudo().read_group(
                [('visitor_id', '=', visitor.id), ('product_id', '!=', False),
                 ],
                ['product_id', 'visit_datetime:max'], ['product_id'],
                limit=10, orderby='visit_datetime DESC')
            # print(products)
            products_ids = [product['product_id'][0] for product in products]
            # print(products_ids)

            # viewed_products = request.env['product.product'].with_context(
            #         display_default_code=False).sudo().browse(products_ids)
            viewed_products = request.env['product.product']\
                .sudo().browse(products_ids)
            # print(viewed_products.product_tmpl_id)
            view_product_tmpl = viewed_products.product_tmpl_id
            # print(view_product_tmpl)
            # for i in products_ids:
            #     print(i == viewed_products.id)
            product_list = [[view.name, view.id, view.description_sale] for view in view_product_tmpl]
            # step_size = 5
            new_list = [product_list[i:i+4] for i in range(
                0, len(product_list), 4)]
                # print(view)
                # print(view.id)
                # print(view.name)
                # product_dict[view.name] = view.id
            print(product_list)
            print(new_list)
            return new_list
