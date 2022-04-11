from django.contrib import admin
from .models import Address, Order


@admin.register(Address)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'country', 'address_user']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['order_info', 'product', 'order_price', 'quantity']
