from django.db import models
from django.contrib import auth
from django.conf import settings
from django.contrib.auth.decorators import login_required
# Create your models here.

class Profile(models.Model):
    #user = models.ForeignKey(settings.AUTH_USER_MODEL,null=True,on_delete=models.SET_NULL)
    First_Name      = models.CharField(max_length=60 , null=True ,blank =True)
    Last_Name       = models.CharField(max_length=60)
    Institution      = models.CharField(max_length=60)