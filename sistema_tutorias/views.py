from  .forms import *
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import authenticate as auth_authenticate
from django.db import IntegrityError
from django.contrib.auth.decorators import user_passes_test, login_required
from .forms import CustomUserCreationForm
from django.contrib import messages
from django.core.mail import send_mail
from django.http import HttpResponse

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
        correo = request.POST['txtCorreo']
        carrera_id = request.POST['slCarrera']
        horario = request.FILES.get('txtHorario')
        try:
            carrera = Carrera.objects.get(pk=carrera_id)
            docente = Docente.objects.create(nombres=nombres, apellidos=apellidos, correo=correo, carrera=carrera, horario=horario)
            messages.success(request, 'Docente registrado exitosamente.')
            return redirect("registro_docentes")
        except Exception as e:
            messages.error(request, 'No se pudo registrar el docente: {}'.format(str(e)))
    return render(request, 'html/registro_docentes.html',{"carreras":carreras})

def gestion_docentes(request):
    listaDocentes = Docente.objects.all()
    return render(request, "html/gestion_docentes.html", {"listaDocentes":listaDocentes})

def eliminar_docente(request, correo):
    docente = get_object_or_404(Docente, correo=correo)
    if docente:
        docente.delete()
        messages.success(request, 'Docente eliminado exitosamente')
        return redirect('gestion_docentes')
    else:
        messages.error(request, 'No se pudo eliminar docente')

def modificar_docente(request, correo):
    docente = get_object_or_404(Docente, correo=correo)
    lista_carreras = Carrera.objects.all()
    if request.method == 'POST':
        nuevos_nombres = request.POST['nuevos_nombres']
        nuevos_apellidos = request.POST['nuevos_apellidos']
        nuevo_correo = request.POST['nuevo_correo']
        nuevo_horario = request.FILES['nuevo_horario'] if 'nuevo_horario' in request.FILES else None
        nuevo_carrera_id = request.POST['nuevo_carrera']

        docente.nombres = nuevos_nombres
        docente.apellidos = nuevos_apellidos
        docente.correo = nuevo_correo
        if nuevo_horario:
            docente.horario = nuevo_horario
        docente.carrera_id = nuevo_carrera_id
        docente.save()

        return redirect('gestion_docentes')

    return render(request, 'html/modificar_docente.html', {'docente': docente, 'lista_carreras':lista_carreras})

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

def gestion_asignaturas(request):
    listaAsignaturas = Asignatura.objects.all()
    return render(request, "html/gestion_asignaturas.html", {"listaAsignaturas":listaAsignaturas})

def eliminar_asignatura(request, nombre):
    asignatura = get_object_or_404(Asignatura, nombre=nombre)
    if asignatura:
        asignatura.delete()
        messages.success(request, 'Asignatura eliminada exitosamente')
        return redirect('gestion_asignaturas')
    else:
        messages.error(request, 'No se pudo eliminar asignatura')

def modificar_asignatura(request, nombre):
    asignatura = get_object_or_404(Asignatura, nombre=nombre)
    lista_carreras = Carrera.objects.all()
    lista_docentes = Docente.objects.all()
    if request.method == 'POST':
        nuevo_nombre = request.POST['nuevo_nombre']
        nuevo_ciclo = request.POST['nuevo_ciclo']
        nuevo_paralelo = request.POST['nuevo_paralelo']
        nuevo_carrera_id = request.POST['nuevo_carrera']
        nuevo_docente_id = request.POST['nuevo_docente']

        asignatura.nombre = nuevo_nombre
        asignatura.ciclo = nuevo_ciclo
        asignatura.paralelo = nuevo_paralelo
        asignatura.carrera_id = nuevo_carrera_id
        asignatura.docente_id = nuevo_docente_id
        asignatura.save()

        return redirect('gestion_asignaturas')

    return render(request, 'html/modificar_asignatura.html', {'asignatura': asignatura, 'lista_carreras': lista_carreras, 'lista_docentes': lista_docentes})

def registro_carreras(request):
    carreras = Carrera.objects.all()
    if request.method == 'POST':
        nombre = request.POST['txtNombre']
        facultad = request.POST['slFacultad']
        inicio_periodo = request.POST['txtInicio']
        final_periodo = request.POST['txtFin']
        try:
            carrera = Carrera.objects.create(nombre=nombre, facultad=facultad, inicio_periodo=inicio_periodo,
                            final_periodo=final_periodo)
            messages.success(request, 'Carrera registrada exitosamente.')
            return redirect("registro_carreras")
        except Exception as e:
            messages.error(request, 'No se pudo registrar la carrera: {}'.format(str(e)))
    return render(request, 'html/registro_carreras.html', {"carreras": carreras})

def gestion_carreras(request):
    listaCarrera = Carrera.objects.all()
    return render(request, "html/gestion_carreras.html", {"listaCarrera":listaCarrera})

def eliminar_carrera(request, nombre):
    carrera = get_object_or_404(Carrera, nombre=nombre)
    if carrera:
        carrera.delete()
        messages.success(request, 'Carrera eliminada exitosamente')
        return redirect('gestion_carreras')
    else:
        messages.error(request, 'No se pudo eliminar la carrera')

def modificar_carrera(request, nombre):
    carrera = get_object_or_404(Carrera, nombre=nombre)
    if request.method == 'POST':
        nueva_nombre = request.POST['nueva_nombre']
        nueva_facultad = request.POST['nueva_facultad']
        nueva_inicio = request.POST['nueva_inicio']
        nueva_final = request.POST['nueva_final']

        carrera.nombre = nueva_nombre
        carrera.facultad = nueva_facultad
        carrera.inicio_periodo = nueva_inicio
        carrera.final_periodo = nueva_final
        carrera.save()

        return redirect('gestion_carreras')

    return render(request, 'html/modificar_carrera.html', {'carrera': carrera})

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
    user = request.user
    if user.is_authenticated:
        tutorias = Tutoria.objects.filter(asignatura__docente__correo=user.email)
        lista_estudiantes = []

        for tutoria in tutorias:
            #docente = asignatura.docente
            estudiante = tutoria.estudiante
            lista_estudiantes.append(estudiante)
        return render(request, 'html/aceptar_tutoria.html', {'lista_estudiantes': lista_estudiantes})

    return HttpResponse("No tienes permisos para acceder a esta página.")

    #return render(request, 'html/aceptar_tutoria.html', {'es_docente': True, "estudiante": estudiante})

@login_required
def enviar_solicitud(request, estudiante_id):
    #estudiante = Estudiante.objects.all()
    if request.method == 'POST':
        accion = request.POST.get('accion')

        if accion == 'aceptar':
            hora = request.POST['txthora']
            dia = request.POST['txtdia']
            tutoria_info = request.POST['txtinfotutoria']
            try:
                estudiantes = Estudiante.objects.get(id=estudiante_id)
            except Estudiante.DoesNotExist:
                return print('error no existe el estudiante')

            # Obtener el correo electrónico del usuario autenticado
            usuario = request.user
            correo_usuario = usuario.email

            # Envío de correo electrónico
            subject = f'Solicitud de Tutoría'
            message = f'Estimado/a {estudiantes.nombre},\n\nSe ha aceptado su tutoria.\n\nDetalles de la solicitud:\nHora: ' \
                      f'{hora}\nDia:{dia}\nInformación: {tutoria_info}\n\nPor favor, ponte en contacto con el estudiante ({correo_usuario}) para coordinar la tutoría.'
            from_email = correo_usuario
            recipient_list = [estudiantes.usuario]

            send_mail(subject, message, from_email, recipient_list)

            return render(request, 'html/aceptar_tutoria.html', {'accion': 'aceptada'})
        elif accion == 'denegar':
            razon_denegacion = request.POST['txttutoria']
            try:
                estudiantes = Estudiante.objects.get(id=estudiante_id)
            except Estudiante.DoesNotExist:
                return print('error no existe el estudiante')

            # Obtener el correo electrónico del usuario autenticado
            usuario = request.user
            correo_usuario = usuario.email

            # Envío de correo electrónico
            subject = f'Solicitud de Tutoría'
            message = f'Estimado/a {estudiantes.nombre},\n\nSe ha negado su tutoria.\n\nDetalles de la solicitud:\nDebido a la siguiente razo: ' \
                      f'{razon_denegacion}\n\nPor favor, ponte en contacto con el estudiante ({correo_usuario}) para coordinar la tutoría.'
            from_email = correo_usuario
            recipient_list = [estudiantes.usuario]

            send_mail(subject, message, from_email, recipient_list)
            return render(request, 'html/aceptar_tutoria.html', {'accion': 'denegada'})

    return render(request, 'html/aceptar_tutoria.html', {'estudiante_id': estudiante_id})

def gestionar_registros(request):
    return render(request, 'html/gestionar_registros.html')

def inicio_estudiante(request):
    listaMaterias = Estudiante.objects.all()
    return render(request, 'html/inicio_estudiante.html', {"lista":listaMaterias})


