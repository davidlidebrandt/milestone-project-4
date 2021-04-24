from django.shortcuts import render
from django.http import HttpResponseNotFound
from django.template import loader


def index(request):
    return render(request, "home/index.html")


def custom_404_handler(request, exception):
    template = loader.get_template("home/404.html")
    context = {}
    response_html = template.render(context, request)
    return HttpResponseNotFound(response_html)
