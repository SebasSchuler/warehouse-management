from django.shortcuts import render


def index(request):
    return render(request, 'frontend/index.html')


def list_products(request):
    return render(request, 'frontend/list_products.html')


def products(request):
    return render(request, 'frontend/products.html')


def warehouses(request):
    return render(request, 'frontend/warehouses/warehouses.html')


def list_warehouses(request):
    return render(request, 'frontend/warehouses/list_warehouses.html')


def orders(request):
    return render(request, 'frontend/orders.html')
