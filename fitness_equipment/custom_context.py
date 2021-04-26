from products.models import Category, Product, Manufacturer


def show_categories(request):

    """
    Retrives categories, products, manufacturers
    and discount objects from the database.
    Limits each query to 6 objects and retrives
    random objects in each model.
    """
    return {
        "categories": Category.objects.all().order_by("?")[:6],
        "products": Product.objects.all().order_by("?")[:6],
        "manufacturers": Manufacturer.objects.all().order_by("?")[:6],
        "fifty_percent_discount": Product.objects.all().filter(
            discount_rate__rate=0.5).order_by("?")[:6]
    }
