# Generated by Django 3.1.1 on 2021-11-14 12:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0035_auto_20211114_1204'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='birth_day',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='birth_month',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='birth_year',
        ),
    ]