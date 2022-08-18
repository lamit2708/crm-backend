from django.conf.urls import url
from register import views

from django.urls import path

# SET THE NAMESPACE!
app_name = 'register'

# Be careful setting the name to just /login use userlogin instead!
urlpatterns=[
    path('register/', views.register, name='register'),
]