from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from tastypie.models import ApiKey

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


@login_required(login_url='khoj:login')
def search_view(request):
    if request.method == 'POST':
        form = InputForm(request.POST)
        if form.is_valid():
            # Get the input values
            input_values = map(
                int, form.cleaned_data['input_values'].split(','))

            # Sort the input values in descending order
            sorted_input_values = sorted(input_values, reverse=True)

            # Convert the sorted input values to a string [Unpacking array]
            sorted_input_values_str = ', '.join(
                str(num) for num in sorted_input_values)

            # Create an instance of Input with sorted input values
            input_instance = Input(
                input_values=sorted_input_values_str, user=request.user)
            input_instance.save()

            # Check if the search value is in the sorted input values
            # Ensure you have a 'search_value' field in your form
            search_value = form.cleaned_data['search_value']
            if search_value in sorted_input_values:
                result = True
            else:
                result = False

            return render(request, 'khoj/search.html', {'form': form, 'result': result})
    else:
        form = InputForm()
    return render(request, 'khoj/search.html', {'form': form})


@login_required
def generate_api_key(request):
    api_key, created = ApiKey.objects.get_or_create(user=request.user)
    if created:
        generated_key = api_key.key
    else:
        generated_key = api_key.key

    return render(request, 'khoj/generate_api_key.html', {'generated_key': generated_key})


def page_not_found_view(request, exception):
    return render(request, "khoj/404.html", {})
