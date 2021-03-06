from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    image_url = models.URLField(blank=True)

    def __str__(self):
        return self.name


class Manufacturer(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.name


class Discount(models.Model):
    name = models.CharField(max_length=10)
    rate = models.FloatField()

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    description = models.CharField(max_length=200, null=False, blank=False)
    image_url = models.URLField(blank=True)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, blank=True)
    manufacturer = models.ForeignKey(
        Manufacturer, on_delete=models.CASCADE, null=False, blank=False)
    prize = models.IntegerField(null=False, blank=False)
    discount_rate = models.ForeignKey(
        Discount, on_delete=models.SET_NULL, null=True, blank=True)
    units_sold = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    objects = models.Manager()


class Review(models.Model):
    class Stars(models.IntegerChoices):
        ONE = 1
        TWO = 2
        THREE = 3
        FOUR = 4
        FIVE = 5
    by_user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=False)
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, null=True, blank=False)
    description = models.CharField(max_length=400, null=False, blank=False, )
    rating = models.IntegerField(choices=Stars.choices)

    def __str__(self):
        return self.description

    objects = models.Manager()
