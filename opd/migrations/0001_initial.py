# Generated by Django 5.1 on 2024-09-05 20:33

import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('username', models.CharField(max_length=200, verbose_name='Username')),
                ('name', models.CharField(max_length=200, verbose_name='Full Name')),
                ('email', models.EmailField(max_length=190, verbose_name='Email')),
                ('profile_image', models.ImageField(default='profile/default-profile.png', upload_to='profile/', verbose_name='Image')),
                ('speciality', models.CharField(max_length=200, verbose_name='Speciality')),
                ('phone_number', models.CharField(max_length=10, verbose_name='Phone Number')),
                ('street_address', models.CharField(max_length=255, verbose_name='Street Address')),
                ('city', models.CharField(max_length=255, verbose_name='City')),
                ('experience', models.IntegerField(verbose_name='Year of Experience')),
                ('about', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='doctor', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
