# Generated by Django 5.1 on 2024-09-08 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('opd', '0017_alter_appointment_unique_together_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='status',
            field=models.CharField(blank=True, choices=[('seen', 'seen'), ('not_seen', 'not_seen')], max_length=20, null=True, verbose_name='Status'),
        ),
    ]
