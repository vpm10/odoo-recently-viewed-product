from odoo import fields, models


class WebTracker(models.Model):
    _inherit = 'website.track'

    product_id = fields.Many2one('product.product')
