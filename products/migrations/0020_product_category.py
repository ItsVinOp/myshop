# Generated by Django 5.0 on 2024-01-03 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0019_remove_product_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ManyToManyField(to='products.category'),
        ),
    ]
