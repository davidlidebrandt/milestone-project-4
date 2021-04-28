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
    shipping_address = models.CharField(max_length=300)
    customer_name = models.CharField(max_length=200)
    customer_email = models.EmailField()

    def __str__(self):
        return self.customer_name


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    discount_rate = models.FloatField(default=1.0)

    def __str__(self):
        return self.product.name
