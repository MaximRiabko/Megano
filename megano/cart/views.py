from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from django.views.decorators.http import require_POST
from django.core.exceptions import ObjectDoesNotExist
from shopapp.models import Discount, ProductSeller, DiscountTypeChoices

from .cart import Cart
from .forms import CartAddProductForm


@require_POST
def cart_add(request, product_seller_id):
    cart = Cart(request)
    product_seller = get_object_or_404(ProductSeller, id=product_seller_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        form_data = form.cleaned_data
        cart.add(
            product_seller=product_seller,
            quantity=form_data["quantity"],
            update_quantity=form_data["update"],
        )
    return redirect("cart:cart_detail")


def remove_cart(request, product_seller_id):
    cart = Cart(request)
    product_seller = get_object_or_404(ProductSeller, id=product_seller_id)
    cart.remove(product_seller=product_seller)
    return redirect("cart:cart_detail")


def set_discounted_product(discount: Discount, cart: Cart):
    for item in cart.cart.values():
        item['old_price'] = item['price']
        product_price = float(item['price'])
        if discount.type == DiscountTypeChoices.PERCENT.value:
            item['price'] = product_price - (product_price * float(discount.value) / 100)
        elif discount.type == DiscountTypeChoices.RUBLES.value:
            item['price'] = product_price - float(discount.value)


def cart_detail(request):
    cart = Cart(request)
    context = {
        "cart": cart
    }
    if request.method == "POST":
        input_promocode = request.POST.get("promocode")
        if input_promocode:
            discount = Discount.objects.filter(promocode=input_promocode).first()
            if discount is not None:
                set_discounted_product(discount, cart)
                return render(request, "cart/cart_detail_with_discount.html", context=context)
    return render(request, "cart/cart_detail.html", context=context)
