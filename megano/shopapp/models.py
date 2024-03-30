from django.db import models
from django.contrib.auth.models import User


class Seller(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    image = models.ImageField(
        upload_to="seller_image_directory_path", blank=True, null=True
    )
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
    images = models.ManyToManyField(ProductImage, blank=True, related_name="products")
    category = models.ForeignKey(Categories, on_delete=models.PROTECT)


class ProductSeller(models.Model):
    """
    Модель ProductSeller представляет продукт с его ценой от продавца
    """

    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    seller = models.ForeignKey(Seller, on_delete=models.PROTECT)
    price = models.DecimalField(default=0, max_digits=8, decimal_places=2)
    quantity = models.SmallIntegerField(default=0)
    sale = models.IntegerField(blank=True, default=0)

    def get_sale(self):
        """Функция рассчитывает стоимость со скидкой"""
        price = int(self.price * (100 - self.sale) / 100)
        return price


class ViewHistory(models.Model):
    """
    Модель ViewHistory представляет историю просмотренных продуктов
    """

    user = models.ForeignKey(User, on_delete=models.PROTECT)
    creation_date = models.DateTimeField(auto_now_add=True)
    viewed_products = models.ManyToManyField(Product)


class Discount(models.Model):
    """
    Модель ViewHistory представляет скидку на продукт
    """

    name = models.CharField(max_length=255)
    description = models.TextField(null=False, blank=True)
    products = models.ManyToManyField(Product)
    date_start = models.DateTimeField(auto_now_add=True)
    date_end = models.DateTimeField()
    promocode = models.CharField(max_length=255)
    is_group = models.BooleanField(default=False)
    value = models.DecimalField(default=0, max_digits=8, decimal_places=2)
    type = models.CharField(max_length=255)

class Review(models.Model):
    """Модель Review представляет отзывы на продукт"""
    author = models.ForeignKey(User, null=True, on_delete=models.PROTECT)
    product = models.ForeignKey(Product, null=True, on_delete=models.PROTECT)
    content = models.TextField(null=False, blank=True)
    created_reviews = models.DateTimeField(auto_now_add=True)