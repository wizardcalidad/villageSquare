from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

# class RegisterForm(UserCreationForm):
#
#     class Meta:
#         model = User
#         fields = forms.CharField(widget=forms.TextInput(attrs={"value": "Testing"}))
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)