from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from .views import (
    AccountDetailView,
    DiscountListView,
    SellerDetailView,
    ProductDetailView,
)

app_name = "shopapp"

urlpatterns = [
    path("about/<int:pk>/", SellerDetailView.as_view(), name="seller_detail"),
    path("discounts/", DiscountListView.as_view(), name="discounts"),
    path("products/<int:pk>", ProductDetailView.as_view(), name="product"),
    path("profile/<int:pk>/details/", AccountDetailView.as_view(), name="profile"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
