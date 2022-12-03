import uuid

from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from manager.models import Product, Warehouse, Order
from manager.serializers import ProductSerializer, WarehouseSerializer, OrderSerializer


@api_view(['POST'])
def add_product(request):
    product = ProductSerializer(data=request.data)

    if Product.objects.filter(**request.data).exists():
        raise serializers.ValidationError('This data already exists')

    if product.is_valid():
        product.save()
        return Response(product.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def list_products(request):
    if request.query_params:
        products = Product.objects.filter(**request.query_param.dict())
    else:
        products = Product.objects.all()

    if products:
        products = ProductSerializer(products, many=True)
        return Response(products.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def get_product_by_pk(request, id):
    product = Product.objects.filter(id=id)
    if product:
        product = ProductSerializer(product, many=True)
        return Response(product.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['DELETE'])
def delete_product(request, id):
    product = Product.objects.filter(id=id)

    if product:
        product.delete()
        return Response(status=status.HTTP_202_ACCEPTED)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def update_product(request, id):
    product = Product.objects.get(id=id)
    data = ProductSerializer(instance=product, data=request.data)

    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def add_warehouse(request):
    warehouse = WarehouseSerializer(data=request.data)

    if Warehouse.objects.filter(**request.data).exists():
        raise serializers.ValidationError('This data already exists')

    if warehouse.is_valid():
        warehouse.save()
        return Response(warehouse.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def list_warehouses(request):
    if request.query_params:
        warehouse = Warehouse.objects.filter(**request.query_param.dict())
    else:
        warehouse = Warehouse.objects.all()

    if warehouse:
        warehouse = WarehouseSerializer(warehouse, many=True)
        return Response(warehouse.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def get_warehouse_by_pk(request, id):
    warehouse = Warehouse.objects.filter(id=id)
    if warehouse:
        warehouse = WarehouseSerializer(warehouse, many=True)
        return Response(warehouse.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['DELETE'])
def delete_warehouse(request, id):
    warehouse = Warehouse.objects.filter(id=id)

    if warehouse:
        warehouse.delete()
        return Response(status=status.HTTP_202_ACCEPTED)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def update_warehouse(request, id):
    warehouse = Warehouse.objects.get(id=id)
    data = WarehouseSerializer(instance=warehouse, data=request.data)

    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def add_order(request):
    order = OrderSerializer(data=request.data)

    if Order.objects.filter(**request.data).exists():
        raise serializers.ValidationError('This data already exists')

    if order.is_valid():
        order.save()
        return Response(order.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def list_orders(request):
    if request.query_params:
        order = Order.objects.filter(**request.query_param.dict())
    else:
        order = Order.objects.all()

    if order:
        order = OrderSerializer(order, many=True)
        return Response(order.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def get_order_by_pk(request, id):
    order = Order.objects.filter(id=id)
    if order:
        order = OrderSerializer(order, many=True)
        return Response(order.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['DELETE'])
def delete_order(request, id):
    order = Order.objects.filter(id=id)

    if order:
        order.delete()
        return Response(status=status.HTTP_202_ACCEPTED)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def update_order(request, id):
    order = Order.objects.get(id=id)
    data = OrderSerializer(instance=order, data=request.data)

    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)