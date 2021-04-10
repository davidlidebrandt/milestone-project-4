from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_bag, name="view_bag"),
    path('add_to_bag/<int:id>/', views.add_to_bag, name="add_to_bag"),
    path('update_bag/<int:id>/<int:quantity>/',
         views.update_bag, name="update_bag"),
]
