from django.contrib.auth.models import User
from django.db import models

from shopapp.models import ProductSeller


class PaymentChoices(models.TextChoices):
    CASH = ('cash', 'Cash')
    CREDIT_CARD = ('credit_card', 'Credit Card')

class DeliveryChoices(models.TextChoices):
    PICKUP = ('pickup', 'Pickup')
    COURIER = ('courier', 'Courier')

class Order(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.PROTECT, related_name='users')
    city = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    payment = models.CharField(choices=PaymentChoices.choices, default=PaymentChoices.CASH, max_length=2)
    payment_status = models.CharField(max_length=100)
    delivery = models.CharField(choices=DeliveryChoices.choices, default=DeliveryChoices.PICKUP, max_length=2)
    created_at = models.DateTimeField(auto_now_add=True)
    comment = models.CharField(max_length=200)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, null=True, blank=True, on_delete=models.CASCADE, related_name='orders')
    price = models.FloatField()
    old_price = models.FloatField()
    count = models.IntegerField()
    product = models.ForeignKey(ProductSeller, null=True, blank=True, on_delete=models.PROTECT, related_name='products')


