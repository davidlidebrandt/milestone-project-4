from django.contrib import admin
from .models import Product, Review


class ReviewInline(admin.StackedInline):
    model = Review


class ProductAdmin(admin.ModelAdmin):
    inlines = [ReviewInline]


admin.site.register(Product, ProductAdmin)
