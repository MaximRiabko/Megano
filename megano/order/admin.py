from django.contrib import admin

from .models import Order, OrderItem

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ["product",]

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'city',
                    'address', 'payment', 'payment_status',
                    'delivery', 'created_at', 'comment', 'reference_num']
    list_filter = ['payment_status', 'created_at']
    inlines = [OrderItemInline,]

