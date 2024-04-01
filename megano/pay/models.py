from django.contrib.auth.models import User
from django.db import models

from shopapp.models import ProductSeller

class Delivery(models.Model):
    name = models.CharField(max_length=100)

class Payment(models.Model):
    name = models.CharField(max_length=100)

class Order(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.PROTECT)
    city = models.CharField(max_length=100)
    address = models.CharField(max_length=100)

    PAYMENT_CHOICES = [
        ('cash', 'Cash'),
        ('credit_card', 'Credit Card'),
    ]
    payment = models.CharField(choices=PAYMENT_CHOICES)

    payment_status = models.CharField(max_length=100)

    DELIVERY_CHOICES = [
        ('pickup', 'Pickup'),
        ('courier', 'Courier'),
    ]
    delivery = models.CharField(choices=DELIVERY_CHOICES)

    created_at = models.DateTimeField(auto_now_add=True)
    comment = models.CharField(max_length=200)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, null=True, blank=True, on_delete=models.PROTECT)
    price = models.FloatField()
    old_price = models.FloatField()
    count = models.IntegerField()
    product = models.ForeignKey(ProductSeller, null=True, blank=True, on_delete=models.PROTECT)


