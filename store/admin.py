from django.contrib import admin
from .models import Product, Store_category

class admin_Product(admin.ModelAdmin):
    readonly_fields=('created','updated')

class admin_Store_category(admin.ModelAdmin):
    readonly_fields=('created','updated')

admin.site.register(Product,admin_Product)
admin.site.register(Store_category,admin_Store_category)
