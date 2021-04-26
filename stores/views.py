from django.shortcuts import render
from . models import Store


def view_stores(request):

    """
    Retrives all Store objects from the database.
    Sends the objects via the context and
    renders a template.
    """

    stores = Store.objects.all()
    context = {
        "stores": stores,
    }
    return render(request, "stores/view_stores.html", context)
