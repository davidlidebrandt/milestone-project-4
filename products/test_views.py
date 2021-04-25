from django.test import TestCase
from django.urls import reverse
from . models import Product, Discount, Category, Manufacturer


class TestViews(TestCase):
    def test_get_all_products_page(self):
        self.assertEquals(self.client.get("/products/").status_code, 200)
        self.assertTemplateUsed(
            self.client.get("/products/"), "products/products.html")

    def test_get_single_product_page(self):
        test_category = Category(name="Kettlebells")
        test_category.save()
        test_discount = Discount(name="30%", rate=0.7)
        test_discount.save()
        test_manufacurer = Manufacturer(name="Great Sports")
        test_manufacurer.save()
        test_product = Product(name="Test", description="A description",
                               image_url="", category=test_category,
                               manufacturer=test_manufacurer,
                               quantity=10, prize=100,
                               discount_rate=test_discount,
                               units_sold=1,)
        test_product.save()
        self.assertEquals(self.client.get(reverse(
            "product_page", kwargs={"id": test_product.id})).status_code, 200)
        self.assertEquals(self.client.get("/products/1").status_code, 200)

        self.assertTemplateUsed(
            self.client.get(reverse(
                "product_page", kwargs={"id": test_product.id})),
            "products/product_page.html")
