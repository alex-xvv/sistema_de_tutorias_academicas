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
from django.contrib import messages

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
    carreras = Carrera.objects.all()
    if request.method == 'POST':
        nombres = request.POST['txtNombre']
        apellidos = request.POST['txtApellido']
        carrera_id = request.POST['slCarrera']
        try:
            carrera = Carrera.objects.get(pk=carrera_id)
            docente = Docente.objects.create(nombres=nombres, apellidos=apellidos, carrera=carrera)
            messages.success(request, 'Docente registrado exitosamente.')
            return redirect("registro_docentes")
        except Exception as e:
            messages.error(request, 'No se pudo registrar el docente: {}'.format(str(e)))
    return render(request, 'html/registro_docentes.html',{"carreras":carreras})


def registro_asignaturas(request):
    carreras = Carrera.objects.all()
    docentes = Docente.objects.all()
    if request.method == 'POST':
        nombre = request.POST['txtNombreAs']
        ciclo = request.POST['txtCiclo']
        paralelo = request.POST['txtParalelo']
        docente_id = request.POST['slDocente']
        carrera_id = request.POST['slCarrera']
        try:
            docente = Docente.objects.get(pk=docente_id)
            carrera = Carrera.objects.get(pk=carrera_id)
            asignatura = Asignatura.objects.create(nombre=nombre, ciclo=ciclo, paralelo=paralelo,
                                     docente=docente, carrera=carrera)
            messages.success(request, 'Asignatura registrada exitosamente.')
            return redirect("registro_asignaturas")
        except Exception as e:
            messages.error(request, 'No se pudo registrar la asignatura: {}'.format(str(e)))
    return render(request, 'html/registro_asignaturas.html',{"carreras":carreras, "docentes":docentes})


def registro_carreras(request):
    carreras=Carrera.objects.all()
    if request.method == 'POST':
        nombre = request.POST['txtNombre']
        facultad = request.POST['slFacultad']
        inicio_periodo = request.POST['txtInicio']
        final_periodo = request.POST['txtFin']

        carrera = Carrera.objects.create(nombre=nombre, facultad=facultad, inicio_periodo=inicio_periodo,
                        final_periodo=final_periodo)
        messages.success(request, 'Carrera registrada exitosamente.')
        return redirect("registro_carreras")
    else:
        print('No se pudo registrar Carrera.')
        #messages.error(request, 'No se pudo registrar Carrera.')
    return render(request, 'html/registro_carreras.html', { "carreras": carreras})

'''def registro_estudiantes(request):
    if request.method == 'POST':
        estudianteForm = EstudianteForm(request.POST)
        if estudianteForm.is_valid():
            estudianteForm.save()
            return redirect('registro_estudiantes')
    else:
        estudianteForm = EstudianteForm()
    return render(request, 'html/registro_estudiantes.html', {'estudianteForm': estudianteForm})'''


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

def inicio_estudiante(request):
    listaMaterias = Estudiante.objects.all()
    return render(request, 'html/inicio_estudiante.html', {"lista":listaMaterias})


