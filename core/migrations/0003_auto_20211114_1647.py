# Generated by Django 3.1.1 on 2021-11-14 16:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_init_address_data'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Wards',
            new_name='Ward',
        ),
        migrations.RenameModel(
            old_name='WardsLevel',
            new_name='WardLevel',
        ),
        migrations.AlterModelTable(
            name='ward',
            table='core_ward',
        ),
        migrations.AlterModelTable(
            name='wardlevel',
            table='core_ward_level',
        ),
    ]
