from django.db.models import fields
from rest_framework import serializers
from .models import Warehouse, Product, Order, ProductWarehouse


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'price', 'order_id',)

class WarehouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warehouse
        fields = ('id','address')

class ProductWarehouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductWarehouse
        fields = ('warehouse_id', 'product_id',)

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('id','email')

