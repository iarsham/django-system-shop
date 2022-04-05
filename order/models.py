from django.db import models
from account.models import CustomUser
from store.models import Product
from cart.models import CartItem


class Orders(models.Model):
    user = models.ForeignKey(CustomUser, models.CASCADE)
    order_item = models.ManyToManyField(CartItem)
    address = models.CharField(max_length=250, blank=True, unique=True)
    city = models.CharField(max_length=50, blank=True)
    country = models.CharField(max_length=50, blank=True)
    postal_code = models.IntegerField(blank=True, unique=True)
    description = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.email + self.address

    def get_full_name(self):
        return self.user.first_name + " " + self.user.last_name
