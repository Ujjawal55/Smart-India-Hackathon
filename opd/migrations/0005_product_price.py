# Generated by Django 5.1 on 2024-09-06 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('opd', '0004_rename_category_product_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.IntegerField(default=0, verbose_name='Price'),
        ),
    ]
