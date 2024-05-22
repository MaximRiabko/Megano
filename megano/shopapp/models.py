from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.db import models


class Seller(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    image = models.ImageField(
        upload_to="seller_image_directory_path", blank=True, null=True
    )
    phone = models.IntegerField()
    address = models.CharField(max_length=255)
    email = models.EmailField()

    def __str__(self):
        return self.name


def seller_image_directory_path(instance: "Seller", filename: str) -> str:
    return "sellers/seller_{pk}/image/{filename}".format(
        pk=instance.pk,
        filename=filename,
    )


class Categories(models.Model):
    name = models.CharField(max_length=255, default="")
    archived = models.BooleanField(default=False)
    parent = models.ForeignKey(
        "self",
        null=True,
        blank=True,
        related_name="subcategories",
        on_delete=models.PROTECT,
    )

    def __str__(self):
        return self.name


def product_images_directory_path(instance: "ProductImage", filename: str) -> str:
    return "products/images/{filename}".format(
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
    category = models.ForeignKey(
        Categories, on_delete=models.PROTECT, related_name="products"
    )
    details = models.JSONField(blank=True, verbose_name="Характеристики", default=dict)

    def __str__(self) -> str:
        return f"Product(pk={self.pk}, name={self.name!r})"


class ProductSeller(models.Model):
    """
    Модель ProductSeller представляет продукт с его ценой от продавца
    """

    product = models.ForeignKey(
        Product, on_delete=models.PROTECT, related_name="product_sellers"
    )
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

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="view_historys"
    )
    creation_date = models.DateTimeField(auto_now_add=True)
    product = models.ForeignKey(
        Product,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name="view_historys",
    )


def discount_img_directory_path(instance: "Discount", filename: str) -> str:
    return "discounts/discount_{pk}/image/{filename}".format(
        pk=instance.pk, filename=filename
    )


class DiscountTypeChoices(models.TextChoices):
    PERCENT = ("%", "%")
    RUBLES = ("RUB", "RUB")


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
    is_active = models.BooleanField(default=False)
    value = models.DecimalField(default=0, max_digits=8, decimal_places=2)
    type = models.CharField(
        choices=DiscountTypeChoices.choices,
        default=DiscountTypeChoices.PERCENT,
        max_length=100,
    )
    image = models.ImageField(
        null=True, blank=True, upload_to=discount_img_directory_path
    )

    def __str__(self) -> str:
        return f"Discount(pk={self.pk}, name={self.name!r})"


class Review(models.Model):
    """Модель Review представляет отзывы на продукт"""

    author = models.ForeignKey(User, null=True, on_delete=models.PROTECT)
    product = models.ForeignKey(
        Product, null=True, on_delete=models.PROTECT, related_name="reviews_product"
    )
    content = models.TextField(null=False, blank=True)
    created_reviews = models.DateTimeField(auto_now_add=True)


def avatar_directory_path(instance: "Profile", filename: str) -> str:
    return "users/user_{pk}/avatar/{filename}".format(pk=instance.pk, filename=filename)


class Profile(models.Model):
    """
    Модель Profile представляет профиль пользователя
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(null=True, blank=True, upload_to=avatar_directory_path)
    phone_regex = RegexValidator(
        regex=r"^\+?1?\d{9,15}$",
        message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.",
    )
    phone = models.CharField(
        validators=[phone_regex], max_length=17, blank=True
    )  # Validators should be a list
    middle_name = models.CharField(max_length=255, null=True, blank=True)
    seller = models.ForeignKey(Seller, on_delete=models.PROTECT, null=True, blank=True)
