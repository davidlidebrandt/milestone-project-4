from django.shortcuts import render, get_object_or_404
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


def product_page(request, id):
    product = get_object_or_404(Product, id=id)
    context = {
        "product": product,
    }
    return render(request, "products/product_page.html", context)
