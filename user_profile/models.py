from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=300, blank=True)
    name = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.name
