# Generated by Django 3.1.1 on 2021-01-14 05:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0023_remove_activity_activity_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='leadstatuscode',
            name='state',
        ),
        migrations.DeleteModel(
            name='Lead',
        ),
        migrations.DeleteModel(
            name='LeadStateCode',
        ),
        migrations.DeleteModel(
            name='LeadStatusCode',
        ),
    ]
