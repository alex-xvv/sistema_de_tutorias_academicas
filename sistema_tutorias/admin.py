from django.contrib import admin
from .models import Persona, Carrera, Asignatura, Tutoria

@admin.register(Persona)
class PersonaAdmin(admin.ModelAdmin):
    pass

@admin.register(Carrera)
class CarreraAdmin(admin.ModelAdmin):
    pass

@admin.register(Asignatura)
class AsignaturaAdmin(admin.ModelAdmin):
    pass

@admin.register(Tutoria)
class TutoriaAdmin(admin.ModelAdmin):
    pass