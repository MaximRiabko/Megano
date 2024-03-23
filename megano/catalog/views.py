from django.shortcuts import render
from django.http import HttpRequest
from .models import Review, ViewedProduct
from .forms import ReviewForm

def adding_review(request: HttpRequest):
    """Функция для обработки формы товара,
    и отображения отзывов на странице"""
    error = ''
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            error = 'Неправильно введён отзыв!'


    form = ReviewForm
    context = {
        "reviews": Review.objects.all(),
        "form": form,
        "error": error
    }
    return render(request, 'catalog/product_reviews.html', context=context,)

def viewed_products(request: HttpRequest):
    context = {
        "vieweds": ViewedProduct.objects.all(),
    }
    return render(request, 'catalog/viewed_products.html', context=context)