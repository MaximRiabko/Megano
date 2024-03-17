from django.shortcuts import render
from django.http import HttpRequest
from .models import Review, ViewedProduct

def adding_review(request: HttpRequest):
    context = {
        "reviews": Review.objects.all(),
    }
    return render(request, 'catalog/product_reviews.html', context=context)

def viewed_products(request: HttpRequest):
    context = {
        "vieweds": ViewedProduct.objects.all(),
    }
    return render(request, 'catalog/viewed_products.html', context=context)