from django.contrib import admin

from .models import Review, Seller, Profile

admin.site.register(Seller)
admin.site.register(Review)
admin.site.register(Profile)
