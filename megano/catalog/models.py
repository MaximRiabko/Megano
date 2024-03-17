from django.db import models
from django.contrib.auth.models import User
class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(null=False, blank=True)
    created_reviews = models.DateTimeField(auto_now_add=True)


class ViewedProduct(models.Model):
    name = models.CharField(max_length=50)


