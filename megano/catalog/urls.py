from django.urls import path
from .views import adding_review, viewed_products, delete_review

app_name = 'catalog'

urlpatterns = [
    path('', adding_review, name='product_review'),
    path('delete_review/', delete_review, name='review_delete'),
    path('viewed/', viewed_products, name='viewed_prodcuts'),
]