from django.http import HttpRequest
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST

from shopapp.models import ProductSeller
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
            quantity=form_data['quantity'],
            update_quantity=form_data['update']
        )
    return redirect('cart:cart_detail')

def remove_cart(request, product_seller_id):
    cart = Cart(request)
    product_seller = get_object_or_404(ProductSeller, id=product_seller_id)
    cart.remove(product_seller=product_seller)
    return redirect('cart:cart_detail')

def cart_detail(request, product_seller_id):
    cart = Cart(request)
    context = {
        "cart": cart,
    }
    return render(request, 'cart/detail.html',context=context)