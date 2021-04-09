from products.models import Product
from django.shortcuts import get_object_or_404


def bag(request):
    bag = request.session.get("shopping_bag", {})
    context = {}
    for product in bag:
        if not product == "total_cost":
            context[product] = {"product": get_object_or_404(
                Product, id=product), "quantity": bag[product]["quantity"]}
    print(context)
    return {"context": context}
