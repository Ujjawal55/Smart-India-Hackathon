# Generated by Django 5.1 on 2024-09-27 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0012_alter_profile_blood_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='blood_group',
            field=models.CharField(max_length=6, null=True, verbose_name='Blood Type'),
        ),
    ]
