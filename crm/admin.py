from django.contrib import admin
from .models import *
from authentication.models import *

admin.site.register(CustomerPriority)
admin.site.register(Customer)
admin.site.register(CustomerSource)
admin.site.register(Appointment)
# admin.site.register(User)

admin.site.register(AppointmentStatus)
admin.site.register(UIObject)
admin.site.register(Role)
admin.site.register(UserRole)
admin.site.register(RolePermission)
# admin.site.register(Lead)
admin.site.register(Department)
admin.site.register(StaffGroup)
admin.site.register(JobTitle)


class StaffAdmin(admin.ModelAdmin):
    list_display = ('code', 'last_name', 'first_name',
                    'job_title', 'department', 'staff_group')
    ordering = ['first_name']
    search_fields = ['first_name', 'code']
    #list_filter = ('email')
    list_per_page = 50


admin.site.register(Staff, StaffAdmin)
