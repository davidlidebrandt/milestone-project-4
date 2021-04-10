from django.test import TestCase


class TestViews(TestCase):
    def test_get_all_products_page(self):
        self.assertEquals(self.client.get("/products/").status_code, 200)
        self.assertTemplateUsed(
            self.client.get("/products/"), "products/products.html")
