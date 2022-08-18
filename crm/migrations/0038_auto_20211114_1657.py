# Generated by Django 3.1.1 on 2021-11-14 16:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20211114_1647'),
        ('crm', '0037_auto_20211114_1607'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='district',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='core.district'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='province',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='core.province'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='ward',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='core.ward'),
        ),
    ]
