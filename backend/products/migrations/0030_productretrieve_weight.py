# Generated by Django 5.0.6 on 2024-06-28 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0029_productlist_productretrieve'),
    ]

    operations = [
        migrations.AddField(
            model_name='productretrieve',
            name='weight',
            field=models.IntegerField(null=True),
        ),
    ]
