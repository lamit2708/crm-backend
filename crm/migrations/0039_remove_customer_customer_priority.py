# Generated by Django 3.1.1 on 2021-11-21 08:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0038_auto_20211114_1657'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='customer_priority',
        ),
    ]
