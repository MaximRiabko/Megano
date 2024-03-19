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


class Categories(models.Model):
    pass


def product_images_directory_path(instance: "ProductImage", filename: str) -> str:
    return "products/product_{pk}/images/{filename}".format(
        pk=instance.product.pk,
        filename=filename,
    )


class ProductImage(models.Model):
    """
    Модель ProductImage представляет изображение продукта.
    """
    image = models.ImageField(upload_to=product_images_directory_path)
    is_preview = models.BooleanField(default=False)


class Product(models.Model):
    """
    Модель Product представляет товар,
    который можно продавать в интернет-магазине.
    """

    name = models.CharField(max_length=100, db_index=True)
    description = models.TextField(null=False, blank=True)
    archived = models.BooleanField(default=False)
    preview = models.ForeignKey(ProductImage, on_delete=models.CASCADE)
    images = models.ManyToManyField(ProductImage, blank=True, related_name='products')
    category = models.ForeignKey(Categories, on_delete=models.PROTECT)


class ProductSeller(models.Model):
    """
    Модель ProductSeller представляет продукт с его ценой от продавца
    """
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    seller = models.ForeignKey(Seller, on_delete=models.PROTECT)
    price = models.DecimalField(default=0, max_digits=8, decimal_places=2)
    quantity = models.SmallIntegerField(default=0)
