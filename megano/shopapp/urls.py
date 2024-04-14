from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import (
    AccountDetailView,
    DiscountListView,
    HistoryOrder,
    MainPageView,
    OrderDetailView,
    ProfileUpdateView,
    SellerDetailView,
)

app_name = "shopapp"

urlpatterns = [
    path("", MainPageView.as_view(), name="index"),
    path("about/<int:pk>/", SellerDetailView.as_view(), name="seller_detail"),
    path("discounts/", DiscountListView.as_view(), name="discounts"),
    path("profile/details/", AccountDetailView.as_view(), name="profile"),
    path("profile/details/update/", ProfileUpdateView.as_view(), name="profile_update"),
    path("profile/order/history/", HistoryOrder.as_view(), name="history_order"),
    path(
        "profile/order/history/<int:pk>",
        OrderDetailView.as_view(),
        name="order_details",
    ),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
