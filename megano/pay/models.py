from django.contrib.auth.models import User
from django.db import models

from shopapp.models import ProductSeller

class Delivery(models.Model):
    name = models.CharField(max_length=100)

class Payment(models.Model):
    name = models.CharField(max_length=100)

class Order(models.Model):
    user_id = models.ForeignKey(User, null=True, blank=True, on_delete=models.PROTECT)
    city = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    payment_id = models.CharField(choices=Payment)
    payment_status = models.CharField(max_length=100)
    delivery_id = models.CharField(choices=Delivery)
    created_at = models.DateTimeField(auto_now_add=True)
    comment = models.CharField(max_length=200)

class OrderItem(models.Model):
    order_id = models.ForeignKey(Order, null=True, blank=True, on_delete=models.PROTECT)
    price = models.FloatField()
    old_price = models.FloatField()
    count = models.IntegerField()
    product = models.ForeignKey(ProductSeller, null=True, blank=True, on_delete=models.PROTECT)


