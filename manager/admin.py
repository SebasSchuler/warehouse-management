from django.contrib import admin

from manager.models import Product, Warehouse, Order

admin.site.register(Product)
admin.site.register(Warehouse)
admin.site.register(Order)