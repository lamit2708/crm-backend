# Generated by Django 3.1.1 on 2020-12-10 15:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0016_auto_20201210_0802'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='end_date',
            new_name='task_date',
        ),
        migrations.RemoveField(
            model_name='task',
            name='start_date',
        ),
    ]
