from django.urls import path
from .views import payment_card, payment_invoice, proof_payment

app_name = 'pay'

urlpatterns = [
    path('payment/', payment_card, name='payment'),
    path('paymentsomeone/', payment_invoice, name='paymentsomeone'),
    path('progressPayment/', proof_payment, name='progressPayment'),
]