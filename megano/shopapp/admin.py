from django.contrib import admin

from .models import Review, Seller, Product

admin.site.register(Seller)
admin.site.register(Review)
admin.site.register(Product)