from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from profiles.models import UserPage


def registration(request):
    if request.method == 'GET':
        return render(request, 'users/registration.html', {"form": UserCreationForm})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                b = UserPage(username_id=user.id)
                b.save()
                return redirect('index')
            except IntegrityError:
                return render(request, 'users/registration.html',
                              {"form": UserCreationForm, "error": "Логин существует"})
        else:
            return render(request, 'users/registration.html',
                          {"form": UserCreationForm,
                           'error': "Пароли не совпали"})


def login_user(request):
    if request.method == 'GET':
        return render(request, 'user/login_user.html', {"login_form": AuthenticationForm})
    else:
        user = authenticate(request, username=request.POST['username'],
                            password=request.POST['password'])
        if user is None:
            print("Неверный логин или пароль!")
            return render(request, 'users/login_user.html',
                          {"login_form": AuthenticationForm, 'error': "Неверный логин или пароль!"})
        else:
            login(request, user)
            return redirect('index')


def logout_user(request):
    if request.method == 'POST':
        logout(request)
        return redirect("index")







