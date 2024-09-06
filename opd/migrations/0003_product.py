# Generated by Django 5.1 on 2024-09-06 07:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('opd', '0002_alter_doctor_about_alter_doctor_city_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('Category', models.CharField(max_length=255, verbose_name='Category')),
                ('stock', models.IntegerField(default=0, verbose_name='Stock')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='opd.doctor')),
            ],
        ),
    ]
