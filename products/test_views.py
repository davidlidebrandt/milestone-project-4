from django.test import TestCase
from django.urls import reverse
from django.shortcuts import redirect, get_object_or_404
from . models import Product, Discount, Category, Manufacturer


class TestViews(TestCase):
    def test_get_all_products_page(self):
        self.assertEquals(self.client.get("/products/").status_code, 200)
        self.assertTemplateUsed(
            self.client.get("/products/"), "products/products.html")

    def test_get_single_product_page(self):
        test_category = Category(name="Kettlebells")
        test_discount = Discount(name="30%", rate=0.7)
        test_manufacurer = Manufacturer(name="Great Sports")
        test_product = Product(name="Test", description="A description",
                               image_url="", category=test_category,
                               manufacturer=test_manufacurer,
                               quantity=10, prize=100,
                               discount_rate=test_discount,
                               units_sold=1,
                               id=1)
        print(f"/products/{test_product.id}")
        """self.assertEquals(self.client.get(f"/products/{test_product.id}")
                          .status_code, 200)"""
        print(test_product.id)
        print("here")
        """self.assertTemplateUsed(
            self.client.get(reverse("product_page", args=[1])),
            "products/product_page.html")"""
