from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib import messages

from cms.apps.authorization.forms import AuthForm, RegistrationForm


def user_login(request):
    if request.user.is_authenticated:
        return redirect('core:index')
    form = AuthForm()
    return render(request, 'authorization/login.html', {'form': form})


def check_login(request):
    form = AuthForm(data=request.POST)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')

        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('core:index')

    for message in form.get_invalid_login_error():
        messages.add_message(request, messages.ERROR, message)

    return redirect('authorization:login')


def user_registration(request):
    form = RegistrationForm()
    return render(request, 'authorization/registration.html', {'form': form})


def check_registration(request):
    form = RegistrationForm(request.POST)
    if form.is_valid():
        form.save()
        username = form.cleaned_data.get('username')
        raw_password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=raw_password)
        login(request, user)
        return redirect('core:index')

    for message in form.errors.values():
        messages.add_message(request, messages.ERROR, message)

    return redirect('authorization:registration')


def user_logout(request):
    logout(request)
    return redirect('core:index')
