from django.test import TestCase
from . models import Store


class TestViews(TestCase):

    def test_get_store_view(self):
        self.assertEquals(self.client.get("/stores/").status_code, 200)
        self.assertTemplateUsed(
            self.client.get("/stores/"), "stores/view_stores.html")


class TestModels(TestCase):

    def test_create_store(self):
        test_store = Store(name="City",
                           city="Stockholm",
                           address="Street",
                           phone_number=9101101010,
                           open_hours="10-18")
        test_store.save()

        self.assertEquals(test_store.name, "City")
        self.assertEquals(test_store.city, "Stockholm")
        self.assertEquals(test_store.address, "Street")
        self.assertEquals(test_store.phone_number, 9101101010)
        self.assertEquals(test_store.open_hours, "10-18")

    def test_store_to_string_method(self):
        test_store = Store(name="City",
                           city="Stockholm",
                           address="Street",
                           phone_number=9101101010,
                           open_hours="10-18")
        test_store.save()

        self.assertEquals(test_store.__str__(), "City")
