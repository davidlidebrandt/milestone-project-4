from django.test import TestCase
from . models import Order, OrderItem
from products.models import Product, Discount, Category, Manufacturer
import datetime
from django.contrib.auth.models import User


class TestModels(TestCase):

    def test_order_to_string_method(self):

        test_user = User(username="Test")
        test_user.save()
        date = datetime.datetime.now()

        test_order = Order(date=date,
                           user=test_user,
                           amount_paid=100,
                           shipping_address="Street",
                           customer_name="Name",
                           customer_email="anemail@email.com")
        test_order.save()

        self.assertEquals(test_order.__str__(), "Name")

    def test_order_item_to_string_method(self):
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

        test_user = User(username="Test")
        test_user.save()
        date = datetime.datetime.now()

        test_order = Order(date=date,
                           user=test_user,
                           amount_paid=100,
                           shipping_address="Street",
                           customer_name="Name",
                           customer_email="anemail@email.com")
        test_order.save()

        test_order_item = OrderItem(product=test_product,
                                    order=test_order,
                                    quantity=1)

        self.assertEquals(test_order_item.__str__(), "Test")


class TestViews(TestCase):

    def test_get_payment_success_page(self):

        self.assertEquals(self.client.get(
            "/payment/success/").status_code, 200)
        self.assertTemplateUsed(
            self.client.get("/payment/success/"), "payment/success.html")

    def test_get_payment_error_page(self):

        self.assertEquals(self.client.get(
            "/payment/error/").status_code, 200)
        self.assertTemplateUsed(
            self.client.get("/payment/error/"), "payment/error.html")
