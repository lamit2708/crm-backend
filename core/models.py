from django.db import models
from django.db.models.deletion import SET_DEFAULT


class ProvinceLevel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'core_province_level'


class Province(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)
    province_level = models.ForeignKey(
        ProvinceLevel, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'core_province'


class DistrictLevel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'core_district_level'


class District(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)
    province = models.ForeignKey(
        Province, null=True, on_delete=models.SET_NULL)
    district_level = models.ForeignKey(
        DistrictLevel, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'core_district'


class WardLevel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'core_ward_level'


class Ward(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)
    district = models.ForeignKey(
        District, null=True, on_delete=models.SET_NULL)
    wards_level = models.ForeignKey(
        WardLevel, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'core_ward'
