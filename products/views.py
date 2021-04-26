from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_http_methods
from django.db.models import Q
from django.core.paginator import Paginator
from django.contrib import messages
from django.contrib.auth.models import User
from . models import Product, Review
from . forms import PartialReviewForm


def products(request):

    """
    Retrives products from the database.
    Sorts and orders the products based on
    query parameters if present.
    Sends the products via the context and
    renders a template.
    """
    if request.GET.get("category"):
        if request.GET.get("sort"):
            if request.GET.get("sort") == "units_sold":
                all_products = Product.objects.filter(
                    category__name=request.GET.get(
                        "category")).order_by("-units_sold")
            else:
                all_products = Product.objects.filter(
                    category__name=request.GET.get(
                        "category")).order_by(request.GET.get("sort"))
        else:
            all_products = Product.objects.filter(
                category__name=request.GET.get("category"))

    elif request.GET.get("manufacturer"):
        if request.GET.get("sort"):
            print("here")
            if request.GET.get("sort") == "units_sold":
                all_products = Product.objects.filter(
                    manufacturer__name=request.GET.get("manufacturer")
                    ).order_by("-units_sold")
            else:
                all_products = Product.objects.filter(
                    manufacturer__name=request.GET.get(
                        "manufacturer")).order_by(request.GET.get("sort"))
        else:
            all_products = Product.objects.filter(
                manufacturer__name=request.GET.get("manufacturer"))

    elif request.GET.get("sort"):
        if request.GET.get("sort") == "units_sold":
            all_products = Product.objects.all().order_by(
                "-units_sold")
        else:
            all_products = Product.objects.all().order_by(
                request.GET.get("sort"))

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

    """
    Retrives a single product by the id sent via
    the request.
    Retrives all reviews present for the product
    and calculates an average rating for the product.
    Uses Djangos paginator class to paginate the
    list of reviews.
    Creates a form for adding new reviews.
    Sends the product, review list, rating and
    form via the context and renders a template.
    """
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
        messages.error(request, ("Error when saving your review," +
                       "please try again or contact us"))
    return redirect("product_page", id=id)


@require_http_methods(["POST"])
def delete_review(request, review_id, product_id):
    review = get_object_or_404(Review, id=review_id)
    author = get_object_or_404(User, id=review.by_user.id)
    current_user = request.user

    if author == current_user:
        review.delete()
        messages.success(request, "Review was deleted")
    else:
        messages.error(request, "Error when trying to delete review")
    return redirect("product_page", id=product_id)


@require_http_methods(["POST"])
def update_review(request, review_id, product_id):
    review = get_object_or_404(Review, id=review_id)
    author = get_object_or_404(User, id=review.by_user.id)
    if request.user == author:
        if request.method == "GET":
            form = PartialReviewForm(instance=review)
            context = {
                "form": form
            }
            return render(request, "products/update_review.html", context)
        elif request.method == "POST":
            updated_form = PartialReviewForm(request.POST, instance=review)
            if updated_form.is_valid():
                updated_form.save()
                messages.success(request, "Review was updated")
            else:
                messages.error(request, "Error when updating your review")
            return redirect("product_page", id=product_id)
    else:
        messages.error(request, "Action not allowed")
        return redirect("home")
