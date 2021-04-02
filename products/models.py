from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.name


class Manufacturer(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    description = models.CharField(max_length=200, null=False, blank=False)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, blank=True)
    manufacturer = models.ForeignKey(
        Manufacturer, on_delete=models.CASCADE, null=False, blank=False)

    def __str__(self):
        return self.name


class Review(models.Model):
    by_user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=False, blank=False)
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, null=False, blank=False)
    description = models.CharField(max_length=400, null=False, blank=False)

    def __str__(self):
        return self.description