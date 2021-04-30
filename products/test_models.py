from django.test import TestCase
from .models import Product, Category, Manufacturer, Discount, Review
from django.contrib.auth.models import User


class TestCategory(TestCase):

    def test_create_category(self):
        test_category = Category(name="Barbells", image_url="/url")
        test_category.save()
        self.assertEquals(test_category.name, "Barbells")
        self.assertEquals(test_category.image_url, "/url")

    def test_category_to_string_method(self):
        test_category = Category(name="Barbells", image_url="/url")
        test_category.save()
        self.assertEquals(test_category.__str__(), "Barbells")


class TestManufacturer(TestCase):

    def test_create_manufacturer(self):
        test_manufacturer = Manufacturer(name="Star Sports")
        test_manufacturer.save()
        self.assertEquals(test_manufacturer.name, "Star Sports")

    def test_manufacturer_to_string_method(self):
        test_manufacturer = Manufacturer(name="Star Sports")
        test_manufacturer.save()
        self.assertEquals(test_manufacturer.__str__(), "Star Sports")


class TestDiscount(TestCase):

    def test_create_discount(self):
        test_discount = Discount(name="20%", rate=0.8)
        test_discount.save()
        self.assertEquals(test_discount.name, "20%")
        self.assertEquals(test_discount.rate, 0.8)

    def test_discount_to_string_method(self):
        test_discount = Discount(name="20%", rate=0.8)
        test_discount.save()
        self.assertEquals(test_discount.__str__(), "20%")


class TestProduct(TestCase):

    @classmethod
    def initialize_creating_product(self):

        test_category = Category(name="Kettlebells")
        test_category.save()
        test_discount = Discount(name="30%", rate=0.7)
        test_discount.save()
        test_manufacurer = Manufacturer(name="Great Sports")
        test_manufacurer.save()
        test_product = Product(name="Test", description="A description",
                               image_url="", category=test_category,
                               manufacturer=test_manufacurer,
                               prize=100,
                               discount_rate=test_discount,
                               units_sold=1)
        return test_product

    def test_create_product(self):
 
        test_product = TestProduct.initialize_creating_product()
        test_product.save()

        self.initialize_creating_product()
        self.assertEquals(test_product.name, "Test")
        self.assertEquals(test_product.description, "A description")
        self.assertEquals(test_product.image_url, "")
        self.assertEquals(test_product.category.name, "Kettlebells")
        self.assertEquals(test_product.manufacturer.name, "Great Sports")
        self.assertEquals(test_product.prize, 100)
        self.assertEquals(test_product.discount_rate.name, "30%")
        self.assertEquals(test_product.units_sold, 1)

    def test_product_to_string_method(self):

        test_product = TestProduct.initialize_creating_product()
        self.assertEquals(test_product.__str__(), "Test")


class TestReview(TestCase):

    def test_create_review(self):

        test_product = TestProduct.initialize_creating_product()
        test_product.save()

        test_user = User(username="Joe")
        test_user.save()
        test_review = Review(by_user=test_user,
                             product=test_product,
                             description="Great",
                             rating=5)
        test_review.save()

        self.assertEquals(test_review.by_user, test_user)
        self.assertEquals(test_review.product, test_product)
        self.assertEquals(test_review.description, "Great")
        self.assertEquals(test_review.rating, 5)

    def test_review_to_string_method(self):

        test_product = TestProduct.initialize_creating_product()
        test_product.save()
        test_user = User(username="Joe")
        test_user.save()
        test_review = Review(by_user=test_user,
                             product=test_product,
                             description="Great",
                             rating=5)
        test_review.save()

        self.assertEquals(test_review.__str__(), "Great")
