from django.db import models
from django.utils.translation import gettext_lazy as _

# Синглтон модель
class SingletonModel(models.Model):
    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.__class__.objects.exclude(id=self.id).delete()
        super(SingletonModel, self).save(*args, **kwargs)

    @classmethod
    def load(cls):
        try:
            return cls.objects.get()
        except cls.DoesNotExist:
            return cls()


class SiteSettings(SingletonModel):
    name = models.CharField(max_length=100, unique=True)
    value = models.TextField()
    is_boolean = models.BooleanField(default=False)

    def __str__(self):
        return self.name