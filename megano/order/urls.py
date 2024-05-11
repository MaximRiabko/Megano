from django.urls import path

from .views import order_view

app_name = "order"

urlpatterns = [
    path("", order_view, name="order"),
]

