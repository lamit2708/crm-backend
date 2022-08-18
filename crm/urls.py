from rest_framework import routers
import register
from . import views

# Register router
crmRouter = routers.SimpleRouter()
crmRouter.register('customer-type', views.CustomerTypeView)
crmRouter.register('customer-priority', views.CRUDCustomerPriorityView)
crmRouter.register('customer', views.CustomerView)
crmRouter.register('customer-source', views.CRUDCustomerSourceView)
crmRouter.register('appointment', views.AppointmentView)
crmRouter.register('appointment-page', views.AppointmentPageView)
#router.register('user', views.CRUDUserView)

crmRouter.register('appointment-status', views.CRUDAppointmentStatusView)
crmRouter.register('ui-object', views.CRUDUIObjectView)
crmRouter.register('role', views.CRUDRoleView)
crmRouter.register('user-role', views.CRUDUserRoleView)
crmRouter.register('role-permission', views.CRUDRolePermissionView)
crmRouter.register('permission', views.CRUDPermissionView)
crmRouter.register('department', views.DepartmentView)
crmRouter.register('customer-transfer', views.CustomerTransferView)
crmRouter.register('customer-transfer-history',
                   views.CustomerTransferHistoryView)
crmRouter.register('task-type',
                   views.TaskTypeView)
crmRouter.register('task-status',
                   views.TaskStatusView)
crmRouter.register('task-priority',
                   views.TaskPriorityView)
crmRouter.register('task',
                   views.TaskView)
crmRouter.register('activity-type',
                   views.ActivityTypeView)
crmRouter.register('activity',
                   views.ActivityView)
crmRouter.register('lead-status-code', views.LeadStatusCodeView)
crmRouter.register('lead-time-frame', views.LeadTimeFrameView)
crmRouter.register('lead', views.LeadView)
crmRouter.register('staff', views.StaffView)
crmRouter.register('staff-group', views.StaffGroupView)
crmRouter.register('job-title', views.JobTitleView)
