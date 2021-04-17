from django.db import models
import uuid
from django.contrib.auth.models import User
from products.models import Product


class Order(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             null=True, blank=True)
    amount_paid = models.IntegerField()

    def __str__(self):
        return self.date


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)

    def __str__(self):
        return self.product
