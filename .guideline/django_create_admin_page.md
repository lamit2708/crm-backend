# Create Administrator Page for a table/model

[Ref](https://www.youtube.com/watch?v=tXyrJi1E74k&list=PLVZgTVNoxdMksQAJI7J2IHpNW7rY7U3XI&index=9)

## Create file project/module_folder/admin.py

Example AZNOSE/crm/admin.py

## Import library for admin

```
from django.contrib import admin
from .models import *
```

## Import model from the other module folder (optional):

```
from authentication.models import *
```

## Add admin site

```
admin.site.register(Customer)
```

## Custom for the admin site for User

```
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'fullname')
    list_filter = ('fullname', 'username')
    search_fields = ('username', 'fullname',)
    exclude = ['first_name', 'last_name']
    list_per_page = 2
    pass

    def get_ordering(self, request):
        if request.user.is_superuser:
            return ('username', '-fullname')
        return ('fullname')

admin.site.register(User, UserAdmin)
```
