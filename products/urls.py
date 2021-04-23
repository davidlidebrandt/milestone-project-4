from django.urls import path
from . import views

urlpatterns = [
    path('', views.products, name="products"),
    path('<int:id>', views.product_page, name="product_page"),
    path('post_review/<int:id>', views.post_review, name="post_review"),
    path('delete_review/<int:review_id>/<int:product_id>/',
         views.delete_review, name="delete_review"),
]
