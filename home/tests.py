from django.test import TestCase


class TestViews(TestCase):
    def test_get_index_page(self):
        self.assertEquals(self.client.get("/").status_code, 200)
        self.assertTemplateUsed(self.client.get("/"), "home/index.html")

    def test_get_non_existent_page(self):
        self.assertEquals(self.client.get("/1").status_code, 404)
        self.assertTemplateUsed(self.client.get("/1"), "home/404.html")
