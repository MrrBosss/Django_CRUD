# Generated by Django 4.0.10 on 2024-06-07 11:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_alter_product_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='user',
        ),
    ]
