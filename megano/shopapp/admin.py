from django.contrib import admin

from .models import Review, Seller, Product, ProductSeller, ProductImage, Categories

class SellerAdmin(admin.ModelAdmin):
    list_display = "pk", "name", "description", "image", "phone", "address", "email"

class ReviewAdmin(admin.ModelAdmin):
    list_display = "pk", "author", "product", "content", "created_reviews"

class ProductAdmin(admin.ModelAdmin):
    list_display = "pk", "category"

class CategoryAdmin(admin.ModelAdmin):
    list_display = "pk", "name"

admin.site.register(Seller, SellerAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Product)
admin.site.register(ProductSeller)
admin.site.register(ProductImage)
admin.site.register(Categories, CategoryAdmin)