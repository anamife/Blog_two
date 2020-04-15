from django.shortcuts import render, redirect
from .models import *
from django.contrib import auth 
from django.contrib.auth.forms import UserCreationForm


def login(request):
	args = {}
	if request.POST:
		username = request.POST.get('username', '')
		password = request.POST.get('password', '')
		user = auth.authenticate(username=username, password=password)
		if user is not None:
			auth.login(request, user)
			return redirect('/')
		else:
			args['login_error'] = 'Пользователь не найден'
			return render(request, 'login.html', args)

	return render(request, 'login.html', args)

def logout(request):
	auth.logout(request)
	return redirect('/')

def register(request):
	args = {}
	args['form'] = UserCreationForm()
	if request.POST:
		new_user_form = UserCreationForm(request.POST)
		if new_user_form.is_valid():
			new_user_form.save()
			new_user = auth.authenticate(username=new_user_form.cleaned_data['username'], password=new_user_form.cleaned_data['password2'])
			auth.login(request, new_user)
			return redirect('/')
		else:
			args['form'] = new_user_form
	return render(request, 'register.html', args)




	