# Generated by Django 4.0.2 on 2022-03-31 20:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Order_item',
        ),
    ]