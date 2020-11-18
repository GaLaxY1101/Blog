from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate

from account.models import Account

class RegistrationForm(UserCreationForm):
	email = forms.CharField(max_length=60, widget = 
	forms.TextInput(attrs={'type':'text', 'id':'email', 'class':'form-control', 'name':'email'}))

	username = forms.CharField(max_length=60, widget = 
	forms.TextInput(attrs={'type':'text', 'id':'user_name', 'class':'form-control', 'name':'username'}))
	
	password1 = forms.CharField(max_length=60, widget = 
	forms.TextInput(attrs={'type':'password', 'id':'password_1', 'class':'form-control', 'name':'password1'}))

	password2 = forms.CharField(max_length=60, widget = 
	forms.TextInput(attrs={'type':'password', 'id':'password_2', 'class':'form-control', 'name':'password2'}))


	class Meta:
		model = Account	
		fields = ('email','username','password1','password2')

class AccountAuthenticationForm(forms.ModelForm):

	password = forms.CharField(label = 'Password', widget = forms.PasswordInput)

	class Meta:
		model = Account
		fields = ('email','password')

	def clean(self):
		email = self.cleaned_data['email']
		password = self.cleaned_data['password']
		if not authenticate(email = email, password = password):
			raise forms.ValidationError('Invalid login')
