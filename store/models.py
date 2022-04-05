from account.models import CustomUser
from django.db import models
from django.urls import reverse
import uuid


class Category(models.Model):
    category_name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)

    class Meta:
        verbose_name_plural = 'Category'

    def __str__(self):
        return self.category_name


class Product(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False, unique=True)
    category = models.ForeignKey(Category, models.CASCADE)
    product_name = models.CharField(max_length=50)
    price = models.PositiveIntegerField()
    discount = models.PositiveIntegerField(null=True, blank=True)
    product_image = models.ImageField(upload_to='photos/products', null=True, blank=True)
    product_image2 = models.ImageField(upload_to='photos/products', null=True, blank=True)
    product_image3 = models.ImageField(upload_to='photos/products', null=True, blank=True)
    added_date = models.DateTimeField(auto_now_add=True)
    # Detail
    description = models.TextField(blank=True)
    brand_logo = models.ImageField(upload_to='photos/brand', null=True)
    product_brand = models.CharField(max_length=50, blank=True)
    os = models.CharField(max_length=40, blank=True)
    processor = models.CharField(max_length=250, blank=True)
    processor_technology = models.CharField(max_length=250, blank=True)
    graphics = models.CharField(max_length=250, blank=True)
    memory = models.CharField(max_length=250, blank=True)
    hard_drive = models.CharField(max_length=250, blank=True)
    wireless = models.CharField(max_length=250, blank=True)
    power_supply = models.CharField(max_length=250, blank=True)
    battery = models.CharField(max_length=250, blank=True)
    color = models.CharField(max_length=250, blank=True)
    storage = models.CharField(max_length=250, blank=True)
    screen = models.CharField(max_length=250, blank=True)

    def __str__(self):
        return self.product_name

    def get_absolute_url(self):
        return reverse('detail-products', args=[self.id])


class Comment(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False, unique=True)
    writer = models.ForeignKey(CustomUser, models.CASCADE, blank=True)
    reply_product = models.ForeignKey(Product, models.CASCADE, blank=True)
    text_comment = models.TextField(blank=True)
    date_entry = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{}".format(self.writer.username)
