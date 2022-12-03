from django.urls import path

from . import views

urlpatterns = [
    path('product/create/', views.add_product, name='add_products'),
    path('products/', views.list_products, name='list_products'),
    path('product/<str:id>', views.get_product_by_pk, name='get_product_by_pk'),
    path('product/delete/<str:id>', views.delete_product, name='delete_product'),
    path('product/update/<str:id>', views.update_product, name='update_products'),
    path('warehouse/create/', views.add_warehouse, name='add_warehouse'),
    path('warehouses/', views.list_warehouses, name='list_warehouses'),
    path('warehouse/<str:id>', views.get_warehouse_by_pk, name='get_warehouse_by_pk'),
    path('warehouse/delete/<str:id>', views.delete_warehouse, name='delete_warehouse'),
    path('warehouse/update/<str:id>', views.update_warehouse, name='update_warehouse'),
    path('order/create/', views.add_order, name='add_order'),
    path('orders/', views.list_orders, name='list_orders'),
    path('order/<str:id>', views.get_order_by_pk, name='get_order_by_pk'),
    path('order/delete/<str:id>', views.delete_order, name='delete_order'),
    path('order/update/<str:id>', views.update_order, name='update_order'),
]