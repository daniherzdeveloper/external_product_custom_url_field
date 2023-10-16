from odoo import models, fields, api

# Module that inherits from product.template and adds two custom fields and overrides the website_url field
class CustomProductTemplate(models.Model):
    _inherit = 'product.template'

    custom_url = fields.Char('URL Custom', readonly=False, default="https://www.example.com")
    website_url = fields.Char(compute="_compute_custom_url")
    activate_custom_url = fields.Boolean('Activate Custom Url', default=False)

    @api.depends('custom_url', 'activate_custom_url')
    # If the user activates the activate_custom_url field, the custom url will be assigned to the product,
    # otherwise the website_url field will remain the same.
    def _compute_custom_url(self):
        for product in self:
            if product.activate_custom_url:
                product.website_url = product.custom_url
            else:
                product._compute_website_url()
                
    # function that keeps the website_url field with its original configuration
    def _compute_website_url(self):
        super(CustomProductTemplate, self)._compute_website_url()



