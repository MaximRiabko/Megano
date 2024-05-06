from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("cart/", include("cart.urls")),
    path("pay/", include("pay.urls")),
    path("shop/", include("shopapp.urls", namespace="shopapp")),
    path("auth/", include("user.urls", namespace="auth")),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns.extend(static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT))
