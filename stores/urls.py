from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_stores, name="view_stores"),
]
