from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User


def show_profile(request):
    current_user = get_object_or_404(User, id=request.user.id)
    