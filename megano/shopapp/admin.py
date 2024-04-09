from django.contrib import admin

from .models import Profile, Review, Seller, Product, ProductSeller, Discount, ProductImage

admin.site.register(Seller)
admin.site.register(Review)
admin.site.register(Profile)
admin.site.register(Product)
admin.site.register(ProductSeller)
admin.site.register(Discount)
admin.site.register(ProductImage)
