import datetime
from django.test import TestCase
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
from django.contrib.auth import get_user_model
from .models import (
    Product,
    Categories,
    ProductImage,
    Seller,
    Discount,
)
from pay.models import Order


User = get_user_model()

class HistoryOrderTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.credentials = dict(username="test name", password="qwerty")
        cls.user = User.objects.create_user(**cls.credentials)

    @classmethod
    def tearDownClass(cls):
        cls.user.delete()

    def setUp(self) -> None:
        self.client.login(**self.credentials)

    def test_history_order(self):
        responce = self.client.get(reverse("shopapp:history_order"))
        for history in Order.objects.all():
            self.assertContains(responce, history.user)
            self.assertContains(responce, history.city)
            self.assertContains(responce, history.address)
            self.assertContains(responce, history.payment_type)
            self.assertContains(responce, history.payment_status)
            self.assertContains(responce, history.delivery)
            self.assertContains(responce, history.created_at)
            self.assertContains(responce, history.comment)
            self.assertContains(responce, history.reference_num)
            self.assertTemplateUsed(responce, "shopapp/historyorder.html")

class LastOrderDetailViewTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.last_order = User.objects.create(
            username="Test name",
            password="password",
        )
    @classmethod
    def tearDownClass(cls):
        cls.last_order.delete()

    def test_get_last_order(self):
        self.client.get(
            reverse("shopapp:last_order_details", kwargs={"pk": self.last_order.pk})
        )

class OrderDetailViewTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.user = User.objects.create(
            username="Test name",
            password="password",
        )
        cls.order = Order.objects.create(
            user=cls.user,
            city="Test city",
            address="UL. Test, D.18",
            delivery="Delivery Test",
            payment_type="Cash",
            payment_status="Cancelled",
            created_at=datetime.date(2024, 5, 1),
            comment="Test Order Comment",
            reference_num="reference num test",
        )
    @classmethod
    def tearDownClass(cls):
        cls.order.delete()

    def test_get_order(self):
        self.client.get(
            reverse("shopapp:order_details", kwargs={"pk": self.order.pk})
        )
class AccountDetailViewTestCase(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.account = User.objects.create(
            username="Test name",
            password="password",
        )

    @classmethod
    def tearDownClass(cls):
        cls.account.delete()

    def test_get_account(self):
        self.client.get(
            reverse("shopapp:profile", kwargs={"pk": self.account.pk})
        )

class DiscountDetailViewTestCase(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.discount = Discount.objects.create(
            name="Test Discount",
            description="Test description Discount",
            promocode="SALE 999",
            date_start=datetime.date(2024, 5, 1),
            date_end=datetime.date(2024, 7, 3),
            value=875,
            image=SimpleUploadedFile(
                "Test Discount.jpg",
                content=b'',
                content_type="image/jpg"
            ),
        )

    @classmethod
    def tearDownClass(cls):
        cls.discount.delete()

    def test_get_discount(self):
        self.client.get(
            reverse("shopapp:discount_details", kwargs={"pk": self.discount.pk})
        )

class DiscountListViewTestCase(TestCase):
    def test_discount(self):
        responce = self.client.get(reverse("shopapp:discounts"))
        for discount in Discount.objects.all():
            self.assertContains(responce, discount.name)
            self.assertContains(responce, discount.description)
            self.assertContains(responce, discount.products)
            self.assertContains(responce, discount.date_start)
            self.assertContains(responce, discount.date_end)
            self.assertContains(responce, discount.promocode)
            self.assertContains(responce, discount.is_group)
            self.assertContains(responce, discount.is_active)
            self.assertContains(responce, discount.value)
            self.assertContains(responce, discount.type)
            self.assertContains(responce, discount.image)
            self.assertTemplateUsed(responce, "shopapp/discount_list.html")

class SellerDetailViewTestCase(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.seller = Seller.objects.create(
            name="Test name Seller",
            description="Test description seller",
            image=SimpleUploadedFile(
                "Test seller.jpg",
                content=b'',
                content_type="image/jpg"
            ),
            phone=+79998887766,
            address="Ul. Test",
            email="test@gmail.com"
        )

    @classmethod
    def tearDownClass(cls) -> None:
        cls.seller.delete()

    def test_get_seller(self):
        self.client.get(
            reverse("shopapp:seller_detail", kwargs={"pk": self.seller.pk})
        )



class ProductDetailViewTestCase(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.categories = Categories.objects.create(name="Smartphone")
        cls.preview = ProductImage.objects.create()
        cls.product = Product.objects.create(
            name="Test name product",
            description="Test description product",
            category=cls.categories,
            preview=cls.preview,
        )
    @classmethod
    def tearDownClass(cls):
        cls.product.delete()

    def test_get_product(self):
        self.client.get(
            reverse("shopapp:product", kwargs={"pk": self.product.pk})
        )



