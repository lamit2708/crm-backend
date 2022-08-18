
from rest_framework import serializers
from .models import *


class CustomerPrioritySerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerPriority
        fields = '__all__'


class CustomerTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerType
        fields = '__all__'


class CustomerSerializer(serializers.ModelSerializer):
    customer_type_name = serializers.SerializerMethodField()
    province_name = serializers.SerializerMethodField()
    district_name = serializers.SerializerMethodField()
    ward_name = serializers.SerializerMethodField()
    customer_source_name = serializers.SerializerMethodField()

    class Meta:
        model = Customer
        fields = '__all__'

    def get_customer_type_name(self, obj):
        if obj.customer_type is not None:
            return obj.customer_type.name

    def get_province_name(self, obj):
        if obj.province is not None:
            return obj.province.name

    def get_district_name(self, obj):
        if obj.district is not None:
            return obj.district.name

    def get_ward_name(self, obj):
        if obj.ward is not None:
            return obj.ward.name

    def get_customer_source_name(self, obj):
        if obj.customer_source is not None:
            return obj.customer_source.name


class CustomerSourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerSource
        fields = '__all__'


class AppointmentSerializer(serializers.ModelSerializer):
    customer_fullname = serializers.SerializerMethodField()

    class Meta:
        model = Appointment
        fields = '__all__'

    def get_customer_fullname(self, obj):
        if obj.customer is not None:
            return obj.customer.fullname


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class StaffSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()
    job_title_name = serializers.SerializerMethodField()
    department_name = serializers.SerializerMethodField()
    staff_group_name = serializers.SerializerMethodField()

    class Meta:
        model = Staff
        fields = '__all__'

    def get_full_name(self, obj):
        # return '%s %s' % (obj.first_name, obj.last_name)
        return obj.last_name+" "+obj.first_name

    def get_job_title_name(self, obj):
        return obj.job_title.name

    def get_department_name(self, obj):
        return obj.department.name

    def get_staff_group_name(self, obj):
        return obj.staff_group.name


class AppointmentStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppointmentStatus
        fields = '__all__'


class UIObjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = UIObject
        fields = '__all__'


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'


class UserRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRole
        fields = '__all__'


class RolePermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = RolePermission
        fields = '__all__'


class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = '__all__'


class CustomerTransferSerializer(serializers.ModelSerializer):
    # customer_info = serializers.SerializerMethodField()
    fullname = serializers.SerializerMethodField()
    code = serializers.SerializerMethodField()
    department_name = serializers.SerializerMethodField()

    class Meta:
        model = CustomerTransfer
        # fields = '__all__'
        fields = ('id', 'customer', 'code', 'fullname',
                  'department', 'department_name', 'note', 'transfer_user', 'transfer_date', 'process_user')

    def get_fullname(self, obj):
        if obj.customer is not None:
            return obj.customer.fullname

    def get_code(self, obj):
        if obj.customer is not None:
            return obj.customer.code

    def get_department_name(self, obj):
        if obj.department is not None:
            return obj.department.name

    def get_customer_info(self, obj):
        # https://stackoverflow.com/questions/42775784/how-to-serialize-a-queryset-from-an-unrelated-model-as-a-nested-serializer?rq=1
        customer_id = obj.customer.id
        queryset = Customer.objects.get(id=customer_id)
        return CustomerSerializer(queryset, read_only=True).data


class CustomerTransferHistorySerializer(serializers.ModelSerializer):
    # customer_info = serializers.SerializerMethodField()
    fullname = serializers.SerializerMethodField()
    code = serializers.SerializerMethodField()
    phone = serializers.SerializerMethodField()
    department_name = serializers.SerializerMethodField()
    transfer_user_fullname = serializers.SerializerMethodField()
    process_user_fullname = serializers.SerializerMethodField()

    class Meta:
        model = CustomerTransferHistory
        # fields = '__all__'
        fields = ('id', 'customer_transfer_id', 'customer', 'code', 'fullname', 'phone',
                  'department', 'department_name', 'note', 'transfer_user',
                  'transfer_user_fullname', 'transfer_date', 'process_user',
                  'process_user_fullname')

    def get_fullname(self, obj):
        if (obj.customer == None):
            return 'Unknown'
        return obj.customer.fullname

    def get_code(self, obj):
        # if obj.customer is not None:
        if (obj.customer == None):
            return 'Unknown'
        return obj.customer.code

    def get_phone(self, obj):
        if (obj.customer == None):
            return 'Unknown'
        return obj.customer.phone

    def get_department_name(self, obj):
        return obj.department.name

    def get_transfer_user_fullname(self, obj):
        if obj.transfer_user is not None:
            return obj.transfer_user.fullname

    def get_process_user_fullname(self, obj):
        if obj.process_user is not None:
            return obj.process_user.fullname


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'


class TaskTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskType
        fields = '__all__'


class TaskStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskStatus
        fields = '__all__'


class TaskPrioritySerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskPriority
        fields = '__all__'


class TaskSerializer(serializers.ModelSerializer):
    task_type_name = serializers.SerializerMethodField()
    task_priority_name = serializers.SerializerMethodField()
    task_status_name = serializers.SerializerMethodField()
    user_fullname = serializers.SerializerMethodField()
    created_user_fullname = serializers.SerializerMethodField()
    # fields = '__all__'

    class Meta:
        model = Task
        fields = '__all__'

    def get_task_type_name(self, obj):
        if obj.task_type is not None:
            return obj.task_type.name

    def get_task_priority_name(self, obj):
        if obj.task_priority is not None:
            return obj.task_priority.name

    def get_task_status_name(self, obj):
        if obj.task_status is not None:
            return obj.task_status.name

    def get_user_fullname(self, obj):
        if obj.user is not None:
            return obj.user.fullname

    def get_created_user_fullname(self, obj):
        if obj.created_user is not None:
            return obj.created_user.fullname


class ActivityTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityType
        fields = '__all__'


class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = '__all__'


class LeadStatusCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeadStatusCode
        fields = '__all__'


class LeadTimeFrameSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeadTimeFrame
        fields = '__all__'


class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lead
        fields = '__all__'


class JobTitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobTitle
        fields = '__all__'


class JobTitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobTitle
        fields = '__all__'


class StaffGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = StaffGroup
        fields = '__all__'
