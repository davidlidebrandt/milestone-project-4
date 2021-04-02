from django.test import TestCase
from . models import Product, Category, Manufacturer


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


"""class TestProduct(TestCase):

    def test_create_product(self):
        test_product = Product(name="Test", description="A description")"""
