from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.views.decorators.http import require_http_methods
from products.models import Product


def view_bag(request):
    return render(request, "shopping_bag/bag.html")


@require_http_methods(["POST"])
def add_to_bag(request, id):
    product = get_object_or_404(Product, id=id)
    bag = request.session.get("shopping_bag", {})
    quantity_request = 0
    if int(request.POST.get("quantity-input")) <= 10:
        quantity_request = int(request.POST.get("quantity-input"))
    else:
        quantity_request = 10

    try:
        if str(id) in bag.keys():
            if bag[str(id)]["quantity"] + quantity_request <= 10:
                bag[str(id)]["quantity"] += quantity_request
            else:
                bag[str(id)]["quantity"] = 10
        else:
            bag.update({id: {"quantity": quantity_request}})
        if "total_cost" in bag.keys():
            bag["total_cost"] += product.prize * quantity_request
        else:
            bag["total_cost"] = product.prize * quantity_request
        request.session["shopping_bag"] = bag
        messages.success(request, "Item was added")
    except Exception as e:
        messages.error(request, f"Error {e} when adding item")
    return redirect("view_bag")


@require_http_methods(["POST"])
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


@require_http_methods(["POST"])
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
