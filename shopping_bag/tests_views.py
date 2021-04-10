from django.test import TestCase


class TestViews(TestCase):
    def test_get_bag(self):
        self.assertEquals(self.client.get("/bag/").status_code, 200)
        self.assertTemplateUsed(
            self.client.get("/bag/"), "shopping_bag/bag.html")
