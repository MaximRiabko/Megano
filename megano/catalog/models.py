from django.db import models

class Review(models.Model):
    description = models.TextField(null=False, blank=True)
    created_reviews = models.DateTimeField(auto_now_add=True)


class ViewedProduct(models.Model):
    name = models.CharField(max_length=50)


