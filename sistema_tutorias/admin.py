from django.contrib import admin
from .models import *
from .models import Carrera, Asignatura, Docente

@admin.register(Docente)
class DocenteAdmin(admin.ModelAdmin):
    pass

@admin.register(Carrera)
class CarreraAdmin(admin.ModelAdmin):
    pass

@admin.register(Asignatura)
class AsignaturaAdmin(admin.ModelAdmin):
    pass


