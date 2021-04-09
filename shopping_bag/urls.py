from django.urls import path
from . import views

urlpatterns = [
    path('', views.checkout, name="checkout"),
    path('add_to_bag/<int:id>/', views.add_to_bag, name="add_to_bag"),
]