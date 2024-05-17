from django.contrib.auth.models import User
from django.db import models


class Role(models.Model):
    name = models.CharField(max_length=50, unique=True)
