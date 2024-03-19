from django.contrib import admin
from django.urls import path

from .views import SellerDetailView

appname = "shopapp"

urlpatterns = [
    path("about/<int:pk>/", SellerDetailView.as_view(), name="seller_detail"),
]
