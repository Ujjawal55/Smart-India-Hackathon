# Generated by Django 5.1 on 2024-09-08 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('opd', '0016_alter_appointment_status'),
        ('user', '0008_profile_gender'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='appointment',
            unique_together={('opd', 'offline_patient'), ('opd', 'online_patient')},
        ),
        migrations.AlterField(
            model_name='appointment',
            name='appointment_id',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Appointment ID'),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='appointment_type',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Appointment Type'),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='status',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Status'),
        ),
    ]
