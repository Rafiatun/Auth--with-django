
from .views import *
from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt


urlpatterns=[
    path('create_profile', views.create_profile, name="create_profile"),
    path('pro_info', views.pro_info, name="pro_info"),
    
 

]