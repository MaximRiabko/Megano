from django.db import models


class Seller(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    image = models.ImageField(upload_to='seller_image_directory_path', blank=True, null=True)
    phone = models.IntegerField()
    address = models.CharField(max_length=255)
    email = models.EmailField()


def seller_image_directory_path(instance: "Seller", filename: str) -> str:
    return "sellers/seller_{pk}/image/{filename}".format(
        pk=instance.pk,
        filename=filename,
    )