from django import forms
from .models import Pass


class CreateForm(forms.ModelForm): #form to add new passwords
	class Meta:
		model = Pass
		fields = ["account_name", "user_name", "password",]


class UserLoginForm(forms.Form):
	"""docstring for UserLoginForm"""
	username = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput)
	
		