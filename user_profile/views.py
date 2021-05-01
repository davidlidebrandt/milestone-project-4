from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.views.decorators.http import require_http_methods
from django.contrib import messages
from django.core.paginator import Paginator
from . forms import UserProfileForm
from . models import UserProfile
from payment.models import Order, OrderItem


def show_profile(request):

    """
    Tries to get the current user by the current session user id.
    Retrives all orders from the user and all order items in the
    database.
    Paginates the orders via the Django Paginator class.
    Tries to retrive the user profile and renders a profile form
    for updating details with the previous details.
    Otherwise creates a new profile for the user and renders an
    empty form.
    Renders the profile template.
    """
    user = get_object_or_404(User, id=request.user.id)
    user_profile_form = UserProfileForm()
    order_list = Order.objects.filter(user=user).order_by("-date")
    order_items = OrderItem.objects.all()
    paginator = Paginator(order_list, 5)
    current_page = request.GET.get("page", 1)
    orders = paginator.get_page(current_page)

    try:
        user_profile = UserProfile.objects.get(user=user)
        user_profile_form = UserProfileForm(instance=user_profile)
    except Exception as e:
        profile = UserProfile(user=request.user, name="", address="")
        profile.save()
        user_profile_form = UserProfileForm()
        messages.success(request, f"{e}, profile was created")

    context = {
        "user": user,
        "user_profile_form": user_profile_form,
        "orders": orders,
        "order_items": order_items,
    }

    return render(request, "profile/profile.html", context)


@require_http_methods(["POST"])
def update_profile(request):
    """
    Tries to get the user based on the current sessions user id.
    Tries to get the users profile.
    Tries to update the users profile with post data sent via the
    form.
    Sends any success/error messages and redirects to view the profile.
    """
    user = get_object_or_404(User, id=request.user.id)
    user_profile = get_object_or_404(UserProfile, user=user)
    try:
        user_profile = UserProfileForm(request.POST, instance=user_profile)
    except AttributeError:
        messages.error(request, "Error when updating profile")
    if user_profile.is_valid():
        user_profile.save()
        messages.success(request, "Profile was updated")
    else:
        messages.error(request, "Error when updating profile")
    return redirect("show_profile")
