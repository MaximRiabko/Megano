import json

from django.http import HttpResponse, JsonResponse

from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView, ListView, TemplateView, UpdateView


from .comparison import Comparison
from .models import Discount, Profile, Seller, ViewHistory, Product, ProductSeller


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

#
# def compare_view(request):
#     products = Comparison(request)  # Получаем товары для сравнения из сессии
#     return render(request, 'shopapp/comparison.html', {'products': products})
#


class CompareView(TemplateView):
    template_name = 'shopapp/comparison.html'
    def get_context_data(self, **kwargs):
        context = super(CompareView, self).get_context_data(**kwargs)
        context['products'] = Comparison(self.request)
        return context

@csrf_exempt
def compare_manager(request):
    body_data = json.loads(request.body)
    pk = body_data['product_pk']

    if request.method == 'POST':
        product = ProductSeller.objects.filter(product_id=pk).prefetch_related('product').first()
        Comparison(request).add(product)
        return JsonResponse({'status': 'ok'})

    if request.method == "DELETE":
        product = ProductSeller.objects.filter(product_id=pk).prefetch_related('product').first()
        Comparison(request).remove(product)
        return JsonResponse({'status': 'ok'})
