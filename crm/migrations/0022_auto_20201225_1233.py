# Generated by Django 3.1.1 on 2020-12-25 12:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0021_remove_activity_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='activity',
            old_name='ActivityId',
            new_name='activity_id',
        ),
        migrations.RenameField(
            model_name='activity',
            old_name='ActivityType',
            new_name='activity_type',
        ),
        migrations.RenameField(
            model_name='activity',
            old_name='RegardingObjectId',
            new_name='regarding_object_id',
        ),
        migrations.RenameField(
            model_name='activity',
            old_name='RegardingObjectTypeCode',
            new_name='regarding_object_type',
        ),
    ]