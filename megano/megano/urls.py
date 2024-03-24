from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('catalog/', include('catalog.urls')),
    path('pay/', include('pay.urls')),
    path("shop/", include("shopapp.urls")),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
