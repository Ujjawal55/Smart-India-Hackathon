# Generated by Django 5.1 on 2024-09-10 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('opd', '0019_alter_inventory_item_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='opd',
            name='no_of_appointment',
            field=models.IntegerField(default=0, verbose_name='No of Appointment'),
        ),
    ]
