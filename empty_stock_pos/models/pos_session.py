from odoo import api, fields, models, _
from odoo.exceptions import UserError
import logging
_logger = logging.getLogger(__name__)

class PosSession(models.Model):
    _inherit = 'pos.session'
    
    def _loader_params_product_product(self):
        domain = [
            '&', '&', ('sale_ok', '=', True), ('available_in_pos', '=', True), '|',
            ('company_id', '=', self.config_id.company_id.id), ('company_id', '=', False)
        ]
        if self.config_id.limit_categories and self.config_id.iface_available_categ_ids:
            domain = AND([domain, [('pos_categ_id', 'in', self.config_id.iface_available_categ_ids.ids)]])
        if self.config_id.iface_tipproduct:
            domain = OR([domain, [('id', '=', self.config_id.tip_product_id.id)]])

        return {
            'search_params': {
                'domain': domain,
                'fields': [
                    'display_name', 'lst_price', 'standard_price', 'categ_id', 'pos_categ_id', 'taxes_id', 'barcode',
                    'default_code', 'to_weight', 'uom_id', 'description_sale', 'description', 'product_tmpl_id', 'tracking',
                    'available_in_pos', 'attribute_line_ids', 'active', '__last_update', 'qty_available', 'virtual_available'
                ],
                'order': 'sequence,default_code,name',
            },
            'context': {'display_default_code': False},
        }
        
    def get_pos_ui_product_product_by_params(self, custom_search_params):
        """
        :param custom_search_params: a dictionary containing params of a search_read()
        """
        params = self._loader_params_product_product()
        # custom_search_params will take priority
        params['search_params'] = {**params['search_params'], **custom_search_params}
        warehouse_id = self.env['pos.config']._default_warehouse_id()
        products = self.env['product.product'].with_context({'warehouse': warehouse_id}).search_read(**params['search_params'])
        if len(products) > 0:
            self._process_pos_ui_product_product(products)
        return products