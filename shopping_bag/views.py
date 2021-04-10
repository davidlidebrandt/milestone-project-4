from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods
from products.models import Product


def view_bag(request):
    return render(request, "shopping_bag/bag.html")


def add_to_bag(request, id):
    product = get_object_or_404(Product, id=id)
    bag = request.session.get("shopping_bag", {})
    if str(id) in bag.keys():
        bag[str(id)]["quantity"] += int(request.POST.get("quantity-input"))
    else:
        bag.update({id: {"quantity": int(request.POST.get("quantity-input"))}})
    if "total_cost" in bag.keys():
        bag["total_cost"] += product.prize
    else:
        bag["total_cost"] = product.prize
    request.session["shopping_bag"] = bag
    return redirect("view_bag")


@require_http_methods(["POST"])
def update_bag(request, id, quantity):
    product = get_object_or_404(Product, id=id)
    if quantity == 0:
        request.session.pop(str(id))
    else:
        bag = request.session.get("shopping_bag", {})
        bag[str(id)]["quantity"] = quantity
        request.session["shopping_bag"] = bag
    return "Bag Updated"

