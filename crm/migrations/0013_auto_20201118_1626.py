# Generated by Django 3.1.1 on 2020-11-18 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0012_task_taskpriority_taskstatus_tasktype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='end_date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='task',
            name='start_date',
            field=models.DateTimeField(),
        ),
    ]
