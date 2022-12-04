from django.db.models import fields
from rest_framework import serializers
from .models import Warehouse, Product, Order


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'price', 'order_id', 'warehouse_id')

class WarehouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warehouse
        fields = ('id','address')

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('id','email')

