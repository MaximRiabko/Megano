from django.shortcuts import render, redirect
from .forms import PaymentForm
from .tasks import process_payment
from megano.megano.settings import ON_PAYMENT

def payment_card(request):
    if request.method == 'GET':
        form = PaymentForm()
        return render(request, "pay/payment_card.html", {"form": form})
    elif request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            if ON_PAYMENT:
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
            if ON_PAYMENT:
                uuid = form.data['card_number']
                process_payment.delay(uuid)
            return redirect("pay:progressPayment")


def proof_payment(request):
    return render(request, "pay/progress_payment.html")

