# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import LoginForm, UserRegistrationForm
from django import views
from django.contrib.auth.models import User


def user_login(request):
	form = LoginForm(request.POST or None)
	if request.POST and form.is_valid():
		user = form.login(request)
		if user:
			label=login(request, user)
			return render(request, 'account/index.html')
	return render(request, 'account/login.html', {'form': form })



@login_required
def index(request):
	return render(request, 'account/index.html', {'section': 'home'})

def base(request):
	return render(request, 'account/base.html')

def register(request):
	if request.method == 'POST':
		form = UserRegistrationForm(request.POST)
		if form.is_valid():
			user = User.objects.create_user(username=form.cleaned_data['username'], 
										password=form.cleaned_data['password'],
										email=form.cleaned_data['email'],
										first_name=form.cleaned_data['first_name'],
										last_name=form.cleaned_data['last_name'])
			return render(request, 'account/register_sucess.html')
	else:
		print("Renderizei o GET")
		form = UserRegistrationForm()
	return render (request, 'account/register.html', {'form':form})