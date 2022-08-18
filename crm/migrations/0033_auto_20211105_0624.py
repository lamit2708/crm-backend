# Generated by Django 3.1.1 on 2021-11-05 06:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('crm', '0032_auto_20211105_0614'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='staff',
            name='fullname',
        ),
        migrations.AddField(
            model_name='staff',
            name='first_name',
            field=models.CharField(default='', max_length=150),
        ),
        migrations.AlterField(
            model_name='staff',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]