from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_profile, name="show_profile"),
    path('update_profile/', views.update_profile, name="update_profile"),
]
