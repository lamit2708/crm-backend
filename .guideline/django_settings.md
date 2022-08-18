# Production Setting Django

[REF](https://thinkster.io/tutorials/configuring-django-settings-for-production)

## Production

from conduit.settings.common import \*

## Create super user

python manage.py createsuperuser --email admin@example.com --username admin

## Django Database setting

DATABASES = {
'default': {
'ENGINE': 'django.db.backends.postgresql',
'NAME': 'db_aznose',
'USER': 'aznose',
'PASSWORD': 'aznose',
'HOST': 'localhost',
'PORT': '5432',
}
}
