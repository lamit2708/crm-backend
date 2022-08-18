# Generated by Django 3.1.1 on 2021-01-14 06:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0025_customertype'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='customer_type',
            field=models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='crm.customertype'),
        ),
    ]