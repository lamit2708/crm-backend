from django.contrib import admin
#from django.contrib.auth.admin import UserAdmin

from .models import User

admin.site.site_header = 'Admin Pannel'
#admin.site.site_title = 'Authen'
# https://www.youtube.com/watch?v=tXyrJi1E74k&list=PLVZgTVNoxdMksQAJI7J2IHpNW7rY7U3XI&index=9


class UserAdmin(admin.ModelAdmin):
    list_display = ('username',  'first_name')
    list_filter = ('first_name', 'username')
    search_fields = ('username', 'fullname',)
    # exclude = ['first_name', 'last_name']
    list_per_page = 2
    pass

    def get_ordering(self, request):
        if request.user.is_superuser:
            return ('username', '-first_name')
        return ('first_name')


admin.site.register(User, UserAdmin)
