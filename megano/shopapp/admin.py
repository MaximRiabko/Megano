from django.contrib import admin

from .models import Review, Seller, Product, ProductSeller

class SellerAdmin(admin.ModelAdmin):
    list_display = "pk", "name", "description", "image", "phone", "address", "email"

class ReviewAdmin(admin.ModelAdmin):
    list_display = "pk", "author", "product", "content", "created_reviews"



admin.site.register(Seller, SellerAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Product)
admin.site.register(ProductSeller)