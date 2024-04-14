from django.contrib import admin

from pay.models import Order, OrderItem

admin.site.register(Order)
admin.site.register(OrderItem)
