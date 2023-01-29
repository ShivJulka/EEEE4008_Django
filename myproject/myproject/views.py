# Render HTML web pages

# import from django
from .forms import CreateUserForm
from django.contrib import messages

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from myproject.models import Profile
from django.contrib.auth.forms import UserCreationForm
from .forms import ProfileForm, LoginForm

def homePage(request):
    return render(request, "Homepage.html")


def location(request):
    return render(request, "maps/location.html")


def Registration (request):
    form = UserCreationForm(request.POST)
    #user djangos checks to hash and check details for repeats etc
    if form.is_valid():
        form.save()
        username =  form.cleaned_data.get('username')
        password= form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(request,user)
        messages.success(request,'Account '+user+' Sucessfully Created')
        return redirect('Homepage.html')

    context = {'form' :form}
    return render(request, "Accounts/Registration.html",context)


def LogIn(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request,user)
                return redirect('Homepage.html')
            else:
                form.add_error(None,'incorrect username of password')
    else:
        form = LoginForm()
    return render(request, "Accounts/LogIn.html")

def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def profile_view(request):
    if request.method=='POST':
        form = ProfileForm(request.POST, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance = request.user.profile)
    return render(request, 'Accounts/profile.html', {'form': form})



@login_required
def edit_profile(request, username):
    user = User.objects.get(username=username)
    profile = Profile.objects.get(user=user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile', username=user.username)
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'Accounts/edit_profile.html', {'form': form})



