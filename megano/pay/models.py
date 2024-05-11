from django.contrib.auth.models import User
from django.db import models

from order.models import PaymentStatus, Order
from shopapp.models import ProductSeller


class Transaction(models.Model):
    uuid = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_status = models.CharField(
        choices=PaymentStatus.choices, default=PaymentStatus.CANCELLED, max_length=100
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
