from os import name
from django.conf import settings
from django.db import models
from django.db.models.deletion import DO_NOTHING
from django.db.models.fields.related import ForeignKey
from django.views.defaults import permission_denied
from rest_framework.generics import DestroyAPIView
from authentication.models import User
from core.models import Ward, District, Province
from django.apps import apps
from django.db.models.signals import post_save
from django.dispatch import receiver
import reversion
from django.contrib import admin
from reversion.admin import VersionAdmin
from django.core.validators import MinValueValidator, MaxValueValidator
# from django.contrib.auth.models import User
GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female'),
    ('O', 'Other')
)

FREQ_TYPE_CHOICES = (
    (1, 'Once'),
    (4, 'Daily'),
    (8, 'Weekly'),
    (16, 'Monthly'),
)
DAY_OF_WEEK_CHOICES = (
    (1, 'Sunday'),
    (2, 'Monday'),
    (4, 'Tuesday'),
    (8, 'Wednesday'),
    (16, 'Thursday'),
    (32, 'Firday'),
    (64, 'Saturday'),
)
CUSTOMER_TYPE_CHOICES = (
    (0, 'Tiềm năng'),
    (1, 'Khách hàng'),

)

TASK_PRIORITY_CHOICES = (

    (1, 'Không'),
    (2, 'Cao'),
)

TASK_TYPE_CHOICES = (
    (0, 'Gọi'),
    (1, 'Email'),
    (2, 'SMS'),
    (3, 'Đặt hẹn'),
    (4, 'Họp'),
    (5, 'Báo giá'),
    #(6,'Ghi chú')
)
# CUSTOMER_TYPE_CHOICES=(
#     (0,'Tiềm năng'),
#     (1,'Khách hàng')
# )


class CustomerType(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'crm_customer_type'


class CustomerPriority(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128)
    description = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'crm_customer_priority'


class Customer(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=128, blank=True, null=True)
    fullname = models.CharField(max_length=128)
    phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=254, blank=True, null=True)
    address = models.CharField(max_length=128, blank=True, null=True)
    ward = models.ForeignKey(
        Ward, blank=True, null=True, on_delete=models.DO_NOTHING)
    district = models.ForeignKey(
        District, blank=True, null=True, on_delete=models.DO_NOTHING)
    province = models.ForeignKey(
        Province, blank=True, null=True, on_delete=models.DO_NOTHING)
    created_user = models.ForeignKey(
        settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL)
    emergency_contact_person = models.CharField(
        max_length=128, blank=True, null=True)
    emergency_contact_phone = models.CharField(
        max_length=20, blank=True, null=True)
    created_date = models.DateTimeField(auto_now=False, auto_now_add=True)
    # birth_day = models.IntegerField(blank=True, null=True)
    # birth_month = models.IntegerField(blank=True, null=True)
    # birth_year = models.IntegerField(blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)

    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=True)
    # customer_priority = models.ForeignKey( 'CustomerPriority', blank = True, null = True, on_delete = models.SET_NULL)
    facebook_link = models.CharField(max_length=512, blank=True, null=True)
    customer_source = models.ForeignKey(
        'CustomerSource', blank=True, null=True, on_delete=models.SET_NULL)
    job_title = models.CharField(max_length=50, blank=True, null=True)
    customer_type = models.ForeignKey(
        CustomerType, on_delete=models.DO_NOTHING, blank=True, null=True, default=1)

    def __str__(self):
        return self.fullname

    class Meta:
        db_table = 'crm_customer'


class Department(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'crm_department'


class CustomerTransfer(models.Model):

    customer = models.ForeignKey(
        Customer, null=True, on_delete=models.SET_NULL)
    department = models.ForeignKey(
        Department, null=True,  on_delete=models.CASCADE)

    transfer_date = models.DateTimeField(auto_now=False, auto_now_add=True)
    transfer_user = models.ForeignKey(
        User, null=True, on_delete=models.CASCADE, related_name="%(class)s_transfer_user")
    process_user = models.ForeignKey(
        User, null=True, on_delete=models.CASCADE, related_name="%(class)s_process_user")
    note = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'crm_customer_transfer'


@ receiver(post_save, sender=CustomerTransfer)
def hear_signal(sender, instance, **kwargs):
    # if kwargs.get('created') or kwargs.get():
    CustomerTransferHistory.objects.create(
        customer_transfer_id=instance.id,
        customer_id=instance.customer_id,
        department_id=instance.department_id,
        transfer_date=instance.transfer_date,
        transfer_user_id=instance.transfer_user_id,
        note=instance.note)

    # Do whatever you want.
    # Your trigger function content.
    # Parameter "instance" will have access to all the attributes of the model being saved. To quote from docs : It's "The actual instance being saved."

    return


class CustomerTransferHistory(models.Model):
    customer_transfer_id = models.IntegerField(
        null=True)
    customer = models.ForeignKey(Customer,
                                 null=True, on_delete=models.SET_NULL)
    department = models.ForeignKey(
        Department, null=True, on_delete=models.SET_NULL)
    transfer_user = models.ForeignKey(
        User, null=True, on_delete=models.CASCADE, related_name="%(class)s_transfer_user")
    transfer_date = models.DateTimeField(blank=True, null=True)
    process_user = models.ForeignKey(
        User, null=True, on_delete=models.CASCADE, related_name="%(class)s_process_user")
    note = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'crm_customer_transfer_history'


class CustomerSource(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128)
    description = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'crm_customer_source'


@ reversion.register()
class Appointment(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=128, default='')
    customer = models.ForeignKey(
        'Customer', null=True, on_delete=models.SET_NULL)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             null=True, on_delete=models.SET_NULL)
    appointment_status = models.ForeignKey(
        'AppointmentStatus', null=True, on_delete=models.SET_NULL)
    description = models.TextField(null=True, blank=True)
    # is_all_day = models.BooleanField(null=True)
    created_date = models.DateTimeField(auto_now=True, auto_now_add=False)
    created_user = models.ForeignKey(
        settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL, related_name="%(class)s_created_user")
    is_active = models.BooleanField(default=True)
    modiefied_date = models.DateTimeField(
        auto_now=False, null=True, auto_now_add=True)
    modified_user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True,
                                      on_delete=models.DO_NOTHING, related_name="%(class)s_modified_user")

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'crm_appointment'


# reversion.register(Appointment)
# @admin.register(Appointment)
# class AppointmentAdmin(VersionAdmin):
#     pass


class Staff(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=64)
    # Family name = Surname = Last name = Phần “họ” trong tiếng Việt.
    # English: Full name = First name + Middle name + Last name/ Family name.
    # VN1: Nguyễn Ngọc Mỹ Anh =>    First name: Anh + Last name: Nguyen Ngoc My
    # VN2: Nguyễn Ngọc Mỹ Anh =>    First name: Ngoc My Anh +Family name: Nguyen
    last_name = models.CharField(max_length=150, default='')
    first_name = models.CharField(max_length=150, default='')
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL)
    # appointment_status = models.ForeignKey('AppointmentStatus', null=True, on_delete=models.SET_NULL)
    # department = models.CharField(max_length=100)
    job_title = models.ForeignKey(
        'JobTitle', null=True, on_delete=models.SET_NULL)
    department = models.ForeignKey(
        'Department', null=True, on_delete=models.SET_NULL)
    email = models.EmailField(max_length=254, blank=True, null=True)
    staff_group = models.ForeignKey(
        'StaffGroup', null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"{self.code} - {self.last_name} {self.first_name}"
    # def __str__(self):
    #     return "{0} {1}".format(self.usr.first_name, self.usr.last_name)

    class Meta:
        db_table = 'crm_staff'


class AppointmentStatus(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128)
    description = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'crm_appointment_status'


class UIObject(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128)
    description = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'crm_ui_object'


class Role(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128)
    description = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'crm_role'


class UserRole(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             null=True, on_delete=models.SET_NULL)
    role = models.ForeignKey(Role, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.user_id

    class Meta:
        db_table = 'crm_user_role'


class RolePermission(models.Model):
    role = models.ForeignKey(Role, null=True, on_delete=models.SET_NULL)
    ui_object = models.ForeignKey(
        UIObject, null=True, on_delete=models.SET_NULL)
    permission_bit = models.IntegerField()

    def __str__(self):
        return self.ui_object_id

    class Meta:
        db_table = 'crm_role_permission'


class Permission(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128)
    description = models.TextField()
    bit = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'crm_permission'

# https://docs.microsoft.com/en-us/sql/relational-databases/system-tables/dbo-sysschedules-transact-sql?redirectedfrom=MSDN&view=sql-server-ver15


class Schedule(models.Model):
    owner_id = models.ForeignKey(
        User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    modified_date = models.DateTimeField()
    # freq_type: 1 (once),
    freq_type = models.IntegerField(
        choices=FREQ_TYPE_CHOICES, null=True)
    # freq_type=8  (weekly)=> freq_interval: 1 = Sunday, 2 = Monday, 4 = Tuesday, 8 = Wednesday, 16 = Thursday, 32 = Friday, 64 = Saturday
    freq_interval = models.IntegerField(
        choices=DAY_OF_WEEK_CHOICES, null=True)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    start_time = models.TimeField(null=True)
    end_time = models.TimeField(null=True)
    created_date = models.DateTimeField(
        auto_now=True, auto_now_add=False)
    created_user = models.ForeignKey(
        settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL, related_name="%(class)s_created_user")
    version = models.IntegerField()


class TaskType(models.Model):
    # Call, SMS, Email, Note, Quote,
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'crm_task_type'


class TaskStatus(models.Model):
    # Chưa bắt đầu, Chờ, Đang tiến hành, Hoàn thành, Hủy
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'crm_task_status'


class TaskPriority(models.Model):
    # Cao, Vừa, Thấp
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'crm_task_priority'


class Task(models.Model):
    task_date = models.DateTimeField()
    client_id = models.IntegerField(blank=True, null=True)
    # client=True => Customer, False => Lead
    client_type = models.BooleanField(blank=True, null=True, default=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.DO_NOTHING, related_name="%(class)s_user")
    task_type = models.ForeignKey(
        TaskType, blank=True, default=1, on_delete=models.DO_NOTHING)
    task_status = models.ForeignKey(
        TaskStatus, blank=True, default=1, on_delete=models.DO_NOTHING)
    task_priority = models.ForeignKey(
        TaskPriority, blank=True, default=1, on_delete=models.DO_NOTHING)
    description = models.TextField(blank=True, null=True)
    created_date = models.DateTimeField(auto_now=True, auto_now_add=False)
    created_user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, related_name="%(class)s_created_user")

    class Meta:
        db_table = 'crm_task'


# class LeadStateCode(models.Model):
#     name = models.CharField(max_length=128)

#     class Meta:
#         db_table = 'crm_lead_state_code'


class LeadStatusCode(models.Model):
    # Open (Unassigned), Contacted, Qualified, Converted,
    # Cannot Contact, Waiting for details, In Progress
    # Important, To follow, Conference ...
    name = models.CharField(max_length=150)
    # state = models.ForeignKey(
    #     LeadStateCode, blank=True, null=True, on_delete=models.DO_NOTHING)

    class Meta:
        db_table = 'crm_lead_status_code'


class LeadTimeFrame(models.Model):
    name = models.TextField()
    value = models.IntegerField(default=0)

    class Meta:
        db_table = 'crm_lead_time_frame'


class Lead(models.Model):

    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=128, blank=True, null=True)
    first_name = models.CharField(max_length=150, blank=True, null=True)
    last_name = models.CharField(max_length=150, blank=True, null=True)
    phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=254, blank=True, null=True)
    address = models.CharField(max_length=128, blank=True, null=True)
    created_user = models.ForeignKey(
        settings.AUTH_USER_MODEL, null=True, on_delete=models.DO_NOTHING)
    created_date = models.DateTimeField(auto_now=True, auto_now_add=False)
    birth_date = models.DateField(blank=True, null=True)

    gender = models.CharField(
        max_length=1, choices=GENDER_CHOICES, null=True)
    facebook_link = models.CharField(max_length=512, blank=True, null=True)
    customer_source = models.ForeignKey(
        'CustomerSource', blank=True, null=True, on_delete=models.DO_NOTHING)
    job_title = models.CharField(max_length=50, blank=True, null=True)
    # score
    interest = models.TextField(blank=True, null=True)
    company = models.TextField(blank=True, null=True)
    staff = models.ForeignKey(
        Staff, blank=True, null=True, on_delete=models.DO_NOTHING)
    # customer = models.ForeignKey(
    #     Customer, blank=True, null=True, on_delete=models.DO_NOTHING)
    # state = models.ForeignKey(
    #     LeadStateCode, blank=True, null=True, on_delete=models.DO_NOTHING)
    status = models.ForeignKey(
        LeadStatusCode, blank=True, null=True, on_delete=models.DO_NOTHING)
    authority = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(5)], default=0)
    budget = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(5)], default=0)
    need = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(5)], default=0)
    timeframe = models.ForeignKey(
        LeadTimeFrame, on_delete=models.DO_NOTHING, blank=True, null=True)
    # behavior

    def get_lead_score(self):
        """
        Return the first_name plus the last_name, with a space in between.
        """
        # lead_score = '%s %s' % (self.first_name, self.last_name)
        lead_score = self.need+self.budget+self.decision_maker
        return lead_score

    def __str__(self):
        fullname = '%s %s' % (self.first_name, self.last_name)
        return fullname.strip()

    class Meta:
        db_table = 'crm_lead'


class ActivityType(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "crm_activity_type"


class Activity(models.Model):
    subject = models.CharField(max_length=255)
    activity_type = models.ForeignKey(
        ActivityType, on_delete=models.DO_NOTHING)
    regarding_object_id = models.IntegerField(blank=True, null=True)
    regarding_object_type = models.CharField(
        max_length=128, blank=True, null=True)
    client_id = models.IntegerField()
    client_type = models.BooleanField(
        default=True)  # True=Customer, False=Lead
    created_date = models.DateTimeField(auto_now=True, auto_now_add=False)
    created_user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, related_name="%(class)s_created_user")

    def __str__(self):
        return self.subject

    class Meta:
        db_table = 'crm_activity'


class StaffGroup(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'crm_staff_group'


class JobTitle(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'crm_job_title'
