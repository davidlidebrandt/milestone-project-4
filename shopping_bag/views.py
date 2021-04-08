from django.shortcuts import render


def checkout(request):
    return render(request, "shopping_bag/checkout.html")


def add_to_bag(request, id):
    request.session["shopping_bag"] = id
    return render(request, "shopping_bag/checkout.html")
