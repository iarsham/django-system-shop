# Generated by Django 4.0.3 on 2022-04-05 15:40

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_remove_cartitem_cart_delete_cart'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('order', '0005_rename_order_orders'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Orders',
            new_name='Address',
        ),
    ]
