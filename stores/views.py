from django.shortcuts import render
from . models import Store


def view_stores(request):
    stores = Store.objects.all()
    context = {
        "stores": stores,
    }
    return render(request, "stores/view_stores.html", context)
