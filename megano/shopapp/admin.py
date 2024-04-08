from django.contrib import admin

from .models import Profile, Review, Seller

admin.site.register(Seller)
admin.site.register(Review)
admin.site.register(Profile)
