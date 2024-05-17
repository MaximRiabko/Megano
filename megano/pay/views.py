from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import redirect, render

from megano.settings import ON_PAYMENT

from shopapp.models import Profile
from .forms import PaymentForm

from django.shortcuts import render, redirect
from .models import Order
from cart.cart import Cart
from .forms import UserRegistrationForm



# def order_view(request):
#     if request.method == 'GET':
#
#         return render(request, "pay/order.html")
#
#     if request.method == 'POST':
#         data = request.POST
#         cart = Cart(request)
#         context = {"cart": cart}
#         # request.POST содержит:
#         # <QueryDict: {'csrfmiddlewaretoken': ['CtqbedzZMgi8TOSDHMNUZ5ZIR12EEA04DNQn7TnitUo1zZ3OMwxfjtC6jhpvimfm'],
#         #              'name': ['asdasd'],
#         #              'phone': ['asdasd'],
#         #              'mail': ['Sam_ctc'],
#         #              'password': ['Djghjc871'],
#         #              'passwordReply': ['asdasd'],
#         #              'delivery': ['ordinary'],
#         #              'city': ['asdasd'],
#         #              'address': ['asdasda'],
#         #              'pay': ['online']
#         #              }>
#
#         name = data.get('name')
#         phone = data.get('phone')
#         mail = data.get('mail')
#         city = data.get('city')
#         address = data.get('address')
#         delivery = data.get('delivery')
#         pay_type = data.get('pay')
#
#
#         if pay_type == 'online':
#             return redirect("pay:payment", context=context)
#         else:
#             return redirect("pay:paymentsomeone", context=context)

def order_step_1(request):
    context = {
        'form_user': UserRegistrationForm,
    }
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect('pay:step_2')
        return render(request, "pay/order_step_1.html", context=context)
    elif request.method == "POST":
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            name = user_form.cleaned_data['username']
            email = user_form.cleaned_data['email']
            password = user_form.cleaned_data['password']
            phone = user_form.cleaned_data['phone']
            user = User.objects.create_user(
                username=email, first_name=name, email=email, password=password
            )
            user.save()
            profile = Profile.objects.create(user=user, phone=phone)
            profile.save()

            new_user = authenticate(request=request, username=email, password=password)
            if new_user:
                login(request, new_user)
                return redirect("pay:step_2")

    return render(request, "pay/order_step_1.html", context=context)

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
