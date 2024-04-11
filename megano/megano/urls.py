from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("pay/", include("pay.urls")),
    path("shop/", include("shopapp.urls", namespace="shopapp")),
    path("auth/", include("user.urls")),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
