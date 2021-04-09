from django.shortcuts import render, redirect, get_object_or_404
from products.models import Product


def checkout(request):
    return render(request, "shopping_bag/checkout.html")


def add_to_bag(request, id):
    get_object_or_404(Product, id=id)
    bag = request.session.get("shopping_bag", {})
    if str(id) in bag.keys():
        bag[str(id)]["quantity"] += int(request.POST.get("quantity-input"))
    else:
        bag.update({id: {"quantity": int(request.POST.get("quantity-input"))}})
    request.session["shopping_bag"] = bag
    print(request.session["shopping_bag"])
    return redirect("checkout")
