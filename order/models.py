from django.db import models
from account.models import CustomUser
from store.models import Product


class Address(models.Model):
    user = models.ForeignKey(CustomUser, models.CASCADE)
    address_user = models.CharField(max_length=250, blank=True, unique=True)
    city = models.CharField(max_length=50, blank=True)
    country = models.CharField(max_length=50, blank=True)
    postal_code = models.IntegerField(blank=True, unique=True)
    description = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.email + self.address_user

    def get_full_name(self):
        return self.user.first_name + " " + self.user.last_name


class Order(models.Model):
    order_info = models.ForeignKey(Address, models.CASCADE)
    product = models.ForeignKey(Product, models.CASCADE)
    order_price = models.DecimalField(max_digits=10, decimal_places=0)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return '{}'.format(self.id)
