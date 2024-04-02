from django.contrib.auth.models import User
from django.db import models

from shopapp.models import ProductSeller


class Order(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.PROTECT, related_name='users')
    city = models.CharField(max_length=100)
    address = models.CharField(max_length=100)

    PAYMENT_CHOICES = [
        ('cash', 'Cash'),
        ('credit_card', 'Credit Card'),
    ]
    payment = models.CharField(choices=PAYMENT_CHOICES, max_length=100)

    payment_status = models.CharField(max_length=100)

    DELIVERY_CHOICES = [
        ('pickup', 'Pickup'),
        ('courier', 'Courier'),
    ]
    delivery = models.CharField(choices=DELIVERY_CHOICES, max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)
    comment = models.CharField(max_length=200)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, null=True, blank=True, on_delete=models.CASCADE, related_name='orders')
    price = models.FloatField()
    old_price = models.FloatField()
    count = models.IntegerField()
    product = models.ForeignKey(ProductSeller, null=True, blank=True, on_delete=models.PROTECT, related_name='products')


