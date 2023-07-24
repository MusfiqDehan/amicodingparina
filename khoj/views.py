from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import *
from .forms import *


def registerPage(request):
    if request.user.is_authenticated:
        return redirect('khoj:latest')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)

                return redirect('khoj:login')

        context = {'form': form}
        return render(request, 'khoj/register.html', context)


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('khoj:search_view')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('khoj:search_view')
            else:
                messages.info(request, 'Username OR password is incorrect')

        context = {}
        return render(request, 'khoj/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('khoj:login')


def home(request):
    context = {}
    return render(request, 'khoj/home.html', context)
