from django.contrib import admin
from .models import *


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['category_name', 'slug']
    prepopulated_fields = {'slug': ('category_name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['category', 'product_name']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['writer', 'reply_product']
