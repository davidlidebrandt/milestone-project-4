from products.models import Product
from django.shortcuts import get_object_or_404


def bag(request):
    bag = request.session.get("shopping_bag", {})
    print(bag)
    context = {}
    try:
        total_cost = request.session["shopping_bag"]["total_cost"]
    except KeyError:
        total_cost = {}
    for product in bag:
        if not product == "total_cost":
            context[product] = {"product": get_object_or_404(
                Product, id=product), "quantity": bag[product]["quantity"]}
    return {"context": context,
            "total_cost": total_cost
    }
