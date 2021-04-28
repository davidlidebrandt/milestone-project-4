from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.views.decorators.http import require_http_methods
from django.contrib import messages
from . forms import UserProfileForm
from payment.models import Order, OrderItem


def show_profile(request):
    user = get_object_or_404(User, id=request.user.id)
    user_profile_form = UserProfileForm()
    orders = Order.objects.filter(user=user)
    order_items = []
    for order in orders:
        print(order.id)
        item = OrderItem.objects.filter(order__id=order.id)
        order_items.append({str(order.id): item})
    try:
        user_profile_form = UserProfileForm(instance=user.userprofile)
    except Exception as e:
        user_profile_form = UserProfileForm()
        print(f"{e}")

    context = {
        "user": user,
        "user_profile_form": user_profile_form,
        "orders": orders,
        "order_items": order_items,
    }

    return render(request, "profile/profile.html", context)


@require_http_methods(["POST"])
def update_profile(request):
    user = get_object_or_404(User, id=request.user.id)
    user_profile = UserProfileForm(request.POST, instance=user.userprofile)
    if user_profile.is_valid():
        user_profile.save()
        messages.success(request, "Profile was updated")
    else:
        messages.error(request, "Error when updating profile")
    return redirect("show_profile")

