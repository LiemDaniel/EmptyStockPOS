odoo.define('empty_stock_pos.EmptyStockPOS_ProductScreen', function(require) {
    'use strict';
    const Registries = require('point_of_sale.Registries');
    const ProductScreen = require('point_of_sale.ProductScreen');
 
     const EmptyStockPOS = (ProductScreen) => class extends ProductScreen {

        async _clickProduct(event) {
            // console.log('Empty Stock POS Click Product')
            // console.log(event.detail.id)
            // console.log(this.env.pos.config.warehouse_id[1])

            let stock_on_hands = await this.env.services.rpc({
                model: 'product.template',
                method: 'get_stock_on_hands_pos',
                args: ['',event.detail.id, this.env.pos.config.warehouse_id[0]],
            }, { shadow: true });
            
            if(stock_on_hands <= 0){
                this.showPopup('ErrorPopup', {
                    title: this.env._t('Produk Habis'),
                    body: this.env._t('Produk Yang Ditambahkan telah habis.'),
                });
            }
            super._clickProduct(event)
        }
     };
     Registries.Component.extend(ProductScreen, EmptyStockPOS);
     return ProductScreen;
 
 });