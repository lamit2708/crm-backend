# Generated by Django 3.1.1 on 2020-11-10 11:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0008_auto_20201107_1707'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='is_all_day',
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='version',
        ),
    ]
