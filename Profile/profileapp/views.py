from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .forms import CreateUserForm, ProfileForm

from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required

from .decorators import unauthenticated_user

from django.contrib.auth.models import User

# Create your views here.

@login_required(login_url='login')
def index(request):
    return render(request, 'profileapp/home.html')


def homepage(request):
    return render(request, 'profileapp/homepage.html')


@login_required(login_url='login')
def profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            username = request.user.username
            messages.success(request, f'{username}, Your profile is updated succesfully')
            return redirect('/')
    else:
        form = ProfileForm(instance=request.user.profile)

    context = {'form': form}
    return render(request, 'profileapp/profile.html', context)



@login_required(login_url='login')
def delete_account(request):
    return HttpResponse('This is the confirmation page of delete-account.')


@unauthenticated_user
def login_user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password = password)
        if user is not None:
            login(request, user)
            messages.info(request, f'{username}, You are logged in.')
            return redirect('/')
        else:
            messages.info(request, 'Invalid username or password.')
            return redirect('login')

    return render(request, 'profileapp/login_page.html')


@unauthenticated_user
def register_user(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, 'Account is created succesfully')
            return redirect('login')
            
        else:
            context = {'form': form}
            messages.info(request, 'Invalid infromation')
            return render(request, 'profileapp/register_page.html', context)



    context = {'form': form}
    return render(request, 'profileapp/register_page.html', context)

@login_required(login_url='login')
def logout_user(request):
    logout(request)
    messages.info(request, 'You have logged out successfully')
    return redirect('login')


