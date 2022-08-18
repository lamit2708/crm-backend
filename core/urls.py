
from . import views
from rest_framework import routers
import register
from django.conf.urls import url, include
from django.urls import path

# Register router
coreRouter = routers.SimpleRouter()
coreRouter.register('province', views.ProvinceViewSet)
coreRouter.register('district', views.DistrictViewSet)
coreRouter.register('ward', views.WardViewSet)
urlpatterns = [
    path('api/', include(coreRouter.urls)),
]
