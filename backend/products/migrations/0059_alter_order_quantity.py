# Generated by Django 5.0.6 on 2024-07-02 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0058_remove_order_result'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='quantity',
            field=models.IntegerField(default=0),
        ),
    ]