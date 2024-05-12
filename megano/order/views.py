from django.shortcuts import render
from .models import Order
from cart.cart import Cart


def order_view(request):
    cart = Cart(request)
    context = {'cart': cart}
    return render(request, "order/order.html", context=context)