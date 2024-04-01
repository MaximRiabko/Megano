from django.db import models

from shopapp.models import ProductSeller

class Order(models.Model):
    price = models.FloatField()
    old_price = models.FloatField()
    count = models.IntegerField()
    product = models.ForeignKey(ProductSeller)

