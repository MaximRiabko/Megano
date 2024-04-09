from io import BytesIO

from django.conf import settings
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.models import User
from django.contrib.sites import requests
from django.core.cache import cache
from django.core.files import File
from django.core.files.storage import FileSystemStorage
from django.db.models import Count
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.template.defaulttags import url
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.cache import cache_page
from django.views.generic import DetailView, ListView, TemplateView, UpdateView

from pay.models import OrderItem

from .models import Discount, ProductSeller, Profile, Review, Seller, ViewHistory


@method_decorator(cache_page(60 * 60), name="dispatch")
class SellerDetailView(DetailView):
    model = Seller
    template_name = "shopapp/seller_detail.html"
    context_object_name = "seller"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        seller = self.get_object()
        top_products = get_top_products(seller)
        context["top_products"] = top_products
        return context


def get_top_products(seller):
    pass


def get_discounted_product():
    pass


class DiscountListView(ListView):
    model = Discount
    template_name = "shopapp/discount_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        discounts = Discount.objects\
            .only('name', 'description', 'date_start', 'date_end')\
            .prefetch_related('products')
        context["discounts"] = discounts
        return context


class AccountDetailView(UserPassesTestMixin, DetailView):
    template_name = "shopapp/account.html"

    def test_func(self):
        return self.request.user.is_authenticated

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["profile"] = self.request.user.profile
        view_history = None
        view_history = ViewHistory.objects.prefetch_related("viewed_products").order_by(
            "-creation_date"
        )[:3]
        three_viewed = []
        for history in view_history:
            for product in history.viewed_products.all():
                three_viewed.append(product)

        context["three_viewed"] = three_viewed
        return context


class ProfileUpdateView(UserPassesTestMixin, TemplateView):
    template_name = "shopapp/profile.html"

    def test_func(self):
        return self.request.user.is_authenticated

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context["user"] = user
        return context

    def post(self, request: HttpRequest) -> HttpResponse:
        user = self.request.user
        if request.method == "POST":
            if request.FILES:
                image = request.FILES["avatar"]
                fs = FileSystemStorage(
                    location=f"/uploads/users/user_{self.request.user.pk}/avatar/{image.name}"
                )
                img_name = fs.save(image.name, image)
                img_url = fs.url(img_name)
                user.profile.avatar = img_url

            user.username = request.POST.get("name")
            if request.POST.get("password") == request.POST.get("passwordReply"):
                user.password = request.POST.get("password")
            user.email = request.POST.get("mail")
            user.profile.phone = request.POST.get("phone")
            user.profile.phone = request.POST.get("phone")
            user.save()
            user.profile.save()
        return redirect(request.path)


class MainPageView(TemplateView):
    template_name = "shopapp/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        top_order_products = ProductSeller.objects.annotate(
            cnt=Count("order_items")
        ).order_by("-cnt")[:8]
        context["top_order_products"] = top_order_products
        return context
