from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('warehouses', views.warehouses),
    path('products', views.products),
    path('orders', views.orders),
    path('list_products', views.list_products),
    path('list_warehouses', views.list_warehouses),

]