from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_profile, name="show_profile"),
    path('change_password/', views.change_password, name="change_password"),
    path('update_profile/', views.update_profile, name="update_profile"),
]
