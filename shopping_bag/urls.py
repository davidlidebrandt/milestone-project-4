from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_bag, name="view_bag"),
    path('add_to_bag/<int:id>/', views.add_to_bag, name="add_to_bag"),
    path('add_to_quantity/<int:id>/',
         views.add_to_quantity, name="add_to_quantity"),
    path('delete_from_quantity/<int:id>/',
         views.delete_from_quantity, name="delete_from_quantity"),
]
