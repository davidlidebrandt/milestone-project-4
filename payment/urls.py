from django.urls import path
from . import views

urlpatterns = [
    path('create_checkout/', views.create_checkout, name="create_checkout"),
]
