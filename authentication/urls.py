from django.urls import path
#from rest_framework_simplejwt import views as jwt_views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,

    #UserCreate, HelloWorldView
)
#from .views import ObtainTokenPairWithColorView, UserCreate, HelloWorldView
#from . import views
from rest_framework import routers
from django.conf.urls import url, include
from django.contrib import admin
from .views import UserDetailAPI, RegisterApi, LoginApi, UserCreate, UserViewSet, ProfileView, MyTokenObtainPairView

# Register router
router = routers.SimpleRouter()
router.register('user', UserViewSet)

urlpatterns = [
    path('api/token/obtain/', TokenObtainPairView.as_view(),
         name='token_obtain_pair'),  # override sjwt stock token
    #path('api/token/', ObtainTokenPairWithColorView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(),
         name='token_refresh'),
    path('api/user/create/', UserCreate.as_view(), name="create_user"),
    path('api/', include(router.urls)),
    #path('admin/', admin.site.urls),
    path("api/get-details/", UserDetailAPI.as_view()),
    path("api/auth/profile/", ProfileView.as_view()),
    #path('api/register/', RegisterUserAPIView.as_view()),
    path('api/auth/signup/', RegisterApi.as_view()),
    #path('api/auth/signin/', LoginApi.as_view()),
    #path('api/auth/signin/', TokenObtainPairView.as_view()),
    path('api/auth/signin/', MyTokenObtainPairView.as_view()),

    #path('api/admin/', admin.site.urls),
    # path('',include('api.urls')),
    #path('api/api-token-auth', obtain_auth_token)

]
