odoo.define('web_recently_viewed_product.dynamic', function (require) {
   var PublicWidget = require('web.public.widget');
   var rpc = require('web.rpc');
   var Dynamic = PublicWidget.Widget.extend({
       selector: '.dynamic_snippet_blog',
       start: function () {
            console.log("ssssssui");
           var self = this;
           rpc.query({
               route: '/recently_viewed',
               params: {},
           }).then(function (result) {
               self.$('#total_sold').text(result);
           });
       },
   });
   PublicWidget.registry.dynamic_snippet_blog = Dynamic;
   return Dynamic;
});