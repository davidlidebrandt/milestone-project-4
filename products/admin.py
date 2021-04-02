from django.contrib import admin
from .models import Product, Review, Category, Manufacturer


class ReviewInline(admin.StackedInline):
    model = Review


class ProductAdmin(admin.ModelAdmin):
    inlines = [ReviewInline]


admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
admin.site.register(Manufacturer)
