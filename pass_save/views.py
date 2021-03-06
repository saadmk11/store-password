from django.contrib import messages
from django.contrib.auth import (
	authenticate,
	get_user_model,
	login,
	logout,
	)
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.shortcuts import render, get_object_or_404, redirect 
from .models import Pass
from .forms import CreateForm,UserLoginForm, UserRegistrationForm


# Create your views here.
@login_required(login_url='/login/')
def list(request): #List of passwords
	title = "Password Save"
	user = request.user
	pass_list = Pass.objects.filter(user=user)
	context = {'pass_list': pass_list, "title":title,}
	return render(request, 'pass_save/list.html', context)


@login_required(login_url='/login/')
def create(request): #Creates New Passwords
	title = "create"
	form = CreateForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.user = request.user
		instance.save()
		messages.success(request, "successfully Added")
		return redirect("list")
	else:
		messages.error(request, "Not successfully Added")
	context = {'title':title, 'form':form}
	return render(request, 'pass_save/create.html', context)


@login_required(login_url='/login/')
def update(request, id=None): #Updatees passwords
	title = "update"
	instance = get_object_or_404(Pass, id=id)
	form = CreateForm(request.POST or None, instance=instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request, "successfully Updated")
		return redirect("list")
	else:
		messages.error(request, "Not successfully Updated")
	context = {'title':title, 'instance':instance, 'form':form}
	return render(request, 'pass_save/create.html', context)



@login_required(login_url='/login/')
def delete(request, id=None): #deletes passwords
	instance = get_object_or_404(Pass, id=id)
	instance.delete()
	messages.success(request, "successfully deleted")
	return redirect("list")



#Creating Accounts, login, logout

def login_view(request):
	title = "Login"
	form = UserLoginForm(request.POST or None)
	if form.is_valid():
		username = form.cleaned_data.get("username")
		password = form.cleaned_data.get("password")
		user = authenticate(username=username, password=password)
		login(request, user)
		return redirect("list")

	context = {"title":title,
				"form":form
	}

	return render(request, "pass_save/login.html", context)


def register_view(request):
	title = "Register"
	form = UserRegistrationForm(request.POST or None)
	if form.is_valid():
		user = form.save(commit=False)
		password = form.cleaned_data.get("password")
		user.set_password(password)
		user.save()
		new_user = authenticate(username=user.username, password=password)
		login(request, new_user)
		return redirect("list")

	context = {"title":title, "form":form}

	return render(request, "pass_save/register.html", context)


def logout_view(request):
	logout(request)
	return redirect("login")
