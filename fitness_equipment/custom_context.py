from products.models import Category, Product, Manufacturer


def show_categories(request):
    return {
        "categories": Category.objects.all()[:6],
        "products": Product.objects.all()[:6],
        "manufacturers": Manufacturer.objects.all()[:6],
    }
