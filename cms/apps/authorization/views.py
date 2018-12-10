from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib import messages


def user_login(request):
    if request.user.is_authenticated:
        return redirect('contact:index')
    form = AuthenticationForm()
    return render(request, 'authorization/login.html', {'form': form})


def check_login(request):
    form = AuthenticationForm(request.POST)

    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')

        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('contact:index')

    for message in form.get_invalid_login_error():
        messages.add_message(request, messages.ERROR, message)

    return redirect('authorization:login')


def user_registration(request):
    form = UserCreationForm()
    return render(request, 'authorization/registration.html', {'form': form})


def check_registration(request):
    form = UserCreationForm(request.POST)
    if form.is_valid():
        form.save()
        username = form.cleaned_data.get('username')
        raw_password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=raw_password)
        login(request, user)
        return redirect('contact:index')

    for message in form.errors.values():
        print(message)
        messages.add_message(request, messages.ERROR, message)

    return redirect('authorization:registration')


def user_logout(request):
    logout(request)
    return redirect('contact:index')
