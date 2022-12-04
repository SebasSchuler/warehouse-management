import uuid

from django.db import models


class ProductWarehouse(models.Model):
    warehouse_id = models.ForeignKey('Warehouse', null=False, on_delete=models.CASCADE)
    product_id = models.ForeignKey('Product', null=False, on_delete=models.CASCADE)


class Product(models.Model):
    id = models.CharField(primary_key=True, default=uuid.uuid4, editable=False, max_length=50)
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    price = models.DecimalField(default=0.00, decimal_places=2, max_digits=10)
    order_id = models.ForeignKey('Order', default=None, blank=True, null=True, on_delete=models.CASCADE)


class Warehouse(models.Model):
    id = models.CharField(primary_key=True, default=uuid.uuid4, editable=False, max_length=50)
    address = models.CharField(max_length=200)

class Order(models.Model):
    id = models.CharField(primary_key=True, default=uuid.uuid4, editable=False, max_length=50)
    email = models.CharField(max_length=200)
