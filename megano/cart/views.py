from django.http import HttpRequest
from django.shortcuts import render
from .services import CartService

def add_to_cart(request: HttpRequest):
    cart_service = CartService()
    cart_service.add_to_cart("Product 1", 2)
    return render(request, "cart.html")
