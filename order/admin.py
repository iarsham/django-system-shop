from django.contrib import admin
from .models import Orders


@admin.register(Orders)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'country', 'address']
