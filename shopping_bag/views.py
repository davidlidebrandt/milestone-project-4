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
        bag["total_cost"] += product.prize * int(
            request.POST.get("quantity-input"))
    else:
        bag["total_cost"] = product.prize * int(
            request.POST.get("quantity-input"))
    request.session["shopping_bag"] = bag
    return redirect("view_bag")


def add_to_quantity(request, id):
    product = get_object_or_404(Product, id=id)
    bag = request.session.get("shopping_bag", {})
    old_quantity = bag[str(id)]["quantity"]
    if old_quantity < 10:
        bag[str(id)]["quantity"] = old_quantity + 1
        bag["total_cost"] += product.prize
    request.session["shopping_bag"] = bag
    return redirect("view_bag")


def delete_from_quantity(request, id):
    product = get_object_or_404(Product, id=id)
    bag = request.session.get("shopping_bag", {})
    try:
        old_quantity = bag[str(id)]["quantity"]
    except KeyError:
        old_quantity = 1
    if old_quantity > 0:
        bag[str(id)]["quantity"] = old_quantity - 1
        bag["total_cost"] -= product.prize
    request.session["shopping_bag"] = bag
    if bag[str(id)]["quantity"] <= 0:
        request.session.pop("shopping_bag", str(id))
    return render(request, "shopping_bag/bag.html")
