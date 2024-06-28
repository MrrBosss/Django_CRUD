# Generated by Django 5.0.6 on 2024-06-28 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0032_rename_weight_product_weights'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='weights',
            new_name='weight',
        ),
        migrations.RemoveField(
            model_name='productlist',
            name='product',
        ),
        migrations.AddField(
            model_name='productlist',
            name='banner',
            field=models.ManyToManyField(to='products.banner'),
        ),
        migrations.AddField(
            model_name='productlist',
            name='brand',
            field=models.ManyToManyField(to='products.brand'),
        ),
        migrations.AddField(
            model_name='productlist',
            name='content',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='productlist',
            name='faq',
            field=models.ManyToManyField(to='products.faq'),
        ),
        migrations.AddField(
            model_name='productlist',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='products'),
        ),
        migrations.AddField(
            model_name='productlist',
            name='price',
            field=models.DecimalField(decimal_places=2, default=99.99, max_digits=15),
        ),
        migrations.AddField(
            model_name='productlist',
            name='public',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='productlist',
            name='title',
            field=models.CharField(max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='productlist',
            name='weight',
            field=models.ManyToManyField(to='products.productweight'),
        ),
    ]
