from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from .views import AccountDetailView, DiscountListView, SellerDetailView, MainPageView, ProfileUpdateView

app_name = "shopapp"

urlpatterns = [
    path("", MainPageView.as_view(), name="index"),
    path("about/<int:pk>/", SellerDetailView.as_view(), name="seller_detail"),
    path("discounts/", DiscountListView.as_view(), name="discounts"),
    path("profile/<int:pk>/details/", AccountDetailView.as_view(), name="profile"),
    path("profile/details/update/", ProfileUpdateView.as_view(), name="profile_update"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
