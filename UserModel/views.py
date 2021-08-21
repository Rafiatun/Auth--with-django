from django.http.response import HttpResponseRedirect
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate,logout

from  UserModel.forms import RegistrationForm,AccountActivationForm
from Profile.models import Profile

def UserNameList(request):
   
    return render(request , 'profile.html')


def register_view(request , *args , **kwargs):
    user=request.user
    if user.is_authenticated:
        return HttpResponse("You are registered ")

    context={}

    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email=form.cleaned_data.get('email').lower()
            raw_password=form.cleaned_data.get('password1')
            account=authenticate(email=email , password=raw_password)
            login(request,account)
            destination=kwargs.get("next")
            if destination:
                return redirect(destination)
          
            return redirect('create_profile')

        else:
            context['registration_form'] = form
            
    else:
        form = RegistrationForm()
        context['registration_form'] = form

    return render(request, 'register.html',context)

def logout_view(request):
    logout(request)
    print('you are logged out')
    return redirect('profilepage')

def login_view(request, *args, **kwargs):
	context = {}

	user = request.user
	if user.is_authenticated: 
		return redirect('profilepage')

	destination = get_redirect_if_exists(request)
	print("destination: " + str(destination))

	if request.POST:
		form = AccountActivationForm(request.POST)
		if form.is_valid():
			email = request.POST['email']
			password = request.POST['password']
			user = authenticate(email=email, password=password)

			if user:
				login(request, user)
				if destination:
					return redirect(destination)
				return redirect('create_profile')

	else:
		form = AccountActivationForm()

	context['login_form'] = form

	return render(request, "user_login.html", context)

def get_redirect_if_exists(request):
	redirect = None
	if request.GET:
		if request.GET.get("next"):
			redirect = str(request.GET.get("next"))
	return redirect


