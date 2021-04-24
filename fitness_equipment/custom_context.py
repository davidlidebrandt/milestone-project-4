from products.models import Category, Product, Manufacturer, Discount


def show_categories(request):
    return {
        "categories": Category.objects.all()[:6],
        "products": Product.objects.all()[:6],
        "manufacturers": Manufacturer.objects.all()[:6],
        "fifty_percent_discount": Product.objects.all().filter(
            discount_rate__rate=0.5)
    }
