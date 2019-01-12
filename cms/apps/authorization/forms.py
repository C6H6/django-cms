from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput


class AuthForm(AuthenticationForm):
    username = forms.CharField(
        widget=TextInput(attrs={'class': 'form-control input-sm chat-input', 'placeholder': 'Username'}))
    password = forms.CharField(
        widget=PasswordInput(attrs={'class': 'form-control input-sm chat-input', 'placeholder': 'Password'}))
