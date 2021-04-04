from django.shortcuts import render
from . models import Product


def products(request):
    if request.GET.get("category"):
        all_products = Product.objects.filter(
            category__name=request.GET.get("category"))
    else:
        all_products = Product.objects.all()
    context = {
        "all_products": all_products,
    }
    return render(request, "products/products.html", context)
