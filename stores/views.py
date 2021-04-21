from django.shortcuts import render


def view_stores(request):
    render(request, "stores/view_stores.html")
