from django.shortcuts import render
from  .forms import *
from django.shortcuts import redirect

# Vistas de las diferentes paginas del proyecto.
def index(request):
    return render(request, 'html/index.html')

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
