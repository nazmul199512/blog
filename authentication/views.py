from django.contrib import auth
from django.contrib.auth import logout, login, authenticate
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import RegistrationForm, LoginForm
from .forms import *


# LOGIN VIEW
def user_login(request):
    next = request.GET.get('next')
    form = LoginForm(request.POST or None)
    if form.is_valid():
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        user = authenticate(email=email, password=password)
        login(request, user)
        return redirect('post:post')

    return render(request, "login.html", {'form': form})


# REGISTER VIEW
def register(request):
    next = request.GET.get('next')
    form = RegistrationForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password1')
        user.set_password(password)
        user.save()
        new_user = authenticate(email=user.email, password=password)
        login(request, new_user)
        if next:
            return redirect(next)
        return redirect('auth:login')

    return render(request, "register.html", {'form': form})


# LOGOUT VIEW
def user_logout(request):
    logout(request)
    return redirect('auth:login')


