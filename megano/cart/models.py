from django.db import models

class ShoppingCart(models.Model):
    product_name = models.CharField(max_length=100)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.product_name} qt.-{self.quantity}"