# Generated by Django 5.0.6 on 2024-07-02 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0056_rename_count_order_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='result',
            field=models.IntegerField(null=True),
        ),
    ]
