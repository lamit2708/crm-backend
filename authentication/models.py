from django.contrib.auth.models import AbstractUser
from django.db import models
# https://www.caktusgroup.com/blog/2019/04/26/how-switch-custom-django-user-model-mid-project/


class User(AbstractUser):
    pass
    #fav_color = models.CharField(blank=True, null=True, max_length=120)
    #fullname = models.CharField(blank=True, null=True, max_length=64)

    class Meta:
        db_table = 'auth_user'
