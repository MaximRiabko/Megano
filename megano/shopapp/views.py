from django.shortcuts import render, get_object_or_404
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.core.cache import cache
from django.conf import settings
from django.views.generic import DetailView

from .models import Seller


@method_decorator(cache_page(60 * 60), name='dispatch')
class SellerDetailView(DetailView):
    model = Seller
    template_name = 'shopapp/seller_detail.html'
    context_object_name = 'seller'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        seller = self.get_object()
        top_products = get_top_products(seller)
        context['top_products'] = top_products
        return context


def get_top_products(seller):
    pass


