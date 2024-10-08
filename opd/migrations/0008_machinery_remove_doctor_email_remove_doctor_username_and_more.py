# Generated by Django 5.1 on 2024-09-07 11:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('opd', '0007_medicine_offline_patient_remove_product_owner_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Machinery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
            ],
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='email',
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='username',
        ),
        migrations.RemoveField(
            model_name='inventory',
            name='machinary',
        ),
        migrations.RemoveField(
            model_name='inventory',
            name='medicine',
        ),
        migrations.RemoveField(
            model_name='inventory',
            name='quantity',
        ),
        migrations.RemoveField(
            model_name='medicine',
            name='price',
        ),
        migrations.RemoveField(
            model_name='opd',
            name='inventory',
        ),
        migrations.RemoveField(
            model_name='opd',
            name='offline_patients',
        ),
        migrations.RemoveField(
            model_name='opd',
            name='online_patient',
        ),
        migrations.AddField(
            model_name='inventory',
            name='opd',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='inventorys', to='opd.opd'),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='opd',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Name'),
        ),
        migrations.CreateModel(
            name='Inventory_Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0, verbose_name='Quantity')),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Price')),
                ('inventory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inventory_items', to='opd.inventory')),
                ('medicine', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='inventory_items', to='opd.medicine')),
                ('machinery', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='inventory_items', to='opd.machinery')),
            ],
            options={
                'verbose_name_plural': 'Inventory Items',
            },
        ),
    ]
