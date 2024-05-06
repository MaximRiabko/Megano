from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import (
    AccountDetailView,
    CompareManager,
    CompareView,
    DiscountDetailView,
    DiscountListView,
    HistoryOrder,
    LastOrderDetailView,
    MainPageView,
    OrderDetailView,
    ProductDetailView,
    ProfileUpdateView,
    SellerDetailView,
    catalog,
    filter_products,
)

app_name = "shopapp"

urlpatterns = [
    path("", MainPageView.as_view(), name="index"),
    path("about/<int:pk>/", SellerDetailView.as_view(), name="seller_detail"),
    path("discounts/", DiscountListView.as_view(), name="discounts"),
    path("products/<int:pk>", ProductDetailView.as_view(), name="product"),
    path("profile/<int:pk>/details/", AccountDetailView.as_view(), name="profile"),
    path("comparison/", CompareView.as_view(), name="compare"),
    path(
        "comparison/compare_manager/", CompareManager.as_view(), name="compare_manager"
    ),
    path(
        "discounts/<int:pk>",
        DiscountDetailView.as_view(),
        name="discount_details",
    ),
    path("profile/details/<int:pk>", AccountDetailView.as_view(), name="profile"),
    path("profile/details/update/", ProfileUpdateView.as_view(), name="profile_update"),
    path("profile/order/history/", HistoryOrder.as_view(), name="history_order"),
    path(
        "profile/order/history/<int:pk>",
        OrderDetailView.as_view(),
        name="order_details",
    ),
    path("categories/products/<int:pk>", catalog, name="catalog"),
    path(
        "profile/<int:pk>/order/last/",
        LastOrderDetailView.as_view(),
        name="last_order_details",
    ),
    path(
        "categories/products/filtered-products/",
        filter_products,
        name="filter-products",
    ),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
