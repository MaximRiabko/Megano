from django.shortcuts import render
from django.views.generic import UpdateView, CreateView

from pay.models import Transaction
from .tasks import process_payment

def payment_card(request):
    return render(request, "pay/payment_card.html")


def payment_invoice(request):
    return render(request, "pay/payment_invoice.html")


def proof_payment(request):
    print(request)
    return render(request, "pay/progress_payment.html")

class PaymentCard(CreateView):
    model = Transaction
    success_url = ""
    template_name = 'pay/payment_card.html'

    def form_valid(self, form):
        form.save()
        process_payment.delay(form.instance)
        return super().form_valid(form)