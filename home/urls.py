from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('404/', views.custom_404_handler, name="custom_404_handler"),
]
