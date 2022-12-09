import json
from decimal import Decimal

from django.contrib.auth.models import User
from django.test import TestCase

from django.test import Client
from unicodedata import decimal

from manager.models import Product, Warehouse, Order


class ProductTestCase(TestCase):
    def setUp(self):
        self.warehouse_1 = Warehouse.objects.create(address="address-test")
        self.product_1 = Product.objects.create(id="745ed4a9-ba4a-4bfd-a775-fbeb83f8a98t", name="product-test",
                                                description="this is a test description", price=1.23,
                                                warehouse_id=self.warehouse_1)
        self.order_1 = Order.objects.create(id="4e293115-6717-46a7-8136-4ce695dddda1", email="email-test")
        my_admin = User.objects.create_superuser("admin", "admin@test.com", "admin")

    def test_list_product(self):
        c = Client()
        c.login(username="admin", password="admin")
        request = c.get('/manager/products/')
        self.assertEqual(request.status_code, 200)

    def test_get_product(self):
        c = Client()
        c.login(username="admin", password="admin")
        request = c.get('/manager/product/745ed4a9-ba4a-4bfd-a775-fbeb83f8a98t')
        self.assertEqual(request.status_code, 200)
    def test_add_product(self):
        c = Client()
        c.login(username="admin", password="admin")
        body = {"name": "product-test-1", "description": "this is a test description",
                "warehouse_id": self.warehouse_1.id}

        request = c.post('/manager/product/create/', body)
        self.assertEqual(request.status_code, 200)

    def test_delete_product(self):
        c = Client()
        c.login(username="admin", password="admin")
        request = c.delete('/manager/product/delete/745ed4a9-ba4a-4bfd-a775-fbeb83f8a98t')
        self.assertEqual(request.status_code, 202)

    def test_update_product(self):
        c = Client()
        c.login(username="admin", password="admin")
        body = {"name": "product-test-updated", "description": "this is a test description",
                "warehouse_id": self.warehouse_1.id}

        request = c.post('/manager/product/update/745ed4a9-ba4a-4bfd-a775-fbeb83f8a98t', body)
        self.assertEqual(request.status_code, 200)

    def test_list_warehouses(self):
        c = Client()
        c.login(username="admin", password="admin")
        request = c.get('/manager/warehouses/')
        self.assertEqual(request.status_code, 200)

    def test_get_warehouse(self):
        c = Client()
        c.login(username="admin", password="admin")
        request = c.get('/manager/warehouse/'+str(self.warehouse_1.id))
        self.assertEqual(request.status_code, 200)

    def test_add_warehouse(self):
        c = Client()
        c.login(username="admin", password="admin")
        body = {"address": "address-test-1"}

        request = c.post('/manager/warehouse/create/', body)
        self.assertEqual(request.status_code, 200)

    def test_delete_warehouse(self):
        c = Client()
        c.login(username="admin", password="admin")
        request = c.delete('/manager/warehouse/delete/'+str(self.warehouse_1.id))
        self.assertEqual(request.status_code, 202)

    def test_update_warehouse(self):
        c = Client()
        c.login(username="admin", password="admin")
        body = {"address": "warehouse-test-updated"}

        request = c.post('/manager/warehouse/update/'+str(self.warehouse_1.id), body)
        self.assertEqual(request.status_code, 200)

    def test_list_orders(self):
        c = Client()
        c.login(username="admin", password="admin")
        request = c.get('/manager/orders/')
        self.assertEqual(request.status_code, 200)

    def test_get_order(self):
        c = Client()
        c.login(username="admin", password="admin")
        request = c.get('/manager/order/4e293115-6717-46a7-8136-4ce695dddda1')
        self.assertEqual(request.status_code, 200)

    def test_add_order(self):
        c = Client()
        c.login(username="admin", password="admin")
        body = {"email": "email-test-1"}

        request = c.post('/manager/order/create/', body)
        self.assertEqual(request.status_code, 200)

