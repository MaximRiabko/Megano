from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from megano.settings import ON_PAYMENT

from .forms import PaymentForm

from django.shortcuts import render, redirect
from .models import Order
from cart.cart import Cart



def order_view(request):
    if request.method == 'GET':



        return render(request, "pay/order.html")

    if request.method == 'POST':
        data = request.POST
        cart = Cart(request)
        context = {"cart": cart}
        # request.POST содержит:
        # <QueryDict: {'csrfmiddlewaretoken': ['CtqbedzZMgi8TOSDHMNUZ5ZIR12EEA04DNQn7TnitUo1zZ3OMwxfjtC6jhpvimfm'],
        #              'name': ['asdasd'],
        #              'phone': ['asdasd'],
        #              'mail': ['Sam_ctc'],
        #              'password': ['Djghjc871'],
        #              'passwordReply': ['asdasd'],
        #              'delivery': ['ordinary'],
        #              'city': ['asdasd'],
        #              'address': ['asdasda'],
        #              'pay': ['online']
        #              }>

        name = data.get('name')
        phone = data.get('phone')
        mail = data.get('mail')
        city = data.get('city')
        address = data.get('address')
        delivery = data.get('delivery')
        pay_type = data.get('pay')


        if pay_type == 'online':
            return redirect("pay:payment", context=context)
        else:
            return redirect("pay:paymentsomeone", context=context)

def order_step_1(request):
    if request.user.is_authenticated:
        return redirect('pay:step_2')
    return render(request, "pay/order_step_1.html")

@login_required
def order_step_2(request):
    return render(request, "pay/order_step_2.html")


def payment_card(request):
    if request.method == "GET":
        form = PaymentForm()
        return render(request, "pay/payment_card.html", {"form": form})
    elif request.method == "POST":
        form = PaymentForm(request.POST)
        if form.is_valid():
            if ON_PAYMENT:
                from .tasks import process_payment

                uuid = form.data["card_number"]
                process_payment.delay(uuid)
            return redirect("pay:progressPayment")


def payment_invoice(request):
    if request.method == "GET":
        form = PaymentForm()
        return render(request, "pay/payment_invoice.html", {"form": form})
    elif request.method == "POST":
        form = PaymentForm(request.POST)
        if form.is_valid():
            if ON_PAYMENT:
                from .tasks import process_payment

                uuid = form.data["card_number"]
                process_payment.delay(uuid)
            return redirect("pay:progressPayment")


def proof_payment(request):
    return render(request, "pay/progress_payment.html")
