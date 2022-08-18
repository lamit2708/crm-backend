from django_filters.filters import DateFromToRangeFilter
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from aznose.pagination import StandardPagination
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from crm.serializers import *
from authentication.models import User
from rest_framework import viewsets
from django.shortcuts import get_object_or_404, render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import status
from django.db.models import Q
from rest_framework import pagination
from django_filters import rest_framework as filters
import unidecode
from django.contrib.auth.views import FormView
from reversion.views import RevisionMixin


class CRUDCustomerPriorityView(viewsets.GenericViewSet, ListCreateAPIView, RetrieveUpdateDestroyAPIView):
    serializer_class = CustomerPrioritySerializer
    queryset = CustomerPriority.objects.all()
    permission_classes = (AllowAny,)
    lookup_field = 'id'


class CustomerTypeView(viewsets.ModelViewSet):
    serializer_class = CustomerTypeSerializer
    queryset = CustomerType.objects.all()
    permission_classes = (AllowAny,)
    lookup_field = 'id'


class CustomerFilter(filters.FilterSet):
    created_date = DateFromToRangeFilter()
    fullname = filters.CharFilter()
    phone = filters.CharFilter()
    code = filters.CharFilter()
    # email = filters.CharFilter()

    class Meta:
        model = Customer
        fields = {'created_date': ['exact'],
                  'fullname': ['exact', 'icontains'],
                  'phone': ['exact', 'icontains'],
                  'code': ['exact', 'icontains'],
                  }


class CustomerView(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()
    lookup_field = 'id'
    pagination_class = StandardPagination
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = CustomerFilter
    # filterset_fields = {
    #     'created_date': ['gte', 'lte', 'exact', 'gt', 'lt'],
    # }
    # search_fields = []

    def get_queryset(self):
        queryset = super().get_queryset()
        # search = self.kwargs['search']
        last_code = self.request.query_params.get('last_code', None)

        if (last_code is not None):
            if last_code == "1":
                last_customer = queryset.order_by('-code')[:1]
                return last_customer
            else:
                return Customer.objects.none()
        code = self.request.query_params.get('code', None)
        if code is not None:
            return queryset.filter(code=code)
        customer_type = self.request.query_params.get('customer_type', None)
        if customer_type is not None:
            queryset = queryset.filter(customer_type=customer_type)
        search = self.request.query_params.get('search', None)
        if search is None:
            return queryset.order_by('-created_date')
        unaccented_search = unidecode.unidecode(search)
        if search != unaccented_search:
            queryset = queryset.filter(
                Q(fullname__icontains=search))
        else:
            queryset = queryset.filter(
                Q(fullname__unaccent__icontains=search) |
                Q(code__icontains=search) |
                Q(phone__icontains=search))

        return queryset.order_by('-created_date')


class CRUDCustomerSourceView(viewsets.GenericViewSet, ListCreateAPIView, RetrieveUpdateDestroyAPIView):
    serializer_class = CustomerSourceSerializer
    queryset = CustomerSource.objects.all()
    permission_classes = (AllowAny,)
    lookup_field = 'id'


class AppointmentFilter(filters.FilterSet):
    start_date = DateFromToRangeFilter()

    class Meta:
        model = Appointment
        fields = {'start_date': ['exact'],
                  }


class AppointmentView(viewsets.ModelViewSet, RevisionMixin):
    serializer_class = AppointmentSerializer
    queryset = Appointment.objects.all()
    permission_classes = (AllowAny,)
    lookup_field = 'id'
    #pagination_class = StandardPagination
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = AppointmentFilter

    def get_queryset(self):
        queryset = super().get_queryset()
        customer_id = self.request.query_params.get('customer', None)
        is_active = self.request.query_params.get('is_active', None)
        user_id = self.request.query_params.get('user', None)
        if customer_id is not None:
            queryset = queryset.filter(customer=customer_id)
        if is_active is not None:
            queryset = queryset.filter(is_active=is_active)
        if user_id is not None:
            queryset = queryset.filter(user=user_id)
        return queryset.order_by('-start_date')


class AppointmentPageView(viewsets.ModelViewSet, RevisionMixin):
    serializer_class = AppointmentSerializer
    queryset = Appointment.objects.all()
    permission_classes = (AllowAny,)
    lookup_field = 'id'
    pagination_class = StandardPagination
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = AppointmentFilter

    def get_queryset(self):
        queryset = super().get_queryset()
        customer_id = self.request.query_params.get('customer', None)
        is_active = self.request.query_params.get('is_active', None)
        user_id = self.request.query_params.get('user', None)
        if customer_id is not None:
            queryset = queryset.filter(customer=customer_id)
        if is_active is not None:
            queryset = queryset.filter(is_active=is_active)
        if user_id is not None:
            queryset = queryset.filter(user=user_id)
        return queryset.order_by('-start_date')


# class CRUDStaffView(viewsets.ModelViewSet):
#     serializer_class = StaffSerializer
#     queryset = Staff.objects.all()
#     permission_classes = (AllowAny,)
#     lookup_field = 'id'


class CRUDAppointmentStatusView(viewsets.ModelViewSet):
    serializer_class = AppointmentStatusSerializer
    queryset = AppointmentStatus.objects.all()
    permission_classes = (AllowAny,)
    lookup_field = 'id'


class CRUDUIObjectView(viewsets.GenericViewSet, ListCreateAPIView, RetrieveUpdateDestroyAPIView):
    serializer_class = UIObjectSerializer
    queryset = UIObject.objects.all()
    permission_classes = (AllowAny,)
    lookup_field = 'id'


class CRUDRoleView(viewsets.GenericViewSet, ListCreateAPIView, RetrieveUpdateDestroyAPIView):
    serializer_class = RoleSerializer
    queryset = Role.objects.all()
    permission_classes = (AllowAny,)
    lookup_field = 'id'


class CRUDUserRoleView(viewsets.GenericViewSet, ListCreateAPIView, RetrieveUpdateDestroyAPIView):
    serializer_class = UserRoleSerializer
    queryset = UserRole.objects.all()
    permission_classes = (AllowAny,)
    lookup_field = 'id'


class CRUDRolePermissionView(viewsets.GenericViewSet, ListCreateAPIView, RetrieveUpdateDestroyAPIView):
    serializer_class = RolePermissionSerializer
    queryset = RolePermission.objects.all()
    permission_classes = (AllowAny,)
    lookup_field = 'id'


class CRUDPermissionView(viewsets.GenericViewSet, ListCreateAPIView, RetrieveUpdateDestroyAPIView):
    serializer_class = PermissionSerializer
    queryset = Permission.objects.all()
    permission_classes = (AllowAny,)
    lookup_field = 'id'


class CustomerTransferView(viewsets.ModelViewSet):
    serializer_class = CustomerTransferSerializer
    queryset = CustomerTransfer.objects.all()
    lookup_field = 'id'
    pagination_class = StandardPagination
    permission_classes = (AllowAny,)

    def get_queryset(self):
        queryset = super().get_queryset()
        # search = self.kwargs['search']
        search = self.request.query_params.get('search', None)
        if search is None:
            return queryset.order_by('-transfer_date')
        unaccented_search = unidecode.unidecode(search)
        if search != unaccented_search:
            queryset = queryset.filter(
                Q(customer__fullname__icontains=search))
        else:
            queryset = queryset.filter(
                Q(customer__fullname__unaccent__icontains=search) |
                Q(customer__code__icontains=search) |
                Q(customer__phone__icontains=search))

        return queryset.order_by('-transfer_date')


class CustomerTransferHistoryFilter(filters.FilterSet):
    transfer_date = DateFromToRangeFilter()

    fullname = filters.CharFilter(
        field_name='customer__fullname', lookup_expr='icontains')
    phone = filters.CharFilter(
        field_name='customer__phone', lookup_expr='icontains')
    code = filters.CharFilter(
        field_name='customer__code', lookup_expr='icontains')
    # email = filters.CharFilter()

    class Meta:
        model = CustomerTransferHistory

        fields = {
            # 'transfer_date': ['exact'],
            #   'customer__fullname': ['exact', 'icontains'],
            #           #   'phone': ['exact', 'icontains'],
            #           #   'code': ['exact', 'icontains'],
        }


class CustomerTransferHistoryView(mixins.RetrieveModelMixin, mixins.ListModelMixin, GenericViewSet):
    serializer_class = CustomerTransferHistorySerializer
    queryset = CustomerTransferHistory.objects.all()
    lookup_field = 'id'
    pagination_class = StandardPagination
    permission_classes = (AllowAny,)
    # filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = CustomerTransferHistoryFilter

    def get_queryset(self):
        queryset = super().get_queryset()
        # search = self.kwargs['search']
        search = self.request.query_params.get('search', None)
        if search is None:
            return queryset.order_by('-transfer_date')

        unaccented_search = unidecode.unidecode(search)
        if search != unaccented_search:
            queryset = queryset.filter(
                Q(customer__fullname__icontains=search))
        else:
            queryset = queryset.filter(
                Q(customer__fullname__unaccent__icontains=search) |
                Q(customer__code__icontains=search) |
                Q(customer__phone__icontains=search))

        return queryset.order_by('-transfer_date')


# @api_view()
# def client_history(request, client_id):
#     client = Client.objects.get(id=client_id)
#     versions = Version.objects.get_for_object(client)

#     data = versions.values('pk',
#                            'revision__date_created',
#                            'revision__user__username',
#                            'revision__comment',
#                            'pk')

#     return Response({"data": data})

class TaskTypeView(viewsets.ModelViewSet):
    serializer_class = TaskTypeSerializer
    queryset = TaskType.objects.all()
    permission_classes = (AllowAny,)
    lookup_field = 'id'


class TaskStatusView(viewsets.ModelViewSet):
    serializer_class = TaskStatusSerializer
    queryset = TaskStatus.objects.all()
    permission_classes = (AllowAny,)
    lookup_field = 'id'


class TaskPriorityView(viewsets.ModelViewSet):
    serializer_class = TaskPrioritySerializer
    queryset = TaskPriority.objects.all()
    permission_classes = (AllowAny,)
    lookup_field = 'id'


class TaskView(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
    permission_classes = (AllowAny,)
    lookup_field = 'id'

    def get_queryset(self):
        queryset = super().get_queryset()
        client_id = self.request.query_params.get('client_id', None)
        user_id = self.request.query_params.get('user', None)
        if client_id is not None:
            queryset = queryset.filter(client_id=client_id)
        if user_id is not None:
            queryset = queryset.filter(user=user_id)
        return queryset.order_by('-task_date')


class ActivityTypeView(viewsets.ModelViewSet):
    serializer_class = ActivityTypeSerializer
    queryset = ActivityType.objects.all()
    permission_classes = (AllowAny,)
    lookup_field = 'id'


class ActivityView(viewsets.ModelViewSet):
    serializer_class = ActivitySerializer
    queryset = Activity.objects.all()
    permission_classes = (AllowAny,)
    lookup_field = 'id'

    def get_queryset(self):
        queryset = super().get_queryset()
        client_id = self.request.query_params.get('client_id', None)
        created_user = self.request.query_params.get('created_user', None)
        if client_id is not None:
            queryset = queryset.filter(client_id=client_id)
        if created_user is not None:
            queryset = queryset.filter(created_user=created_user)
        return queryset.order_by('-created_date')


class LeadStatusCodeView(viewsets.ModelViewSet):
    serializer_class = LeadStatusCodeSerializer
    queryset = LeadStatusCode.objects.all()
    permission_classes = (AllowAny,)
    lookup_field = 'id'


class LeadTimeFrameView(viewsets.ModelViewSet):
    serializer_class = LeadTimeFrameSerializer
    queryset = LeadTimeFrame.objects.all()
    permission_classes = (AllowAny,)
    lookup_field = 'id'


class LeadView(viewsets.ModelViewSet):
    serializer_class = LeadSerializer
    queryset = Lead.objects.all()
    permission_classes = (AllowAny,)
    lookup_field = 'id'


class StaffView(viewsets.ModelViewSet):
    serializer_class = StaffSerializer
    queryset = Staff.objects.all()
    permission_classes = (AllowAny,)
    lookup_field = 'id'

    def get_queryset(self):
        queryset = super().get_queryset()
        # search = self.kwargs['search']
        department = self.request.query_params.get('department', None)
        if department is not None:
            queryset = queryset.filter(department=department)
        staff_group = self.request.query_params.get('staff_group', None)
        if department is not None:
            queryset = queryset.filter(staff_group=staff_group)
        search = self.request.query_params.get('search', None)
        if search is None:
            return queryset.order_by('first_name')
        unaccented_search = unidecode.unidecode(search)
        if search != unaccented_search:
            queryset = queryset.filter(
                Q(first_name__icontains=search))
        else:
            queryset = queryset.filter(
                Q(first_name__unaccent__icontains=search) |
                Q(last_name__unaccent__icontains=search) |
                Q(code__icontains=search) |
                Q(email__icontains=search))

        return queryset.order_by('first_name')


class StaffGroupView(viewsets.ModelViewSet):
    serializer_class = StaffGroupSerializer
    queryset = StaffGroup.objects.all()
    permission_classes = (AllowAny,)
    lookup_field = 'id'


class DepartmentView(viewsets.ModelViewSet):
    serializer_class = DepartmentSerializer
    queryset = Department.objects.all()
    permission_classes = (AllowAny,)
    lookup_field = 'id'


class JobTitleView(viewsets.ModelViewSet):
    serializer_class = JobTitleSerializer
    queryset = JobTitle.objects.all()
    permission_classes = (AllowAny,)
    lookup_field = 'id'
