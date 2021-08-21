from .views import *
from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt


urlpatterns=[
    path('', views.UserNameList , name="profilepage"),
    path('login_view', views.login_view , name="login_view"),
    path('logout_view', views.logout_view , name="logout_view"),
    path('register_view', views.register_view , name="register_view"),
   


]