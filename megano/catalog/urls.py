from django.urls import path
from .views import adding_review, viewed_products

app_name = 'catalog'

urlpatterns = [
    path('', adding_review, name='product'),
    path('viewed/', viewed_products, name='viewed_prodcuts')
]