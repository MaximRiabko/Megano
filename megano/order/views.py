from django.shortcuts import render, redirect
from .models import Order





def order_view(request):
    if request.method == 'GET':



        return render(request, "order/order.html")

    if request.method == 'POST':
        data = request.POST

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
            return redirect("pay:payment")
        else:
            return redirect("pay:paymentsomeone")
