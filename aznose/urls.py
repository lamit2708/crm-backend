"""aznose URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url, include
from django.urls import path
from rest_framework.schemas import get_schema_view
from crm.urls import crmRouter
#from core.urls import coreRouter
from rest_framework_simplejwt import views as jwt_views


# Register
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(crmRouter.urls)),
    # path('schema/', get_schema_view()),
    # path('user/', include('register.urls', namespace='user')),

    # path('api/token/', jwt_views.TokenObtainPairView.as_view(),         name='token_obtain_pair'),
    # path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(),         name='token_refresh'),
    path('', include('authentication.urls')),
    # path('', include('tutorials.urls')),
    path('', include('core.urls')),
    path('', include('authentication.urls')),
    path('', include('tutorials.urls')),

]
