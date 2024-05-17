from django.urls import path

from .views import (
    order_step_1,
    order_step_2,
    payment_card,
    payment_invoice,
    proof_payment,
)

app_name = "pay"

urlpatterns = [
    # path("", order_view, name="order"),
    path("step_1/", order_step_1, name="step_1"),
    path("step_2/", order_step_2, name="step_2"),
    path("payment/", payment_card, name="payment"),
    path("paymentsomeone/", payment_invoice, name="paymentsomeone"),
    path("progressPayment/", proof_payment, name="progressPayment"),
]
