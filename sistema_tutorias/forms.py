from django.forms import ModelForm
from .models import *
#from django import forms

class AsignaturaForm(ModelForm):
    class Meta:
        model=Asignatura
        fields='__all__'

class CarreraForm(ModelForm):
    class Meta:
        model=Carrera
        fields='__all__'

class DocenteForm(ModelForm):
    class Meta:
        model=Docente
        fields='__all__'