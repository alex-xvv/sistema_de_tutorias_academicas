from django.contrib import admin
from .models import Persona, Carrera, Asignatura

@admin.register(Persona)
class PersonaAdmin(admin.ModelAdmin):
    pass

@admin.register(Carrera)
class CarreraAdmin(admin.ModelAdmin):
    pass

@admin.register(Asignatura)
class Asignatura(admin.ModelAdmin):
    pass