# Generated by Django 5.0 on 2024-01-03 08:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0014_product_brand'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shirt',
            name='brand',
        ),
    ]
