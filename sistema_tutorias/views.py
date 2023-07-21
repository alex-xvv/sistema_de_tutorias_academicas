from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import authenticate as auth_authenticate
from django.db import IntegrityError

# Vistas de las diferentes paginas del proyecto.
def index(request):
    return render(request, 'html/index.html')

def about(request):
    return render(request, 'html/about.html')

def register(request):
    if request.method == 'GET':
        return render(request, 'html/registro.html', {'form': UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                auth_login(request, user)
                return redirect('/')
            except IntegrityError:
                return render(request, 'html/registro.html', {'form': UserCreationForm(), 'error': 'El nombre de usuario ya existe. Por favor, elija otro nombre.'})

def login(request):
    if request.method == 'GET':
        return render(request, 'html/iniciosesion.html', {'form': AuthenticationForm()})
    else:
        user = auth_authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'html/iniciosesion.html', {'form': AuthenticationForm(), 'error': 'Usuario y/o contraseña incorrectos.'})
        else:
            auth_login(request, user)
            return redirect('/')

def logout(request):
    auth_logout(request)
    return redirect('/')

def pedir_tutoria(request):
    return render(request, 'html/pedir_tutoria.html')