from django.contrib import messages
from django.contrib.auth import (
	authenticate,
	get_user_model,
	login,
	logout,
	)
from django.core.exceptions import ValidationError
from django.shortcuts import render, get_object_or_404, redirect 
from .models import Pass
from .forms import CreateForm,UserLoginForm
from django import forms

# Create your views here.

def details(request): #List of passwords
	pass_detail = Pass.objects.all()
	context = {'pass_detail': pass_detail}
	return render(request, 'pass_save/index.html', context)

def create(request): #Creates New Passwords
	form = CreateForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request, "successfully Added")
		return redirect("details")
	else:
		messages.error(request, "Not successfully Added")
	context = {'form':form}
	return render(request, 'pass_save/create.html', context)

def update(request, id=None): #Updatees passwords
	instance = get_object_or_404(Pass, id=id)
	form = CreateForm(request.POST or None, instance=instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request, "successfully Updated")
		return redirect("details")
	else:
		messages.error(request, "Not successfully Updated")
	context = {'instance':instance, 'form':form}
	return render(request, 'pass_save/create.html', context)

def delete(request, id=None): #deletes passwords
	instance = get_object_or_404(Pass, id=id)
	instance.delete()
	messages.success(request, "successfully deleted")
	return redirect("details")


#Creating Accounts, login, logout

def login_view(request):
	title = "Login"
	form = UserLoginForm(request.POST or None)
	if form.is_valid():
		username = form.cleaned_data.get("username")
		password = form.cleaned_data.get("password")
		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				login(request, user)
				return redirect("details")
			else:
				raise forms.ValidationError("this user is not Active")
		else:
			raise forms.ValidationError("this user does not exist")

	context = {"title":title,
				"form":form
	}

	return render(request, "pass_save/login.html", context)


def register_view(request):
	return render(request, "login.html", context)


def logout_view(request):
	return render(request, "login.html", context)
