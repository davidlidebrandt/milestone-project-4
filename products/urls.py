from django.urls import path
from . import views

urlpatterns = [
    path('', views.products, name="products"),
    path('<int:id>', views.product_page, name="product_page"),
]
