from django.test import TestCase
from products.models import Product, Discount, Category, Manufacturer


class TestViews(TestCase):

    def test_get_bag(self):

        """
        Makes a request to the given URL.
        Ensures correct status code is returned.
        Ensures correct template is used.
        """
        self.assertEquals(self.client.get("/bag/").status_code, 200)
        self.assertTemplateUsed(
            self.client.get("/bag/"), "shopping_bag/bag.html")

    def test_add_to_bag(self):

        """
        Creates a test Product.
        Sends a post request with the id of the Product.
        Ensures that the Product is saved in the bag by
        displaying the correct message returned by the
        request.
        Ensure correct redirect status code is returned.
        """

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
        test_product.save()
        test_response = self.client.post("/bag/add_to_bag/1/",
                                         {"quantity-input": 1})

        test_response_message = self.client.post("/bag/add_to_bag/1/",
                                                 {"quantity-input": 1},
                                                 follow=True)

        intended_message = "Item was added"
        message = ""

        get_stored_messages = test_response_message.context["messages"]
        for message in get_stored_messages:
            message = message

        self.assertEquals(test_response.status_code, 302)
        self.assertEquals(intended_message, message.__str__())

    def test_add_to_quantity(self):

        """
        Creates a test Product.
        First sends a post request with the id of the product
        to add the product to the bag to add_to_bag view.
        Then sends another post request to add_to quantity.
        Ensures that the Product quantity is increased in the bag by
        displaying the correct message returned by the request.
        Ensures correct redirect status code is returned.
        """

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
        test_product.save()

        self.client.post("/bag/add_to_bag/1/", {"quantity-input": 1})
        test_response = self.client.post("/bag/add_to_quantity/1/")
        test_response_message = self.client.post("/bag/add_to_quantity/1/",
                                                 follow=True)

        intended_message = "Item was added"
        message = ""

        get_stored_messages = test_response_message.context["messages"]
        for message in get_stored_messages:
            message = message

        self.assertEquals(test_response.status_code, 302)
        self.assertEquals(intended_message, message.__str__())

    def test_delete_from_quantity(self):

        """
        Creates a test Product.
        First sends a post request with the id of the product
        to add the product to the bag to add_to_bag view.
        Then sends another post request to delete_from_quantity to
        remove one item of that product from the bag.
        Ensures that the Product quantity is decreased in the bag by
        displaying the correct message returned by the request.
        Ensures correct redirect status code is returned.
        """

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
        test_product.save()

        self.client.post("/bag/add_to_bag/1/", {"quantity-input": 1})
        test_response = self.client.post("/bag/delete_from_quantity/1/")

        self.client.post("/bag/add_to_bag/1/", {"quantity-input": 1})
        test_response_message = self.client.post(
            "/bag/delete_from_quantity/1/", follow=True)

        intended_message = "Item was deleted"
        message = ""

        get_stored_messages = test_response_message.context["messages"]
        for message in get_stored_messages:
            message = message

        self.assertEquals(test_response.status_code, 302)
        self.assertEquals(intended_message, message.__str__())

        # Add a quantity of two
        # Ensure the bag content contains one item after deleting one

        self.client.post("/bag/add_to_bag/1/", {"quantity-input": 2})
        test_response_message = self.client.post(
            "/bag/delete_from_quantity/1/", follow=True)

        intended_bag_content = {'1': {'quantity': 1}, 'total_cost': 70}
        shopping_bag = self.client.session["shopping_bag"]

        self.assertEquals(test_response.status_code, 302)
        self.assertEquals(intended_bag_content, shopping_bag)


class TestShoppingBagContext(TestCase):

    def test_get_shopping_bag(self):

        """
        Gets the custom shopping bag context by
        making a get request to the index page.
        Ensures the context is equal to an empty
        dictionary.
        """

        response = self.client.get("/")
        self.assertEquals(response.context["context"], {})
