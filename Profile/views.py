from django import forms
from django.shortcuts import render,redirect
from .models import *
from .forms import ProfileForm
from django.http import HttpResponseRedirect,HttpResponse

@login_required(login_url='login_view')
def pro_info(request):
    Userinfo=Profile.objects.all()
    context={
        'userinfo':Userinfo

    }
    return render(request,'profile_info.html',context)

# Create your views here.
@login_required(login_url='login_view')
def create_profile(request):

    if request.method =="POST":
        form =ProfileForm(request.POST)
        if form.is_valid():
            
            First_Name=form.cleaned_data['First_Name']
            Last_Name=form.cleaned_data['Last_Name']
            Institution=form.cleaned_data['Institution']

            result=Profile(First_Name=First_Name,Last_Name=Last_Name,Institution=Institution)
            result.save()
            return redirect('pro_info')
        else: 
            form=ProfileForm()
            
    else:
        form=ProfileForm()

    return render(request, 'create_profile.html', {'form': form})
        