# Generated by Django 3.1.1 on 2020-12-25 12:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0020_auto_20201225_1155'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activity',
            name='description',
        ),
    ]
