from django.shortcuts import render
from django.views.generic import View

def payment_card(request):
    return render(request, 'pay/payment_card.html')


def payment_invoice(request):
    return render(request, 'pay/payment_invoice.html')


def proof_payment(request):
    return render(request, 'pay/progress_payment.html')