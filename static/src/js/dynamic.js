odoo.define('web_recently_viewed_product.dynamic', function (require) {
   var PublicWidget = require('web.public.widget');
   var rpc = require('web.rpc');
   var core = require('web.core')
   var Qweb = core.qweb
   var Dynamic = PublicWidget.Widget.extend({
       selector: '.dynamic_snippet_blog',
       start: function () {
//            console.log("ssssssui");
           var self = this;
           rpc.query({
               route: '/recently_viewed',
               params: {},
           }).then(function (result) {
           result[0].set_active = true;
           $('.qweb_product').append(Qweb.render('web_recently_viewed_product.recently_product', {result}));
//               self.$('#product_dict').text(result);
//               console.log(result)
           });
       },
   });
   PublicWidget.registry.dynamic_snippet_blog = Dynamic;
   return Dynamic;
});
