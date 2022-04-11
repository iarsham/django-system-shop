# Generated by Django 4.0.3 on 2022-04-08 21:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
        ('order', '0008_remove_address_order_item'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_price', models.DecimalField(decimal_places=0, max_digits=10)),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('order_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.address')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.product')),
            ],
        ),
    ]
