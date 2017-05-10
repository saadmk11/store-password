from django import forms
from .models import Pass
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout,
)

User = get_user_model()

class CreateForm(forms.ModelForm): #form to add new passwords
	class Meta:
		model = Pass
		fields = ["account_name", "user_name", "password",]


class UserLoginForm(forms.Form):
	"""docstring for UserLoginForm"""
	username = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput)
	
	def clean(self, *args, **kwargs):
		username = self.cleaned_data.get("username")
		password = self.cleaned_data.get("password")
		if username and password:
			user = authenticate(username=username, password=password)	
			if not user:
				raise forms.ValidationError("User Does not Exist.")
			if not user.check_password(password):
				raise forms.ValidationError("password does not match.")
			if not user.is_active:
				raise forms.ValidationError("User is not Active.")
		return super(UserLoginForm, self).clean(*args, **kwargs)		


class UserRegistrationForm(forms.ModelForm):
	"""docstring for UserRegistrationForm"""
	password = forms.CharField(widget=forms.PasswordInput)
	password2 = forms.CharField(widget=forms.PasswordInput)

	class Meta:
		model = User
		fields = [
			"username",
			"password",
			"password2",
		]
	
	def clean_password2(self):
		password = self.cleaned_data.get("password")
		password2= self.cleaned_data.get("password2")
		if password != password2:
			raise forms.ValidationError("passwords Must Match")
		return password