from django.shortcuts import render


def index(request):
    return render(request, 'frontend/index.html')


def list_products(request):
    return render(request, 'frontend/products/list_products.html')


def products(request):
    return render(request, 'frontend/products/products.html')


def list_products(request):
    return render(request, 'frontend/products/list_products.html')


def add_product(request):
    return render(request, 'frontend/products/add_product.html')


def update_product(request):
    return render(request, 'frontend/products/update_product.html')


def delete_product(request):
    return render(request, 'frontend/products/delete_product.html')


def warehouses(request):
    return render(request, 'frontend/warehouses/warehouses.html')


def list_warehouses(request):
    return render(request, 'frontend/warehouses/list_warehouses.html')


def add_warehouse(request):
    return render(request, 'frontend/warehouses/add_warehouse.html')


def update_warehouse(request):
    return render(request, 'frontend/warehouses/update_warehouse.html')


def delete_warehouse(request):
    return render(request, 'frontend/warehouses/delete_warehouse.html')


def orders(request):
    return render(request, 'frontend/orders/orders.html')
