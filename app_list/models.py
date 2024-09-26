from django.db import models

from enums import AppName


class App(models.Model):
    name = models.CharField(max_length=255, choices=[(app.value, app.value) for app in AppName])
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_api_url(self, store_name, access_token):
        if self.name == AppName.SHOPIFY.value:
            return f"https://{store_name}.myshopify.com/admin/api/2024-07"

    def __str__(self):
        return self.name

class Action(models.Model):
    app = models.ForeignKey(App, on_delete=models.CASCADE)
    name = models.CharField(max_length=255) #Get Customer by ID
    slug = models.SlugField(unique=True)    
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    parameters = models.JSONField() #{"customer_id": "1234567890"}
    output_schema = models.JSONField() #{"customer": {"id": "1234567890", "name": "John Doe", "email": "john.doe@example.com"}}
    action_path = models.CharField(max_length=255) #"ecommerce.shopify.get_customer_by_id"

    def __str__(self):
        return self.name
    
class OrganizationApp(models.Model):
    organization_id = models.CharField(max_length=255)
    app = models.ForeignKey(App, on_delete=models.CASCADE)
    app_specific_params = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_api_url(self, store_name):
        return self.app.get_api_url(store_name=self.app_specific_params['store_name'], access_token=self.app_specific_params['auth_token'])

    def __str__(self):
        return self.organization_id