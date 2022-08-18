from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import viewsets
from core.serializers import DistrictSerializer, ProvinceSerializer, WardSerializer
from core.models import *
from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins

# class ProvinceViewSet(viewsets.ModelViewSet):
#     serializer_class = ProvinceSerializer
#     queryset = Province.objects.all()
#     lookup_field = 'id'
#     permission_classes = (AllowAny,)
#     http_method_names = ['get']


class ProvinceViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides the standard actions
    """
    queryset = Province.objects.all()
    serializer_class = ProvinceSerializer
    #lookup_field = 'id'
    http_method_names = ['get']
    permission_classes = (AllowAny,)

    @action(methods=['get'], detail=True)
    def district(self, request, pk=None):
        """
        Returns a list of all the group names that the given
        user belongs to.
        """
        province = self.get_object()
        districts = District.objects.filter(
            province_id=province.id).values('id', 'name')
        return Response(districts)


class DistrictViewSet(mixins.RetrieveModelMixin, GenericViewSet):
    """
    A viewset that provides the standard actions
    """
    queryset = District.objects.all()
    serializer_class = DistrictSerializer
    #lookup_field = 'id'
    http_method_names = ['get']
    permission_classes = (AllowAny,)

    @action(methods=['get'], detail=True)
    def ward(self, request, pk=None):
        """
        Returns a list of all the group names that the given
        user belongs to.
        """
        district = self.get_object()
        wardList = Ward.objects.filter(
            district_id=district.id).values('id', 'name')
        return Response(wardList)


class WardViewSet(mixins.RetrieveModelMixin, GenericViewSet):
    """
    A viewset that provides the standard actions
    """
    queryset = Ward.objects.all()
    serializer_class = WardSerializer
    #lookup_field = 'id'
    http_method_names = ['get']
    permission_classes = (AllowAny,)
