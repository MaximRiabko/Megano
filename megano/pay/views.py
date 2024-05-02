import json

from django.shortcuts import render, redirect
from django.views.generic import UpdateView, CreateView

from pay.models import Transaction
from .forms import PaymentForm
from .tasks import process_payment

def payment_card(request):
    if request.method == 'GET':
        form = PaymentForm()
        return render(request, "pay/payment_card.html", {"form": form})
    elif request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            uuid = form.data['card_number']
            process_payment.delay(uuid)
            return redirect("pay:progressPayment")



def payment_invoice(request):
    if request.method == 'GET':
        form = PaymentForm()
        return render(request, "pay/payment_invoice.html", {"form": form})
    elif request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            uuid = form.data['card_number']
            process_payment.delay(uuid)
            return redirect("pay:progressPayment")


def proof_payment(request):
    return render(request, "pay/progress_payment.html")

