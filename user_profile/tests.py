from django.test import TestCase
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib.sessions.models import Session
from django.contrib.sessions.middleware import SessionMiddleware
from django.http import HttpRequest
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

    def test_get_profile_view(self):

        test_user = User(username="User")
        test_user.save()

        test_session = self.client.session()
        test_session["user"] = {"id": test_user.id}
        test_session.create()
        print(test_user.id)

        request = HttpRequest()

        middleware = SessionMiddleware()
        middleware.process_request(request)

        request.session.save()

        self.assertEquals(self.client.get("/profile/").status_code, 200)
        self.assertTemplateUsed(self.client.get(
            "/profile/"), "profile/profile.html")
