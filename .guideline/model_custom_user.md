# Guideline to custom the user athentication

## Customer User with the same name in model

[REF](https://www.caktusgroup.com/blog/2019/04/26/how-switch-custom-django-user-model-mid-project/)

## Import CustomUser to shell

from django.contrib.auth import get_user_model
User = get_user_model()

# Create superuser in the table user

python manage.py createsuperuser
admin
password123

http://127.0.0.1:8000/admin/
