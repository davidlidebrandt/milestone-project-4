from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods
from products.models import Product


def view_bag(request):
    print(request.session.get("shopping_bag", {}))
    return render(request, "shopping_bag/bag.html")


def add_to_bag(request, id):
    product = get_object_or_404(Product, id=id)
    bag = request.session.get("shopping_bag", {})
    print(bag)
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
    print(bag)
    return redirect("view_bag")


def add_to_quantity(request, id):
    product = get_object_or_404(Product, id=id)
    bag = request.session.get("shopping_bag", {})
    print(bag)
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
        if bag[str(id)]["quantity"] <= 1:
            bag["total_cost"] -= product.prize
            if bag["total_cost"] <= 0:
                del bag["total_cost"]
            del bag[str(id)]
        else:
            old_quantity = bag[str(id)]["quantity"]
            bag[str(id)]["quantity"] = old_quantity - 1
            bag["total_cost"] -= product.prize
        request.session["shopping_bag"] = bag
        return redirect("view_bag")
    except KeyError:
        return "Error"
