from django.test import TestCase
from .models import Product, Category, Manufacturer


class TestCategory(TestCase):

    def test_create_category(self):
        test_category = Category(name="Barbells")
        test_empty_category_name = Category(name="")
        self.assertEquals(test_category.name, "Barbells")
        self.assertEquals(test_empty_category_name.name, "")


class TestManufacturer(TestCase):

    def test_create_manufacturer(self):
        test_manufacturer = Manufacturer(name="Star Sports")
        self.assertEquals(test_manufacturer.name, "Star Sports")


class TestProduct(TestCase):

    def test_create_product(self):
        test_category = Category(name="Kettlebells")
        test_manufacurer = Manufacturer(name="Great Sports")
        test_product = Product(name="Test", description="A description",
                               image_url="", category=test_category,
                               manufacturer=test_manufacurer,
                               has_size=False, quantity=10, prize=100)

        self.assertEquals(test_product.name, "Test")
        self.assertEquals(test_product.description, "A description")
        self.assertEquals(test_product.image_url, "")
        self.assertEquals(test_product.category.name, "Kettlebells")
        self.assertEquals(test_product.manufacturer.name, "Great Sports")
        self.assertEquals(test_product.has_size, False)
        self.assertEquals(test_product.quantity, 10)
        self.assertEquals(test_product.prize, 100)
