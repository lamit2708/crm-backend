# Generated by Django 3.1.1 on 2020-10-22 07:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AppointmentStatus',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=128)),
                ('description', models.TextField()),
            ],
            options={
                'db_table': 'crm_appointment_status',
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('code', models.CharField(blank=True, max_length=128, null=True)),
                ('fullname', models.CharField(max_length=128)),
                ('phone', models.CharField(max_length=20)),
                ('address', models.CharField(blank=True, max_length=50, null=True)),
                ('emergency_contact_person', models.CharField(blank=True, max_length=128, null=True)),
                ('emergency_contact_phone', models.CharField(blank=True, max_length=20, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('birth_day', models.IntegerField(blank=True, null=True)),
                ('birth_month', models.IntegerField(blank=True, null=True)),
                ('birth_year', models.IntegerField(blank=True, null=True)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=1, null=True)),
                ('facebook_link', models.CharField(blank=True, max_length=512, null=True)),
                ('job_title', models.CharField(blank=True, max_length=50, null=True)),
                ('created_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'crm_customer',
            },
        ),
        migrations.CreateModel(
            name='CustomerPriority',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=128)),
                ('description', models.TextField()),
            ],
            options={
                'db_table': 'crm_customer_priority',
            },
        ),
        migrations.CreateModel(
            name='CustomerSource',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=128)),
                ('description', models.TextField()),
            ],
            options={
                'db_table': 'crm_customer_source',
            },
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=128)),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'crm_department',
            },
        ),
        migrations.CreateModel(
            name='Permission',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=128)),
                ('description', models.TextField()),
                ('bit', models.IntegerField()),
            ],
            options={
                'db_table': 'crm_permission',
            },
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=128)),
                ('description', models.TextField()),
            ],
            options={
                'db_table': 'crm_role',
            },
        ),
        migrations.CreateModel(
            name='UIObject',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=128)),
                ('description', models.TextField()),
            ],
            options={
                'db_table': 'crm_ui_object',
            },
        ),
        migrations.CreateModel(
            name='UserRole',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='crm.role')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'crm_user_role',
            },
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('code', models.CharField(max_length=64)),
                ('fullname', models.CharField(max_length=128)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'crm_staff',
            },
        ),
        migrations.CreateModel(
            name='RolePermission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('permission_bit', models.IntegerField()),
                ('role', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='crm.role')),
                ('ui_object', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='crm.uiobject')),
            ],
            options={
                'db_table': 'crm_role_permission',
            },
        ),
        migrations.CreateModel(
            name='CustomerTransferHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_transfer_id', models.IntegerField(null=True)),
                ('transfer_date', models.DateTimeField(blank=True, null=True)),
                ('note', models.TextField(blank=True, null=True)),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='crm.customer')),
                ('department', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='crm.department')),
                ('process_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='customertransferhistory_process_user', to=settings.AUTH_USER_MODEL)),
                ('transfer_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='customertransferhistory_transfer_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'crm_customer_transfer_history',
            },
        ),
        migrations.CreateModel(
            name='CustomerTransfer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transfer_date', models.DateTimeField(auto_now_add=True)),
                ('note', models.TextField(blank=True, null=True)),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='crm.customer')),
                ('department', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='crm.department')),
                ('process_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='customertransfer_process_user', to=settings.AUTH_USER_MODEL)),
                ('transfer_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='customertransfer_transfer_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'crm_customer_transfer',
            },
        ),
        migrations.AddField(
            model_name='customer',
            name='customer_priority',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='crm.customerpriority'),
        ),
        migrations.AddField(
            model_name='customer',
            name='customer_source',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='crm.customersource'),
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('from_date', models.DateTimeField()),
                ('to_date', models.DateTimeField()),
                ('description', models.TextField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('appointment_status', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='crm.appointmentstatus')),
                ('created_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='crm.customer')),
                ('staff', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='crm.staff')),
            ],
            options={
                'db_table': 'crm_appointment',
            },
        ),
    ]