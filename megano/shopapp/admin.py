from django.contrib import admin

from .models import (
    Categories,
    Discount,
    Product,
    ProductImage,
    ProductSeller,
    Profile,
    Review,
    Seller,
)

admin.site.register(Seller)
admin.site.register(Review)
admin.site.register(Profile)
admin.site.register(Product)
admin.site.register(ProductSeller)
admin.site.register(Discount)
admin.site.register(ProductImage)
admin.site.register(Categories)
