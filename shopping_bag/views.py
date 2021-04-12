from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.views.decorators.http import require_http_methods
from products.models import Product


def view_bag(request):
    print(request.session.get("shopping_bag", {}))
    return render(request, "shopping_bag/bag.html")


def add_to_bag(request, id):
    product = get_object_or_404(Product, id=id)
    bag = request.session.get("shopping_bag", {})
    try:
        if str(id) in bag.keys():
            bag[str(id)]["quantity"] += int(request.POST.get("quantity-input"))
        else:
            bag.update({id: {"quantity": int(
                request.POST.get("quantity-input"))}})
        if "total_cost" in bag.keys():
            bag["total_cost"] += product.prize * int(
                request.POST.get("quantity-input"))
        else:
            bag["total_cost"] = product.prize * int(
                request.POST.get("quantity-input"))
        request.session["shopping_bag"] = bag
        messages.success(request, "Item was added")
    except Exception as e:
        messages.error(request, f"Error {e} when adding item")
    return redirect("view_bag")


def add_to_quantity(request, id):
    product = get_object_or_404(Product, id=id)
    bag = request.session.get("shopping_bag", {})
    try:
        old_quantity = bag[str(id)]["quantity"]
        if old_quantity < 10:
            bag[str(id)]["quantity"] = old_quantity + 1
            bag["total_cost"] += product.prize
            request.session["shopping_bag"] = bag
            messages.success(request, "Item was added")
    except KeyError:
        messages.error(request, "Item could not be added, try again")
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
        messages.success(request, "Item was deleted")
    except KeyError:
        messages.error(request, "Error when trying to delete the item")
    return redirect("view_bag")
