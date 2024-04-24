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
    ViewHistory,
)


class DiscountInline(admin.TabularInline):
    model = Discount.products.through


@admin.register(Discount)
class DiscountAdmin(admin.ModelAdmin):
    inlines = [
        DiscountInline,
    ]
    list_display = (
        "pk",
        "name",
        "description_short",
        "date_start",
        "date_end",
        "promocode",
        "value",
        "type",
    )
    list_display_links = "pk", "name"
    ordering = ["pk"]
    search_fields = "name", "description"

    def description_short(self, obj: Discount) -> str:
        if len(obj.description) < 48:
            return obj.description
        return obj.description[:48] + "..."

    def get_queryset(self, request):
        return Discount.objects.prefetch_related("products")


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
admin.site.register(Profile)
admin.site.register(ViewHistory)
