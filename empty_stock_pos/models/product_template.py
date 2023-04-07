from odoo import api, fields, models, _
from odoo.exceptions import UserError
import logging
_logger = logging.getLogger(__name__)

class ProductTemplate(models.Model):
    _inherit = 'product.template'
    
    def get_stock_on_hands_pos(self, product_id, warehouse_id):
        return self.env['product.product'].sudo().with_context({'warehouse' : warehouse_id}).browse(product_id).qty_available
        