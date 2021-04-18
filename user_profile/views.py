from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from allauth.account.forms import ChangePasswordForm


def show_profile(request):
    user = get_object_or_404(User, id=request.user.id)
    password_form = ChangePasswordForm
    context = {
        "user": user,
        "password_form": password_form
    }

    return render(request, "profile/profile.html", context)
