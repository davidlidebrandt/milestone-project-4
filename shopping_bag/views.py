from django.shortcuts import render, redirect, get_object_or_404
from products.models import Product


def checkout(request):
    return render(request, "shopping_bag/checkout.html")


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
    return redirect("checkout")
