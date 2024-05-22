from django.contrib.auth.models import User
from django.db import models

from shopapp.models import ProductSeller


class PaymentChoices(models.TextChoices):
    CASH = ("someone", "Someone")
    CREDIT_CARD = ("online", "Online")


class DeliveryChoices(models.TextChoices):
    PICKUP = ("pickup", "Pickup")
    COURIER = ("courier", "Courier")


class PaymentStatus(models.TextChoices):
    PAID = ("paid", "Paid")
    CANCELLED = ("cancelled", "Cancelled")


class TransactionStatus(models.TextChoices):
    PAID = ("paid", "Paid")
    RUNNING = ("running", "Running")
    CANCELLED = ("cancelled", "Cancelled")


class Order(models.Model):
    class Meta:
        get_latest_by = "created_at"

    user = models.ForeignKey(
        User, null=True, blank=True, on_delete=models.PROTECT, related_name="users"
    )
    city = models.CharField(max_length=100, null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    payment_type = models.CharField(
        choices=PaymentChoices.choices, default=PaymentChoices.CASH, max_length=100
    )
    payment_status = models.CharField(
        choices=PaymentStatus.choices, default=PaymentStatus.CANCELLED, max_length=100
    )
    delivery = models.CharField(
        choices=DeliveryChoices.choices, default=DeliveryChoices.PICKUP, max_length=100
    )
    created_at = models.DateTimeField(auto_now_add=True)
    comment = models.CharField(max_length=200, null=True, blank=True)
    reference_num = models.CharField(max_length=100, null=True, blank=True)


class OrderItem(models.Model):
    order = models.ForeignKey(
        Order,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="orders",
    )
    price = models.FloatField()
    old_price = models.DecimalField(max_digits=10, decimal_places=2)
    count = models.IntegerField(default=1)
    product = models.ForeignKey(
        ProductSeller,
        null=True,
        blank=True,
        on_delete=models.PROTECT,
        related_name="order_items",
    )


class Transaction(models.Model):
    uuid = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_status = models.CharField(
        choices=TransactionStatus.choices,
        default=TransactionStatus.RUNNING,
        max_length=100,
    )
    order = models.ForeignKey(
        Order,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="transaction",
    )
    user = models.ForeignKey(
        User, null=False, on_delete=models.PROTECT, related_name="transaction"
    )
