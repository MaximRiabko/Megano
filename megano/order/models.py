from django.db import models
from django.contrib.auth.models import User

from shopapp.models import ProductSeller


class PaymentChoices(models.TextChoices):
    CASH = ("cash", "Cash")
    CREDIT_CARD = ("credit_card", "Credit Card")


class DeliveryChoices(models.TextChoices):
    PICKUP = ("pickup", "Pickup")
    COURIER = ("courier", "Courier")


class PaymentStatus(models.TextChoices):
    PAID = ("paid", "Paid")
    CANCELLED = ("cancelled", "Cancelled")


class Order(models.Model):
    class Meta:
        get_latest_by = "created_at"

    user = models.ForeignKey(
        User, null=True, blank=True, on_delete=models.PROTECT, related_name="orders"
    )
    city = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    payment = models.CharField(
        choices=PaymentChoices.choices, default=PaymentChoices.CASH, max_length=100
    )
    payment_status = models.CharField(
        choices=PaymentStatus.choices, default=PaymentStatus.CANCELLED, max_length=100
    )
    delivery = models.CharField(
        choices=DeliveryChoices.choices, default=DeliveryChoices.PICKUP, max_length=100
    )
    created_at = models.DateTimeField(auto_now_add=True)
    comment = models.CharField(max_length=200)
    reference_num = models.CharField(max_length=100)


class OrderItem(models.Model):
    order = models.ForeignKey(
        Order,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="items",
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