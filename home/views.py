from django.shortcuts import render
from django.http import HttpResponseNotFound
from django.template import loader


def index(request):

    """
    Renders template when URL is
    requested.
    """

    return render(request, "home/index.html")


def custom_404_handler(request, exception):

    """
    Overrides the default Django 404 handler.
    Loads and renders template and sends back
    the template in the http response.
    Triggers whenever a page is not found on the site.
    """

    template = loader.get_template("home/404.html")
    context = {}
    response_html = template.render(context, request)
    return HttpResponseNotFound(response_html)
