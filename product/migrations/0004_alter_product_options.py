# Generated by Django 3.2.4 on 2021-09-07 17:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_rename_products_product_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'Product', 'verbose_name_plural': 'Products'},
        ),
    ]