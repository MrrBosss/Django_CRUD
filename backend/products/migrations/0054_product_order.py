# Generated by Django 5.0.6 on 2024-07-02 01:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0053_remove_order_product_order_color_order_weight_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='order',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='products.order'),
        ),
    ]
