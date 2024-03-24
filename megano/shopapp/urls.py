from django.contrib import admin
from django.urls import path

from .views import SellerDetailView, DiscountListView

appname = "shopapp"

urlpatterns = [
    path("about/<int:pk>/", SellerDetailView.as_view(), name="seller_detail"),
    path("discounts/", DiscountListView.as_view(), name="discounts"),
]
