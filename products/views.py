from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_http_methods
from django.db.models import Q
from django.core.paginator import Paginator
from django.contrib import messages
from . models import Product, Review
from . forms import PartialReviewForm


def products(request):
    if request.GET.get("category"):
        if request.GET.get("sort"):
            all_products = Product.objects.filter(
                category__name=request.GET.get(
                    "category")).order_by(request.GET.get("sort"))
        else:
            all_products = Product.objects.filter(
                category__name=request.GET.get("category"))

    elif request.GET.get("manufacturer"):
        if request.GET.get("sort"):
            all_products = Product.objects.filter(
                manufacturer__name=request.GET.get(
                    "manufacturer")).order_by(request.GET.get("sort"))
        else:
            all_products = Product.objects.filter(
                manufacturer__name=request.GET.get("manufacturer"))

    elif request.GET.get("sort"):
        all_products = Product.objects.all().order_by(request.GET.get("sort"))

    elif request.GET.get("search"):
        all_products = Product.objects.filter(
            Q(name__contains=request.GET.get("search")) | Q(
                description__contains=request.GET.get("search")) | Q(
                    manufacturer__name__contains=request.GET.get("search")))

    else:
        all_products = Product.objects.all()
    context = {
        "all_products": all_products,
    }
    return render(request, "products/products.html", context)


def product_page(request, id):
    product = get_object_or_404(Product, id=id)
    reviews_list = Review.objects.filter(product=product)
    count = 0
    rating = None
    if reviews_list:
        for review in reviews_list:
            count += review.rating
        rating = int(count/len(reviews_list))
    paginator = Paginator(reviews_list, 5)
    current_page = request.GET.get("page", 1)
    reviews = paginator.get_page(current_page)

    form = PartialReviewForm()
    context = {
        "product": product,
        "form": form,
        "reviews": reviews,
        "rating": rating,
    }
    return render(request, "products/product_page.html", context)


@require_http_methods(["POST"])
def post_review(request, id):
    product = get_object_or_404(Product, id=id)
    user_and_product = Review(by_user=request.user, product=product)
    form = PartialReviewForm(request.POST, instance=user_and_product)
    if form.is_valid():
        form.save()
        messages.success(request, "Your review was saved")
    else:
        messages.error(request, "Error when saving your review, please try again or contact us")
    return redirect("product_page", id=id)
