from django.urls import path
from . import views

urlpatterns = [
    path('create_checkout/', views.create_checkout, name="create_checkout"),
    path('confirmation/', views.confirmation_of_payment,
         name="confirmation_of_payment"),
    path('success/', views.payment_success, name="payment_success"),
    path('error/', views.payment_error, name="payment_error"),
]
