from django.test import TestCase
from django.contrib.auth.models import User
from django.test import Client
from . models import UserProfile


class TestModels(TestCase):

    def test_create_user_profile(self):

        test_user = User(username="User")
        test_user.save()

        test_profile = UserProfile(
            name="A name", address="A street", user=test_user)
        test_profile.save()

        self.assertEquals(test_profile.name, "A name")
        self.assertEquals(test_profile.address, "A street")
        self.assertEquals(test_profile.user.username, "User")

    def test_user_profile_to_string_method(self):

        test_user = User(username="User")
        test_user.save()

        test_profile = UserProfile(
            name="A name", address="A street", user=test_user)
        test_profile.save()

        self.assertEquals(test_profile.__str__(), "A name")


class TestViews(TestCase):

    def test_show_profile_view(self):

        test_user = User(username="User", password="Averysecretpassword")
        test_user.save()

        client = Client()

        client.force_login(test_user)

        self.assertTemplateUsed(client.get(
            "/profile/"), "profile/profile.html")
        self.assertEquals(client.get("/profile/").status_code, 200)

    def test_update_profile(self):

        test_user = User(
            username="User", password="Averysecretpassword", id="1")
        test_user.save()

        client = Client()

        client.force_login(test_user)

        get_profile = client.get("/profile/")

        test_response = client.post(
            "/profile/update_profile/",
            {"name": "Test", "address": "Street"})
        test_response_message = client.post(
            "/profile/update_profile/",
            {"name": "Test", "address": "Street"}, follow=True)

        intended_message = "Profile was updated"
        message = ""

        get_stored_messages = test_response_message.context["messages"]
        for message in get_stored_messages:
            message = message

        self.assertEquals(intended_message, message.__str__())
        self.assertEquals(test_response.status_code, 302)

