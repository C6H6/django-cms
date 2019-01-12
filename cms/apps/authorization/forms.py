from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.forms.widgets import PasswordInput, TextInput


class AuthForm(AuthenticationForm):
    username = forms.CharField(
        widget=TextInput(attrs={'class': 'form-control input-sm chat-input', 'placeholder': 'Username'}))
    password = forms.CharField(
        widget=PasswordInput(attrs={'class': 'form-control input-sm chat-input', 'placeholder': 'Password'}))


class RegistrationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    password1 = forms.CharField(label="Password", strip=False, widget=forms.PasswordInput(
        attrs={'class': 'form-control input-sm chat-input', 'placeholder': 'Password'}))
    password2 = forms.CharField(label="Password confirmation", strip=False, widget=forms.PasswordInput(
        attrs={'class': 'form-control input-sm chat-input', 'placeholder': 'Password confirmation'}))
    field_order = ['username', 'email', 'password1', 'password2']

    class Meta:
        model = get_user_model()
        fields = ("username", "email", "password1", "password2")
