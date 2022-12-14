from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('warehouses', views.warehouses),
    path('products', views.products),
    path('orders', views.orders),
    path('list_products', views.list_products),
    path('add_product', views.add_product),
    path('delete_product', views.delete_product),
    path('list_warehouses', views.list_warehouses),
    path('add_warehouse', views.add_warehouse),
    path('update_warehouse', views.update_warehouse),
    path('delete_warehouse', views.delete_warehouse),
    path('list_orders', views.list_orders),
    path('add_order', views.add_order),
    path('delete_order', views.delete_order),

]