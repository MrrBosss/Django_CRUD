# Generated by Django 5.0.6 on 2024-06-28 12:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0033_rename_weights_product_weight_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ProductRetrieve',
        ),
        migrations.RemoveField(
            model_name='product',
            name='banner',
        ),
        migrations.RemoveField(
            model_name='product',
            name='brand',
        ),
        migrations.RemoveField(
            model_name='product',
            name='faq',
        ),
    ]
