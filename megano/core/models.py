from django.db import models

class SiteSettings(models.Model):
    name = models.CharField(max_length=100, unique=True)
    value = models.TextField()
    is_boolean = models.BooleanField(default=False)

    def __str__(self):
        return self.name