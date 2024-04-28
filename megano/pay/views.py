import json

from django.shortcuts import render
from django.views.generic import UpdateView, CreateView

from pay.models import Transaction
from .tasks import process_payment

def payment_card(request):
    if request.method == 'GET':
        return render(request, "pay/payment_card.html")
    elif request.method == 'POST':
        body_data = json.loads(request.body)
        transaction_id = body_data["transaction_id"]
        process_payment.delay(transaction_id)


def payment_invoice(request):
    if request.method == 'GET':
        return render(request, "pay/payment_invoice.html")
    elif request.method == 'POST':
        body_data = json.loads(request.body)
        transaction_id = body_data["transaction_id"]
        process_payment.delay(transaction_id)


def proof_payment(request):
    return render(request, "pay/progress_payment.html")

