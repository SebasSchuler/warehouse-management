import uuid

from django.contrib.auth import authenticate
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import ensure_csrf_cookie
from rest_framework import serializers, status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, renderer_classes
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND, HTTP_200_OK

from manager.models import Product, Warehouse, Order
from manager.serializers import ProductSerializer, WarehouseSerializer, OrderSerializer



@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")
    if username is None or password is None:
        return Response({'error': 'Please provide both username and password'},
                        status=HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)
    if not user:
        return Response({'error': 'Invalid Credentials'},
                        status=HTTP_404_NOT_FOUND)
    token = Token.objects.create(user=user)
    print(token.key)
    return Response({'token': token.key},
                    status=HTTP_200_OK)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
@renderer_classes([JSONRenderer])
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
@permission_classes([IsAuthenticated])
@renderer_classes([JSONRenderer])
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
@permission_classes([IsAuthenticated])
@renderer_classes([JSONRenderer])
def get_product_by_pk(request, id):
    product = Product.objects.filter(id=id)
    if product:
        product = ProductSerializer(product, many=True)
        return Response(product.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_product(request, id):
    product = Product.objects.filter(id=id)

    if product:
        product.delete()
        return Response(status=status.HTTP_202_ACCEPTED)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def update_product(request, id):
    product = Product.objects.get(id=id)
    data = ProductSerializer(instance=product, data=request.data)

    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
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
@permission_classes([IsAuthenticated])
@renderer_classes([JSONRenderer])
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
@permission_classes([IsAuthenticated])
@renderer_classes([JSONRenderer])
def get_warehouse_by_pk(request, id):
    warehouse = Warehouse.objects.filter(id=id)
    if warehouse:
        warehouse = WarehouseSerializer(warehouse, many=True)
        return Response(warehouse.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_warehouse(request, id):
    warehouse = Warehouse.objects.filter(id=id)

    if warehouse:
        warehouse.delete()
        return Response(status=status.HTTP_202_ACCEPTED)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def update_warehouse(request, id):
    warehouse = Warehouse.objects.get(id=id)
    data = WarehouseSerializer(instance=warehouse, data=request.data)

    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
@renderer_classes([JSONRenderer])
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
@permission_classes([IsAuthenticated])
@renderer_classes([JSONRenderer])
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
@permission_classes([IsAuthenticated])
@renderer_classes([JSONRenderer])
def get_order_by_pk(request, id):
    order = Order.objects.filter(id=id)
    if order:
        order = OrderSerializer(order, many=True)
        return Response(order.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_order(request, id):
    order = Order.objects.filter(id=id)

    if order:
        order.delete()
        return Response(status=status.HTTP_202_ACCEPTED)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def update_order(request, id):
    order = Order.objects.get(id=id)
    data = OrderSerializer(instance=order, data=request.data)

    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
@renderer_classes([JSONRenderer])
def list_products_from_order(request, id):
    products = Product.objects.filter(order_id_id__id=id)
    if products:
        products = ProductSerializer(products, many=True)
        return Response(products.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)