from products.models import Product


def bag(request):
    id = 1
    quantity = 1
    return {
        "product": Product.objects.get(id=id),
        "quantity": quantity,
    }
