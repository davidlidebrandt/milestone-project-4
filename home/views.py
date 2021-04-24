from django.shortcuts import render


def index(request):
    return render(request, "home/index.html")


def custom_404_handler(request):
    return render(request, "404.html")
