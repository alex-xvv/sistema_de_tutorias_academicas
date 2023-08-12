from django.shortcuts import render
from  .forms import *
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import authenticate as auth_authenticate
from django.db import IntegrityError
from django.contrib.auth.decorators import user_passes_test
from .forms import CustomUserCreationForm

# Vistas de las diferentes paginas del proyecto.
def is_docente(user):
    return user.groups.filter(name='Docente').exists()


def index(request):
    es_docente = is_docente(request.user)
    es_superuser = request.user.is_superuser
    return render(request, 'html/index.html', {'es_docente': es_docente, 'es_superuser': es_superuser})


def about(request):
    return render(request, 'html/about.html')


def registro_docentes(request):
    ListaDocentes = Docente.objects.all()
    if request.method == "POST":
        docenteForm = DocenteForm(request.POST)
        if docenteForm.is_valid():
            docenteForm.save()
            return redirect('registro_docentes')
    else:
        docenteForm = DocenteForm()
    return render(request, 'html/registro_docentes.html',{'docenteForm':docenteForm, "Docente":ListaDocentes})


def registro_asignaturas(request):
    ListaAsignaturas = Asignatura.objects.all()
    if request.method == "POST":
        asignaturaForm = AsignaturaForm(request.POST)
        if asignaturaForm.is_valid():
            asignaturaForm.save()
            return redirect('registro_asignaturas')
    else:
        asignaturaForm = AsignaturaForm()
    return render(request, 'html/registro_asignaturas.html',{'asignaturaForm':asignaturaForm, "Asignatura": ListaAsignaturas})


def registro_carreras(request):
    ListaCarreras = Carrera.objects.all()
    if request.method == "POST":
        carreraForm = CarreraForm(request.POST)
        if carreraForm.is_valid():
            carreraForm.save()
            return redirect('registro_carreras')
    else:
        carreraForm = CarreraForm()
    return render(request, 'html/registro_carreras.html',{'carreraForm':carreraForm, "Carrera": ListaCarreras})


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('/')
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'html/registro.html', {'form': form})


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


@user_passes_test(is_docente)
def aceptar_tutoria(request):
    return render(request, 'html/aceptar_tutoria.html', {'es_docente': True})


def gestionar_registros(request):
    return render(request, 'html/gestionar_registros.html')
