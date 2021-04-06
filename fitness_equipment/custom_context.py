from products.models import Category, Product


def show_categories(request):
    return {
        "categories": Category.objects.all(),
        "products": Product.objects.all()[:5],
    }
