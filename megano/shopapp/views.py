from django.conf import settings
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.models import User
from django.core.cache import cache
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from django.views import View
from django.views.decorators.cache import cache_page
from django.views.generic import DetailView, ListView, TemplateView, UpdateView
from django.views.generic.edit import FormMixin

from .models import Discount, Profile, Review, Seller, ViewHistory, Product
from .forms import ReviewForm

class ProductDetailView(FormMixin, DetailView,):
    """Класс детальной страницы товаров"""
    model = Product
    template_name = "shopapp/product_detail.html"
    context_object_name = "product"
    form_class = ReviewForm
    success_msg = "Отзыв успешно создан"

    def get_success_url(self, **kwargs):
        return reverse_lazy("shopapp:product", kwargs={"pk": self.get_object().id})
    def post(self, request: HttpRequest, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.product = self.get_object()
        self.object.save()
        return super().form_valid(form)



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


class DiscountListView(ListView):
    model = Discount
    template_name = "shopapp/discount_list.html"


class AccountDetailView(DetailView):
    model = Profile
    template_name = "shopapp/account.html"
    context_object_name = "profile"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
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
