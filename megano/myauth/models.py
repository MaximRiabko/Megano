from django.db import models


class Seller(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    image = models.ImageField(upload_to='seller_images/', blank=True, null=True)
    phone = models.IntegerField()
    address = models.IntegerField()
    email = models.EmailField()

