# Generated by Django 5.1 on 2024-09-27 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_profile_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='blood_group',
            field=models.CharField(choices=[('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('AB+', 'AB+'), ('AB-', 'AB-'), ('O+', 'O+'), ('O-', 'O-')], default=None, max_length=6, verbose_name='Blood Type'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True, verbose_name='Date of Birth'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.CharField(choices=[('male', 'male'), ('female', 'female'), ('other', 'other')], max_length=10, null=True, verbose_name='Gender'),
        ),
    ]
