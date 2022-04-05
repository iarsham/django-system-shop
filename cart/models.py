from django.db import models
from account.models import CustomUser
from store.models import Product


class Cart(models.Model):
    cart_id = models.CharField(max_length=50, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.cart_id


class CartItem(models.Model):
    cart_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    cart_product = models.ForeignKey(Product, models.CASCADE)
    cart = models.ForeignKey(Cart, models.CASCADE)
    quantity = models.PositiveIntegerField()
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.cart_product.product_name + " / Quantity: " + str(self.quantity)
